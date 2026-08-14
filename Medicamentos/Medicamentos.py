from PyQt6.QtWidgets import QWidget, QHeaderView, QTableWidgetItem, QInputDialog, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6 import uic
from BaseDatos.MySqlManager import MySqlManager
from message_box import Message_Box
from general_sistem_service import General_Sistem_Service as GSS
from almacendar_id_us_con import Almacenar_Id_Usuario_Consultorio_SG as AIUCSG


class Ventana_Medicamentos(QWidget):
    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.navegar = navegar
        self.db = db
        self.mb = Message_Box()
        uic.loadUi("Documentacion/QtDesigner/Medicamentoswidget.ui", self)

        self.btnRegistrar.clicked.connect(lambda: self.registrar_medicamento())
        self.btnModificar.clicked.connect(lambda: self.modificar_medicamento())
        self.btnEliminar.clicked.connect(lambda: self.eliminar_medicamento())
        self.btnActualizar.clicked.connect(lambda: self.refrescar_datos())
        self.btnVolver.clicked.connect(lambda: self.navegar.ir_a_ventana("menu_principal"))
        self.txtBuscar.textChanged.connect(lambda: self.cargar_datos())
        self.tableMedicamentos.cellClicked.connect(lambda fila, col: self.mostrar_detalle(fila))

        self.tableMedicamentos.setColumnCount(6)
        self.columnas_table_view = ["ID", "Medicamento", "Stock", "Mín", "Costo", "Caducidad"]
        self.tableMedicamentos.setHorizontalHeaderLabels(self.columnas_table_view)
        self.tableMedicamentos.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.tableMedicamentos.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.cargar_datos()

    def obtener_vias_administracion(self) -> list:
        try:
            with self.db.obtener_cursor() as cursor:
                cursor.execute("""
                    SELECT CONCAT(id_via_administrar_medicamento, ' ', via_administrar_medicamento) AS concat
                    FROM Via_Administrar_Medicamento
                    ORDER BY id_via_administrar_medicamento
                """)
                tupla_vias = cursor.fetchall()
            return [fila["concat"] for fila in tupla_vias]
        except Exception as e:
            print(f"Error critico: {e}")
            self.mb.message_box(self, "error", "Error", "No se lograron cargar las vías de administración")
            return []

    def seleccionar_via(self, id_actual=None):
        vias = self.obtener_vias_administracion()
        if not vias:
            return None
        inicio = 0
        if id_actual:
            for i, texto in enumerate(vias):
                if GSS.obtener_solo_numeros(texto) == id_actual:
                    inicio = i
                    break
        via, ok = QInputDialog.getItem(
            self,
            "Vía de administración",
            "Seleccione la vía de administración:",
            vias,
            inicio,
            False
        )
        if not ok:
            return None
        id_via = GSS.obtener_solo_numeros(via)
        if not id_via:
            self.mb.message_box(self, "info", "Atención", "Seleccione una vía de administración válida")
            return None
        return id_via

    def cargar_datos(self):
        self.tableMedicamentos.setRowCount(0)
        buscar = self.txtBuscar.text().strip()
        sql = """
            SELECT m.id_medicamento, m.medicamento_name, m.medicamento_cantidad,
                   m.medicamento_min, m.medicamento_caducidad, m.medicamento_costo,
                   m.medicamento_dosis, m.id_via_administrar_medicamento,
                   co.consultorio_name, v.via_administrar_medicamento
            FROM Medicamento m
            JOIN Consultorio co ON m.id_consultorio = co.id_consultorio
            JOIN Via_Administrar_Medicamento v ON m.id_via_administrar_medicamento = v.id_via_administrar_medicamento
        """
        args = ()
        if buscar:
            sql += " WHERE m.medicamento_name LIKE %s"
            args = (f"%{buscar}%",)
        try:
            with self.db.obtener_cursor() as cursor:
                cursor.execute(sql, args)
                datos = cursor.fetchall()
            if datos:
                for fila, med in enumerate(datos):
                    self.tableMedicamentos.insertRow(fila)
                    item_id = QTableWidgetItem(str(med["id_medicamento"]))
                    item_id.setData(Qt.ItemDataRole.UserRole, med)
                    self.tableMedicamentos.setItem(fila, 0, item_id)
                    self.tableMedicamentos.setItem(fila, 1, QTableWidgetItem(str(med["medicamento_name"])))
                    self.tableMedicamentos.setItem(fila, 2, QTableWidgetItem(str(med["medicamento_cantidad"])))
                    self.tableMedicamentos.setItem(fila, 3, QTableWidgetItem(str(med["medicamento_min"])))
                    self.tableMedicamentos.setItem(fila, 4, QTableWidgetItem(str(med["medicamento_costo"])))
                    self.tableMedicamentos.setItem(fila, 5, QTableWidgetItem(str(med["medicamento_caducidad"])))
            else:
                print("No hay datos que cargar")
        except Exception as e:
            print(f"Error critico: {e}")
            self.mb.message_box(self, "error", "Error", "No se pudieron cargar los medicamentos")

    def mostrar_detalle(self, fila):
        item = self.tableMedicamentos.item(fila, 0)
        if not item:
            return
        med = item.data(Qt.ItemDataRole.UserRole)
        if med:
            detalle = (
                f"<b>Nombre:</b> {med['medicamento_name']}<br>"
                f"<b>Stock:</b> {med['medicamento_cantidad']} (Mín: {med['medicamento_min']})<br>"
                f"<b>Costo:</b> ${med['medicamento_costo']}<br>"
                f"<b>Caducidad:</b> {med['medicamento_caducidad']}<br>"
                f"<b>Dosis:</b> {med['medicamento_dosis']}<br>"
                f"<b>Vía:</b> {med['via_administrar_medicamento']}<br>"
                f"<b>Consultorio:</b> {med['consultorio_name']}"
            )
            self.lblDetalle.setText(detalle)

    def medicamento_seleccionado(self):
        fila = self.tableMedicamentos.currentRow()
        if fila < 0:
            self.mb.message_box(self, "info", "Atención", "Seleccione un medicamento de la tabla")
            return None
        item = self.tableMedicamentos.item(fila, 0)
        return item.data(Qt.ItemDataRole.UserRole) if item else None

    def registrar_medicamento(self):
        nombre, ok = QInputDialog.getText(self, "Nuevo Medicamento", "Nombre del medicamento:")
        if not ok or not nombre.strip():
            return
        nombre = nombre.strip()
        cantidad, ok = QInputDialog.getInt(self, "Nuevo Medicamento", "Cantidad disponible en stock:", 10, 0, 10000)
        if not ok:
            return
        min_stock, ok = QInputDialog.getInt(self, "Nuevo Medicamento", "Cantidad mínima de alerta:", 2, 0, 500)
        if not ok:
            return
        caducidad, ok = QInputDialog.getText(self, "Nuevo Medicamento", "Fecha de caducidad (YYYY-MM-DD):", text="2027-12-31")
        if not ok:
            return
        dosis, ok = QInputDialog.getText(self, "Nuevo Medicamento", "Dosis general predeterminada:", text="1 cada 8 horas")
        if not ok:
            return
        costo, ok = QInputDialog.getDouble(self, "Nuevo Medicamento", "Costo unitario ($):", 0.0, 0.0, 9999.99, 2)
        if not ok:
            return

        id_via = self.seleccionar_via()
        if not id_via:
            return
        id_consultorio = AIUCSG.obetner_id_consultorio()

        try:
            with self.db.obtener_cursor() as cursor:
                sql = """
                    INSERT INTO Medicamento
                    (medicamento_name, medicamento_cantidad, medicamento_min, medicamento_caducidad,
                     medicamento_dosis, medicamento_costo, id_consultorio, id_via_administrar_medicamento)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
                cursor.execute(sql, (nombre, cantidad, min_stock, caducidad, dosis, costo, id_consultorio, id_via))
                self.db.commit_conexion()
            self.mb.message_box(self, "info", "Éxito", "Medicamento registrado correctamente.")
            self.refrescar_datos()
        except Exception as e:
            print(f"Error critico: {e}")
            self.mb.message_box(self, "error", "Error", "No se pudo registrar el medicamento")

    def modificar_medicamento(self):
        med = self.medicamento_seleccionado()
        if not med:
            return

        id_via = self.seleccionar_via(med["id_via_administrar_medicamento"])
        if not id_via:
            return
        nueva_cantidad, ok = QInputDialog.getInt(self, "Modificar Medicamento", f"Actualizar stock para '{med['medicamento_name']}':", int(med['medicamento_cantidad']), 0, 10000)
        if not ok:
            return
        nuevo_costo, ok = QInputDialog.getDouble(self, "Modificar Medicamento", "Actualizar costo unitario ($):", float(med['medicamento_costo']), 0.0, 9999.99, 2)
        if not ok:
            return

        try:
            with self.db.obtener_cursor() as cursor:
                sql = """
                    UPDATE Medicamento
                    SET medicamento_cantidad = %s,
                        medicamento_costo = %s,
                        id_via_administrar_medicamento = %s
                    WHERE id_medicamento = %s
                """
                cursor.execute(sql, (nueva_cantidad, nuevo_costo, id_via, med['id_medicamento']))
                self.db.commit_conexion()
            self.mb.message_box(self, "info", "Éxito", "Medicamento actualizado correctamente.")
            self.refrescar_datos()
        except Exception as e:
            print(f"Error critico: {e}")
            self.mb.message_box(self, "error", "Error", "No se pudo actualizar el medicamento")

    def eliminar_medicamento(self):
        med = self.medicamento_seleccionado()
        if not med:
            return
        if self.mb.message_box(self, "question", "Eliminar", f"¿Está seguro de eliminar el medicamento '{med['medicamento_name']}'?") == QMessageBox.StandardButton.Yes:
            try:
                with self.db.obtener_cursor() as cursor:
                    sql = "DELETE FROM Medicamento WHERE id_medicamento = %s"
                    cursor.execute(sql, (med['id_medicamento'],))
                    self.db.commit_conexion()
                self.mb.message_box(self, "info", "Eliminado", "Medicamento eliminado.")
                self.lblDetalle.setText("Seleccione un medicamento para ver sus detalles.")
                self.refrescar_datos()
            except Exception as e:
                print(f"Error critico: {e}")
                self.mb.message_box(self, "error", "Error", "No se pudo eliminar (podría estar vinculado a una receta)")

    def refrescar_datos(self):
        self.cargar_datos()
