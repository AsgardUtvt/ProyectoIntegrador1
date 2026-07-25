import os
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QScrollArea, QVBoxLayout, QTableWidgetItem, QMessageBox
from PyQt6.QtCore import QDate, Qt
from PyQt6.QtGui import QIntValidator

class Ventana_Pacientes(QWidget):
    def __init__(self, db, navegar=None):
        super().__init__()
        self.db = db
        self.navegar = navegar
        self.paciente_seleccionado_id = None

        # -------------------------------------------------------------
        # 1. FIX DE SCROLL: Cargar contenido y forzar altura mínima
        # -------------------------------------------------------------
        self.contenido_widget = QWidget()
        
        dir_actual = os.path.dirname(__file__)
        ruta_ui = os.path.join(dir_actual, "pacientes.ui")
        uic.loadUi(ruta_ui, self.contenido_widget)

        # FORZAR ALTURA MÍNIMA: Esto obliga al QScrollArea a mostrar la barra
        self.contenido_widget.setMinimumHeight(1100) 

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.contenido_widget)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn) # Forzar que aparezca siempre
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(scroll_area)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # -------------------------------------------------------------
        # 2. VALIDACIONES DE TELÉFONO Y TEXTO
        # -------------------------------------------------------------
        self._aplicar_validaciones()

        # -------------------------------------------------------------
        # 3. CONEXIÓN DE EVENTOS
        # -------------------------------------------------------------
        # Crear
        self.contenido_widget.date_nacimiento.setDate(QDate.currentDate())
        self.contenido_widget.btn_guardar.clicked.connect(self._crear_paciente)

        # Modificar
        self.contenido_widget.date_nacimiento_2.setDate(QDate.currentDate())
        self.contenido_widget.btn_buscar.clicked.connect(self._buscar_pacientes_modificar)
        self.contenido_widget.tbl_pacientes.itemSelectionChanged.connect(self._cargar_paciente_seleccionado)
        self.contenido_widget.btn_actualizar_paciente.clicked.connect(self._actualizar_paciente)

        # Suspender
        self.contenido_widget.btn_buscar_susp.clicked.connect(self._buscar_pacientes_suspender)
        self.contenido_widget.busquedas_suspender.itemSelectionChanged.connect(self._cargar_paciente_suspender)
        self.contenido_widget.btn_suspender_paciente.clicked.connect(self._suspender_paciente)

    def _aplicar_validaciones(self):
        w = self.contenido_widget

        # 1. Teléfono: Solo enteros y MÁXIMO 10 dígitos exactamente
        validador_num = QIntValidator(0, 2147483647, self)
        
        w.txt_telefono.setValidator(validador_num)
        w.txt_telefono.setMaxLength(10)
        
        w.txt_telefono_2.setValidator(validador_num)
        w.txt_telefono_2.setMaxLength(10)

        # 2. Capitalizar primera letra en LineEdits
        line_edits = [
            w.txt_nombre, w.txt_apellido_paterno, w.txt_apellido_materno,
            w.txt_nombre_2, w.txt_apellido_paterno_2, w.txt_apellido_materno_2
        ]
        for le in line_edits:
            le.textChanged.connect(lambda text, widget=le: self._capitalizar_line_edit(widget, text))

        # 3. Capitalizar primera letra en TextEdits (Dirección y Alergias)
        text_edits = [
            w.text_direccion, w.text_alergias,
            w.text_direccion_2, w.text_alergias_2
        ]
        for te in text_edits:
            te.textChanged.connect(lambda widget=te: self._capitalizar_text_edit(widget))

    def _capitalizar_line_edit(self, widget, text):
        if not text:
            return
        cap_text = text.title()
        if text != cap_text:
            pos = widget.cursorPosition()
            widget.blockSignals(True)
            widget.setText(cap_text)
            widget.setCursorPosition(pos)
            widget.blockSignals(False)

    def _capitalizar_text_edit(self, widget):
        text = widget.toPlainText()
        if text and len(text) > 0 and text[0].islower():
            cursor = widget.textCursor()
            pos = cursor.position()
            cap_text = text[0].upper() + text[1:]
            widget.blockSignals(True)
            widget.setPlainText(cap_text)
            cursor.setPosition(pos)
            widget.setTextCursor(cursor)
            widget.blockSignals(False)

    # =================================================================
    # MÉTODOS DE BASE DE DATOS (Crear, Modificar, Suspender)
    # =================================================================
    def _crear_paciente(self):
        w = self.contenido_widget
        nombre = w.txt_nombre.text().strip()
        paterno = w.txt_apellido_paterno.text().strip()
        materno = w.txt_apellido_materno.text().strip()
        fecha_nac = w.date_nacimiento.date().toString("yyyy-MM-dd")
        genero = w.cmb_genero.currentText()
        telefono = w.txt_telefono.text().strip()
        email = w.txt_email.text().strip()
        direccion = w.text_direccion.toPlainText().strip()
        alergias = w.text_alergias.toPlainText().strip()

        if not nombre or not paterno:
            QMessageBox.warning(self, "Atención", "El nombre y apellido paterno son obligatorios.")
            return

        query = """
            INSERT INTO paciente (nombre, primer_apellido, segundo_apellido, fecha_nacimiento, genero, telefono, email, direccion, alergias, estatus)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, 'Activo')
        """
        try:
            with self.db.obtener_cursor() as cursor:
                cursor.execute(query, (nombre, paterno, materno, fecha_nac, genero, telefono, email, direccion, alergias))
            QMessageBox.information(self, "Éxito", "¡Paciente registrado exitosamente!")
            self._limpiar_crear()
        except Exception as e:
            QMessageBox.critical(self, "Error BD", f"No se pudo guardar el paciente:\n{e}")

    def _limpiar_crear(self):
        w = self.contenido_widget
        w.txt_nombre.clear()
        w.txt_apellido_paterno.clear()
        w.txt_apellido_materno.clear()
        w.date_nacimiento.setDate(QDate.currentDate())
        w.txt_telefono.clear()
        w.txt_email.clear()
        w.text_direccion.clear()
        w.text_alergias.clear()

    def _buscar_pacientes_modificar(self):
        w = self.contenido_widget
        criterio = w.txt_buscar_paciente.text().strip()
        tbl = w.tbl_pacientes
        tbl.setRowCount(0)

        query = """
            SELECT id_paciente, CONCAT(nombre, ' ', primer_apellido, ' ', IFNULL(segundo_apellido, '')) AS nombre_completo, estatus
            FROM paciente 
            WHERE (nombre LIKE %s OR primer_apellido LIKE %s) AND estatus = 'Activo'
        """
        try:
            with self.db.obtener_cursor() as cursor:
                cursor.execute(query, (f"%{criterio}%", f"%{criterio}%"))
                res = cursor.fetchall()

                for row_idx, p in enumerate(res):
                    tbl.insertRow(row_idx)
                    tbl.setItem(row_idx, 0, QTableWidgetItem(str(p['id_paciente'])))
                    tbl.setItem(row_idx, 1, QTableWidgetItem(p['nombre_completo']))
                    tbl.setItem(row_idx, 2, QTableWidgetItem(p['estatus']))
        except Exception as e:
            print(f"Error al buscar pacientes: {e}")

    def _cargar_paciente_seleccionado(self):
        w = self.contenido_widget
        tbl = w.tbl_pacientes
        row = tbl.currentRow()
        if row < 0:
            return

        id_paciente = int(tbl.item(row, 0).text())
        self.paciente_seleccionado_id = id_paciente

        query = "SELECT * FROM paciente WHERE id_paciente = %s"
        try:
            with self.db.obtener_cursor() as cursor:
                cursor.execute(query, (id_paciente,))
                p = cursor.fetchone()
                if p:
                    w.txt_nombre_2.setText(p.get('nombre', ''))
                    w.txt_apellido_paterno_2.setText(p.get('primer_apellido', ''))
                    w.txt_apellido_materno_2.setText(p.get('segundo_apellido', ''))
                    
                    if p.get('fecha_nacimiento'):
                        w.date_nacimiento_2.setDate(QDate.fromString(str(p['fecha_nacimiento']), "yyyy-MM-dd"))

                    index_gen = w.cmb_genero_2.findText(p.get('genero', 'Femenino'))
                    if index_gen >= 0:
                        w.cmb_genero_2.setCurrentIndex(index_gen)

                    w.txt_telefono_2.setText(p.get('telefono', ''))
                    w.txt_email_2.setText(p.get('email', ''))
                    w.text_direccion_2.setText(p.get('direccion', ''))
                    w.text_alergias_2.setText(p.get('alergias', ''))
        except Exception as e:
            print(f"Error al cargar detalle: {e}")

    def _actualizar_paciente(self):
        if not self.paciente_seleccionado_id:
            QMessageBox.warning(self, "Atención", "Selecciona primero un paciente de la tabla.")
            return

        w = self.contenido_widget
        nombre = w.txt_nombre_2.text().strip()
        paterno = w.txt_apellido_paterno_2.text().strip()
        materno = w.txt_apellido_materno_2.text().strip()
        fecha_nac = w.date_nacimiento_2.date().toString("yyyy-MM-dd")
        genero = w.cmb_genero_2.currentText()
        telefono = w.txt_telefono_2.text().strip()
        email = w.txt_email_2.text().strip()
        direccion = w.text_direccion_2.toPlainText().strip()
        alergias = w.text_alergias_2.toPlainText().strip()

        query = """
            UPDATE paciente 
            SET nombre=%s, primer_apellido=%s, segundo_apellido=%s, fecha_nacimiento=%s,
                genero=%s, telefono=%s, email=%s, direccion=%s, alergias=%s
            WHERE id_paciente=%s
        """
        try:
            with self.db.obtener_cursor() as cursor:
                cursor.execute(query, (nombre, paterno, materno, fecha_nac, genero, telefono, email, direccion, alergias, self.paciente_seleccionado_id))
            QMessageBox.information(self, "Éxito", "¡Datos del paciente actualizados correctamente!")
            self._buscar_pacientes_modificar()
        except Exception as e:
            QMessageBox.critical(self, "Error BD", f"No se pudo actualizar:\n{e}")

    def _buscar_pacientes_suspender(self):
        w = self.contenido_widget
        criterio = w.cmb_paciente_suspender.text().strip() if hasattr(w.cmb_paciente_suspender, 'text') else ""
        tbl = w.busquedas_suspender
        tbl.setRowCount(0)

        query = """
            SELECT id_paciente, CONCAT(nombre, ' ', primer_apellido) AS nombre_completo, estatus
            FROM paciente 
            WHERE (nombre LIKE %s OR primer_apellido LIKE %s)
        """
        try:
            with self.db.obtener_cursor() as cursor:
                cursor.execute(query, (f"%{criterio}%", f"%{criterio}%"))
                res = cursor.fetchall()

                for row_idx, p in enumerate(res):
                    tbl.insertRow(row_idx)
                    tbl.setItem(row_idx, 0, QTableWidgetItem(str(p['id_paciente'])))
                    tbl.setItem(row_idx, 1, QTableWidgetItem(p['nombre_completo']))
                    tbl.setItem(row_idx, 2, QTableWidgetItem(p['estatus']))
        except Exception as e:
            print(f"Error al buscar suspender: {e}")

    def _cargar_paciente_suspender(self):
        w = self.contenido_widget
        tbl = w.busquedas_suspender
        row = tbl.currentRow()
        if row < 0:
            return

        estatus_actual = tbl.item(row, 2).text()
        if hasattr(w.chk_activo, 'setChecked'):
            w.chk_activo.setChecked(estatus_actual == 'Activo')

    def _suspender_paciente(self):
        w = self.contenido_widget
        tbl = w.busquedas_suspender
        row = tbl.currentRow()
        if row < 0:
            QMessageBox.warning(self, "Atención", "Selecciona un paciente de la tabla para suspender.")
            return

        id_paciente = int(tbl.item(row, 0).text())
        motivo = w.txt_motivo_suspension.toPlainText().strip() if hasattr(w.txt_motivo_suspension, 'toPlainText') else w.txt_motivo_suspension.text().strip()

        if not motivo:
            QMessageBox.warning(self, "Atención", "Por favor ingresa un motivo de baja/suspensión.")
            return

        query = "UPDATE paciente SET estatus = 'Inactivo', motivo_baja = %s WHERE id_paciente = %s"
        try:
            with self.db.obtener_cursor() as cursor:
                cursor.execute(query, (motivo, id_paciente))
            QMessageBox.information(self, "Éxito", "El paciente ha sido suspendido (inactivado) correctamente.")
            self._buscar_pacientes_suspender()
        except Exception as e:
            QMessageBox.critical(self, "Error BD", f"No se pudo suspender:\n{e}")