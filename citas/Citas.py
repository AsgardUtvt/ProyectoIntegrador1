from PyQt6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem, QInputDialog, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6 import uic
from BaseDatos.MySqlManager import MySqlManager
from message_box import Message_Box
from general_sistem_service import General_Sistem_Service as GSS
from almacendar_id_us_con import Almacenar_Id_Usuario_Consultorio_SG as AIUCSG


class Ventana_Citas(QWidget):
    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.navegar = navegar
        self.db = db
        self.mb = Message_Box()
        uic.loadUi("Documentacion/QtDesigner/citasWidget.ui", self)

        self.btnGen.clicked.connect(lambda: self.generar_cita())
        self.btnMod.clicked.connect(lambda: self.modificar_cita())
        self.btnEli.clicked.connect(lambda: self.eliminar_cita())
        self.btnAct.clicked.connect(lambda: self.refrescar_datos())
        self.btnVolver.clicked.connect(lambda: self.navegar.ir_a_ventana("menu_principal"))
        self.calendar.selectionChanged.connect(lambda: self.cargar_datos())
        self.tableCitas.cellClicked.connect(lambda fila, col: self.mostrar_detalle(fila))

        self.tableCitas.setColumnCount(4)
        self.columnas_table_view = ["ID", "Paciente", "Fecha", "Duración"]
        self.tableCitas.setHorizontalHeaderLabels(self.columnas_table_view)
        self.tableCitas.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.tableCitas.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.cargar_datos()

    def obtener_pacientes(self) -> list:
        try:
            with self.db.obtener_cursor() as cursor:
                cursor.execute("""
                    SELECT CONCAT(id_paciente, ' ', paciente_name, ' ', paciente_paterno) AS concat
                    FROM Paciente
                    ORDER BY id_paciente
                """)
                tupla_pacientes = cursor.fetchall()
            return [fila["concat"] for fila in tupla_pacientes]
        except Exception as e:
            print(f"Error critico: {e}")
            self.mb.message_box(self, "error", "Error", "No se lograron cargar los pacientes")
            return []

    def obtener_estados_cita(self) -> list:
        try:
            with self.db.obtener_cursor() as cursor:
                cursor.execute("""
                    SELECT CONCAT(id_estado_cita, ' ', estado_cita) AS concat
                    FROM Estado_Cita
                    ORDER BY id_estado_cita
                """)
                tupla_estados = cursor.fetchall()
            return [fila["concat"] for fila in tupla_estados]
        except Exception as e:
            print(f"Error critico: {e}")
            self.mb.message_box(self, "error", "Error", "No se lograron cargar los estados de cita")
            return []

    def cargar_datos(self):
        self.tableCitas.setRowCount(0)
        fecha = self.calendar.selectedDate().toString("yyyy-MM-dd")
        try:
            with self.db.obtener_cursor() as cursor:
                cursor.execute("""
                    SELECT c.id_cita, c.cita_date, c.cita_duracion, c.cita_nota,
                           c.id_paciente, c.id_consultorio, c.id_estado_cita, c.id_tratamiento,
                           CONCAT(p.paciente_name, ' ', p.paciente_paterno) AS paciente,
                           e.estado_cita
                    FROM Cita c
                    JOIN Paciente p ON c.id_paciente = p.id_paciente
                    LEFT JOIN Estado_Cita e ON c.id_estado_cita = e.id_estado_cita
                    WHERE DATE(c.cita_date) = %s
                    ORDER BY c.cita_date
                """, (fecha,))
                datos = cursor.fetchall()
            if datos:
                for fila, cita in enumerate(datos):
                    self.tableCitas.insertRow(fila)
                    item_id = QTableWidgetItem(str(cita["id_cita"]))
                    item_id.setData(Qt.ItemDataRole.UserRole, cita)
                    self.tableCitas.setItem(fila, 0, item_id)
                    self.tableCitas.setItem(fila, 1, QTableWidgetItem(str(cita["paciente"])))
                    self.tableCitas.setItem(fila, 2, QTableWidgetItem(str(cita["cita_date"])))
                    self.tableCitas.setItem(fila, 3, QTableWidgetItem(str(cita["cita_duracion"])))
            else:
                print("No hay citas para esta fecha")
        except Exception as e:
            print(f"Error critico: {e}")
            self.mb.message_box(self, "error", "Error", "No se pudieron cargar las citas")

    def mostrar_detalle(self, fila):
        item = self.tableCitas.item(fila, 0)
        if not item:
            return
        cita = item.data(Qt.ItemDataRole.UserRole)
        if cita:
            self.lblDet.setText(
                f"<b>Paciente:</b> {cita['paciente']}<br>"
                f"<b>Fecha:</b> {cita['cita_date']}<br>"
                f"<b>Duración:</b> {cita['cita_duracion']}<br>"
                f"<b>Nota:</b> {cita['cita_nota']}<br>"
                f"<b>Estado:</b> {cita['estado_cita']}"
            )

    def cita_seleccionada(self):
        fila = self.tableCitas.currentRow()
        if fila < 0:
            self.mb.message_box(self, "info", "Atención", "Seleccione una cita de la tabla")
            return None
        item = self.tableCitas.item(fila, 0)
        return item.data(Qt.ItemDataRole.UserRole) if item else None

    def generar_cita(self):
        fecha = self.calendar.selectedDate().toString("yyyy-MM-dd")

        pacientes = self.obtener_pacientes()
        if not pacientes:
            return
        paciente, ok = QInputDialog.getItem(self, "Nueva Cita", "Paciente:", pacientes, 0, False)
        if not ok:
            return
        id_paciente = GSS.obtener_solo_numeros(paciente)
        if not id_paciente:
            self.mb.message_box(self, "info", "Atención", "Seleccione un paciente válido")
            return

        hora, ok = QInputDialog.getText(self, "Nueva Cita", "Hora (HH:MM:SS):", text="09:00:00")
        if not ok or not hora.strip():
            return
        duracion, ok = QInputDialog.getText(self, "Nueva Cita", "Duración (HH:MM:SS):", text="01:00:00")
        if not ok or not duracion.strip():
            return
        nota, ok = QInputDialog.getText(self, "Nueva Cita", "Nota (opcional):")
        if not ok:
            return

        estados = self.obtener_estados_cita()
        if not estados:
            return
        estado, ok = QInputDialog.getItem(self, "Nueva Cita", "Estado de la cita:", estados, 0, False)
        if not ok:
            return
        id_estado = GSS.obtener_solo_numeros(estado)
        if not id_estado:
            self.mb.message_box(self, "info", "Atención", "Seleccione un estado válido")
            return

        try:
            with self.db.obtener_cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Cita
                    (cita_date, cita_duracion, cita_nota, id_paciente, id_consultorio, id_estado_cita)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (f"{fecha} {hora.strip()}", duracion.strip(), nota.strip() or None,
                      id_paciente, AIUCSG.obetner_id_consultorio(), id_estado))
                self.db.commit_conexion()
            self.mb.message_box(self, "info", "Éxito", "Cita generada correctamente.")
            self.refrescar_datos()
        except Exception as e:
            print(f"Error critico: {e}")
            self.mb.message_box(self, "error", "Error", "No se pudo generar la cita")

    def modificar_cita(self):
        cita = self.cita_seleccionada()
        if not cita:
            return

        fecha_original = cita["cita_date"]
        if hasattr(fecha_original, "date"):
            fecha_original = fecha_original.date().isoformat()
        hora_actual = cita["cita_date"]
        if hasattr(hora_actual, "time"):
            hora_actual = hora_actual.time().strftime("%H:%M:%S")

        hora, ok = QInputDialog.getText(self, "Modificar Cita", "Nueva hora (HH:MM:SS):", text=str(hora_actual))
        if not ok or not hora.strip():
            return
        duracion, ok = QInputDialog.getText(self, "Modificar Cita", "Nueva duración (HH:MM:SS):", text=str(cita["cita_duracion"]))
        if not ok or not duracion.strip():
            return
        nota, ok = QInputDialog.getText(self, "Modificar Cita", "Nota:", text=str(cita["cita_nota"] or ""))
        if not ok:
            return
        try:
            with self.db.obtener_cursor() as cursor:
                cursor.execute("""
                    UPDATE Cita
                    SET cita_date = %s,
                        cita_duracion = %s,
                        cita_nota = %s
                    WHERE id_cita = %s
                """, (f"{fecha_original} {hora.strip()}", duracion.strip(), nota.strip() or None, cita["id_cita"]))
                self.db.commit_conexion()
            self.mb.message_box(self, "info", "Éxito", "Cita actualizada correctamente.")
            self.refrescar_datos()
        except Exception as e:
            print(f"Error critico: {e}")
            self.mb.message_box(self, "error", "Error", "No se pudo actualizar la cita")

    def eliminar_cita(self):
        cita = self.cita_seleccionada()
        if not cita:
            return
        if self.mb.message_box(self, "question", "Eliminar", f"¿Está seguro de eliminar la cita {cita['id_cita']}?") == QMessageBox.StandardButton.Yes:
            try:
                with self.db.obtener_cursor() as cursor:
                    cursor.execute("DELETE FROM Cita WHERE id_cita = %s", (cita["id_cita"],))
                    self.db.commit_conexion()
                self.mb.message_box(self, "info", "Eliminado", "Cita eliminada.")
                self.lblDet.setText("Seleccione una cita.")
                self.refrescar_datos()
            except Exception as e:
                print(f"Error critico: {e}")
                self.mb.message_box(self, "error", "Error", "No se pudo eliminar la cita")

    def refrescar_datos(self):
        self.cargar_datos()
