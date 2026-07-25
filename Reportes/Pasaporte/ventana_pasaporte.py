import os
import qrcode
from io import BytesIO

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtGui import QPixmap, QImage

class Ventana_Pasaporte(QWidget):
    def __init__(self, db, navegar=None):
        super().__init__()
        self.db = db
        self.navegar = navegar

        # .ui
        dir_actual = os.path.dirname(__file__)
        ruta_ui = os.path.join(dir_actual, "pasaporte.ui")
        uic.loadUi(ruta_ui, self)

        #ComboBox editable para permitir búsquedas por texto
        self.cmb_paciente_pasaporte.setEditable(True)

        #conectar eventos
        self.cmb_paciente_pasaporte.currentIndexChanged.connect(self._cargar_datos_paciente)
        self.pushButton.clicked.connect(self._guardar_y_generar_qr)

        #cargar lista inicial de pacientes
        self._cargar_pacientes()

    def _cargar_pacientes(self):
        """Carga la lista de pacientes en el ComboBox editable."""
        self.cmb_paciente_pasaporte.clear()
        self.cmb_paciente_pasaporte.addItem("Escribe o selecciona un paciente...", None)
        
        query = "SELECT id_paciente, CONCAT(nombre, ' ', primer_apellido) AS nombre_completo FROM paciente ORDER BY nombre_completo"
        try:
            with self.db.obtener_cursor() as cursor:
                cursor.execute(query)
                pacientes = cursor.fetchall()
                for p in pacientes:
                    self.cmb_paciente_pasaporte.addItem(p['nombre_completo'], p['id_paciente'])
        except Exception as e:
            print(f"Error al cargar pacientes: {e}")

    def _cargar_datos_paciente(self):
        """Si el paciente ya tiene pasaporte/ficha médica creada en la BD, autocompleta los campos."""
        id_paciente = self.cmb_paciente_pasaporte.currentData()
        if not id_paciente:
            self._limpiar_campos()
            return

        query = """
            SELECT tipo_sangre, alergias_emergencia, padecimientos, contacto_emergencia 
            FROM pasaporte_medico 
            WHERE id_paciente = %s
        """
        try:
            with self.db.obtener_cursor() as cursor:
                cursor.execute(query, (id_paciente,))
                data = cursor.fetchone()
                if data:
                    self.txt_tipo_sangre.setText(data.get('tipo_sangre', ''))
                    self.txt_alergias_emergencia.setText(data.get('alergias_emergencia', ''))
                    self.txt_padecimientos.setText(data.get('padecimientos', ''))
                    self.txt_contacto_emergencia.setText(data.get('contacto_emergencia', ''))
                else:
                    self._limpiar_campos()
        except Exception as e:
            # Si aún no existe la tabla o no hay datos registrados para ese paciente
            self._limpiar_campos()

    def _limpiar_campos(self):
        """Limpia los campos de texto y la imagen QR."""
        self.txt_tipo_sangre.clear()
        self.txt_alergias_emergencia.clear()
        self.txt_padecimientos.clear()
        self.txt_contacto_emergencia.clear()
        self.lbl_codigo_qr.clear()
        self.lbl_codigo_qr.setText("Aquí aparecerá el QR")

    def _guardar_y_generar_qr(self):
        """Guarda en BD y genera el código QR personalizado."""
        id_paciente = self.cmb_paciente_pasaporte.currentData()
        nombre_paciente = self.cmb_paciente_pasaporte.currentText()

        if not id_paciente:
            QMessageBox.warning(self, "Atención", "Por favor selecciona un paciente válido de la lista.")
            return

        tipo_sangre = self.txt_tipo_sangre.text().strip()
        alergias = self.txt_alergias_emergencia.text().strip()
        padecimientos = self.txt_padecimientos.text().strip()
        contacto = self.txt_contacto_emergencia.text().strip()

        if not tipo_sangre or not contacto:
            QMessageBox.warning(self, "Atención", "El Tipo de Sangre y el Contacto de Emergencia son obligatorios.")
            return

        #}Guardar o Actualizar en la base de datos (UPSERT)
        query_guardar = """
            INSERT INTO pasaporte_medico (id_paciente, tipo_sangre, alergias_emergencia, padecimientos, contacto_emergencia)
            VALUES (%s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
                tipo_sangre = VALUES(tipo_sangre),
                alergias_emergencia = VALUES(alergias_emergencia),
                padecimientos = VALUES(padecimientos),
                contacto_emergencia = VALUES(contacto_emergencia)
        """
        try:
            with self.db.obtener_cursor() as cursor:
                cursor.execute(query_guardar, (id_paciente, tipo_sangre, alergias, padecimientos, contacto))

            #construir el texto estructurado para el QR
            contenido_qr = (
                f"=== PASAPORTE MÉDICO DE EMERGENCIA ===\n"
                f"Paciente: {nombre_paciente}\n"
                f"Tipo de Sangre: {tipo_sangre}\n"
                f"Alergias Graves: {alergias if alergias else 'Ninguna'}\n"
                f"Padecimientos: {padecimientos if padecimientos else 'Ninguno'}\n"
                f"Contacto de Emergencia: {contacto}"
            )

            #Generar la imagen QR en memoria usando python-qrcode
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=6,
                border=2,
            )
            qr.add_data(contenido_qr)
            qr.make(fit=True)

            img_qr = qr.make_image(fill_color="black", back_color="white")

            # Convertir PIL Image a QPixmap para mostrarlo en el QLabel
            buffer = BytesIO()
            img_qr.save(buffer, format="PNG")
            qimage = QImage()
            qimage.loadFromData(buffer.getvalue())
            pixmap = QPixmap.fromImage(qimage)

            # Escalar pixmap al tamaño del Label manteniendo la relación de aspecto
            self.lbl_codigo_qr.setPixmap(
                pixmap.scaled(
                    self.lbl_codigo_qr.width(), 
                    self.lbl_codigo_qr.height(), 
                    aspectRatioMode=1 # Qt.AspectRatioMode.KeepAspectRatio
                )
            )

            QMessageBox.information(self, "Éxito", "¡Pasaporte médico guardado y código QR generado correctamente!")

        except Exception as e:
            QMessageBox.critical(self, "Error BD", f"No se pudieron guardar los datos:\n{e}")