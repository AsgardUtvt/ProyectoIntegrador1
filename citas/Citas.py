import sys
import os
from PyQt6.QtWidgets import QWidget, QMessageBox, QTableWidgetItem
from PyQt6 import uic
from PyQt6.QtCore import QDate
from BaseDatos.MySqlManager import MySqlManager

class CitasWindow(QWidget):
    def __init__(self, db: MySqlManager, navegar=None):
        super().__init__()
        self.db = db
        self.navegar = navegar
        self.init_ui()

    def init_ui(self):
        # -------------------------
        # Carga del archivo .ui con ruta relativa segura
        # -------------------------
        directorio_actual = os.path.dirname(os.path.abspath(__file__))
        ruta_ui = os.path.join(directorio_actual, "..", "Documentacion", "QtDesigner", "citasSIHMED.ui")
        
        if not os.path.exists(ruta_ui):
            QMessageBox.critical(None, "Error crítico", f"No se encontró el archivo de interfaz en:\n{ruta_ui}")
            sys.exit(1)

        uic.loadUi(ruta_ui, self)

        # -------------------------
        # Configuración inicial de la tabla y calendario
        # -------------------------
        self.configurar_tabla()
        self.calendar.setSelectedDate(QDate.currentDate())

        # -------------------------
        # Conexión de Botones y Eventos
        # -------------------------
        self.btnAct.clicked.connect(self.cargar_citas)
        self.btnGen.clicked.connect(self.generar_cita)
        self.btnMod.clicked.connect(self.modificar_cita)
        self.btnEli.clicked.connect(self.eliminar_cita)
        
        if hasattr(self, "btnVolver") and self.navegar:
            self.btnVolver.clicked.connect(self.navegar)

        self.calendar.selectionChanged.connect(self.cargar_citas)
        self.tableCitas.itemSelectionChanged.connect(self.mostrar_detalle_cita)

        # Cargar las citas del día actual al iniciar
        self.cargar_citas()

    def configurar_tabla(self):
        """Configura las columnas y propiedades de la tabla de citas basándose en el esquema SQL."""
        if not hasattr(self, "tableCitas"):
            return
        tabla = self.tableCitas
        tabla.setColumnCount(5)
        tabla.setHorizontalHeaderLabels([
            "ID Cita", "Fecha y Hora", "Paciente", "Consultorio", "Estado"
        ])
        tabla.verticalHeader().setVisible(False)
        tabla.setAlternatingRowColors(True)
        tabla.horizontalHeader().setStretchLastSection(True)
        tabla.setSelectionBehavior(tabla.SelectionBehavior.SelectRows)
        tabla.setEditTriggers(tabla.EditTrigger.NoEditTriggers)

    # --- LÓGICA DE DATOS CON MySqlManager ---

    def cargar_citas(self):
        """Consulta las citas de la base de datos filtrando por la fecha seleccionada en el calendario."""
        fecha_seleccionada = self.calendar.selectedDate().toString("yyyy-MM-dd")
        try:
            query = """
                SELECT c.id_cita, c.cita_date, 
                       CONCAT(p.paciente_name, ' ', p.paciente_paterno) AS paciente_completo,
                       co.consultorio_name, ec.estado_cita
                FROM Cita c
                JOIN Paciente p ON c.id_paciente = p.id_paciente
                JOIN Consultorio co ON c.id_consultorio = co.id_consultorio
                JOIN Estado_Cita ec ON c.id_estado_cita = ec.id_estado_cita
                WHERE DATE(c.cita_date) = %s
                ORDER BY c.cita_date
            """
            datos = self.db.fetchall(query, (fecha_seleccionada,))
            self.actualizar_tabla_visual(datos if datos is not None else [])
        except Exception as err:
            QMessageBox.warning(self, "Error de Base de Datos", f"No se pudieron cargar las citas:\n{err}")

    def actualizar_tabla_visual(self, datos):
        """Inserta los registros en la tabla de la interfaz."""
        tabla = self.tableCitas
        tabla.setRowCount(len(datos))

        for fila, cita in enumerate(datos):
            tabla.setItem(fila, 0, QTableWidgetItem(str(cita.get("id_cita", ""))))
            tabla.setItem(fila, 1, QTableWidgetItem(str(cita.get("cita_date", ""))))
            tabla.setItem(fila, 2, QTableWidgetItem(str(cita.get("paciente_completo", ""))))
            tabla.setItem(fila, 3, QTableWidgetItem(str(cita.get("consultorio_name", ""))))
            tabla.setItem(fila, 4, QTableWidgetItem(str(cita.get("estado_cita", ""))))

        if hasattr(self, "lblDet"):
            self.lblDet.setText("Seleccione una cita.")

    def mostrar_detalle_cita(self):
        """Muestra la información completa de la cita seleccionada en el recuadro de detalles."""
        tabla = self.tableCitas
        seleccion = tabla.selectedItems()
        if not seleccion:
            return

        fila = seleccion[0].row()
        id_cita = tabla.item(fila, 0).text()

        try:
            query = """
                SELECT c.id_cita, c.cita_date, c.cita_duracion, c.cita_nota,
                       CONCAT(p.paciente_name, ' ', p.paciente_paterno, ' ', p.paciente_materno) AS paciente,
                       p.paciente_telefono, co.consultorio_name, ec.estado_cita, t.tratamiento_name
                FROM Cita c
                JOIN Paciente p ON c.id_paciente = p.id_paciente
                JOIN Consultorio co ON c.id_consultorio = co.id_consultorio
                JOIN Estado_Cita ec ON c.id_estado_cita = ec.id_estado_cita
                JOIN Tratamiento t ON c.id_tratamiento = t.id_tratamiento
                WHERE c.id_cita = %s
            """
            resultado = self.db.fetchone(query, (id_cita,))
            if resultado:
                texto_detalle = (
                    f"ID Cita: {resultado.get('id_cita')}\n"
                    f"Fecha y Hora: {resultado.get('cita_date')} (Duración: {resultado.get('cita_duracion')})\n"
                    f"Paciente: {resultado.get('paciente')} (Tel: {resultado.get('paciente_telefono')})\n"
                    f"Consultorio: {resultado.get('consultorio_name')}\n"
                    f"Tratamiento: {resultado.get('tratamiento_name')}\n"
                    f"Estado: {resultado.get('estado_cita')}\n"
                    f"Nota: {resultado.get('cita_nota', 'Sin notas')}"
                )
                if hasattr(self, "lblDet"):
                    self.lblDet.setText(texto_detalle)
        except Exception as err:
            QMessageBox.critical(self, "Error", f"No se pudo obtener el detalle de la cita:\n{err}")

    def generar_cita(self):
        """Lógica para registrar una nueva cita (pendiente de conectar con formulario de alta)."""
        QMessageBox.information(self, "Generar Cita", "Aquí se abrirá el formulario para registrar una nueva cita.")

    def modificar_cita(self):
        """Lógica para modificar la cita seleccionada."""
        tabla = self.tableCitas
        if not tabla.selectedItems():
            QMessageBox.warning(self, "Advertencia", "Seleccione una cita para modificar.")
            return
        fila = tabla.selectedItems()[0].row()
        id_cita = tabla.item(fila, 0).text()
        QMessageBox.information(self, "Modificar Cita", f"Modificar la cita con ID: {id_cita}")

    def eliminar_cita(self):
        """Elimina o da de baja la cita seleccionada tras confirmación."""
        tabla = self.tableCitas
        if not tabla.selectedItems():
            QMessageBox.warning(self, "Advertencia", "Seleccione una cita para eliminar.")
            return

        fila = tabla.selectedItems()[0].row()
        id_cita = tabla.item(fila, 0).text()

        respuesta = QMessageBox.question(
            self, "Confirmar eliminación",
            f"¿Está seguro de que desea eliminar la cita ID {id_cita}?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if respuesta == QMessageBox.StandardButton.Yes:
            try:
                query = "DELETE FROM Cita WHERE id_cita = %s"
                filas_afectadas = self.db.execute(query, (id_cita,))
                if filas_afectadas is not None and filas_afectadas > 0:
                    QMessageBox.information(self, "Éxito", "Cita eliminada correctamente.")
                    self.cargar_citas()
                else:
                    QMessageBox.warning(self, "Atención", "No se pudo eliminar la cita.")
            except Exception as err:
                QMessageBox.critical(self, "Error de Base de Datos", f"No se pudo eliminar la cita:\n{err}")