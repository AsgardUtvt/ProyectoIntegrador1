import sys
import os
from PyQt6.QtWidgets import QWidget, QTableWidgetItem
from PyQt6 import uic
from PyQt6.QtCore import Qt
from BaseDatos.MySqlManager import MySqlManager
from message_box import Message_Box

class MedicamentosWindow(QWidget):
    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.db = db
        self.navegar = navegar
        self.mb = Message_Box()
        uic.loadUi("../Documentacion/QtDesigner/Medicamentoswidget.ui", self)

        # Configuración inicial de la tabla
        self.configurar_tabla()

        # Conexión de Botones de la interfaz .ui
        if hasattr(self, "btnRegistrar"):
            self.btnRegistrar.clicked.connect(self.generar_medicamento)
        if hasattr(self, "btnModificar"):
            self.btnModificar.clicked.connect(self.modificar_medicamento)
        if hasattr(self, "btnEliminar"):
            self.btnEliminar.clicked.connect(self.eliminar_medicamento)
        if hasattr(self, "btnActualizar"):
            self.btnActualizar.clicked.connect(self.cargar_medicamentos)
            
    
        if hasattr(self, "tableMedicamentos"):
            self.tableMedicamentos.itemSelectionChanged.connect(self.mostrar_detalle_medicamento)
        if hasattr(self, "txtBuscar"):
            self.txtBuscar.textChanged.connect(self.filtrar_medicamentos)

        ##se supone deberia mostrar los medicamentos existentesal ingresar  a la foking vista pero alch ya no se ni que pedo si dios quiere esta baina va a jalar
        self.cargar_medicamentos()

    def configurar_tabla(self):
        """Configura las columnas de la tabla basada en el esquema del .ui."""
        if not hasattr(self, "tableMedicamentos"):
            return
        tabla = self.tableMedicamentos
        tabla.setColumnCount(6)
        tabla.setHorizontalHeaderLabels([
            "ID", "Medicamento", "Stock", "Mínimo", "Caducidad", "Costo ($)"
        ])
        tabla.verticalHeader().setVisible(False)
        tabla.setAlternatingRowColors(True)
        tabla.horizontalHeader().setStretchLastSection(True)
        tabla.setSelectionBehavior(tabla.SelectionBehavior.SelectRows)
        tabla.setEditTriggers(tabla.EditTrigger.NoEditTriggers)

    def cargar_medicamentos(self):
        """Consulta la base de datos y llena la tabla visual."""
        try:
            query = """
                SELECT m.id_medicamento, m.medicamento_name, m.medicamento_cantidad, 
                       m.medicamento_min, m.medicamento_caducidad, m.medicamento_costo,
                       m.medicamento_dosis, co.consultorio_name, v.via_administrar_medicamento
                FROM Medicamento m
                JOIN Consultorio co ON m.id_consultorio = co.id_consultorio
                JOIN Via_Administrar_Medicamento v ON m.id_via_administrar_medicamento = v.id_via_administrar_medicamento
            """
            datos = self.db.fetchall(query)
            self.actualizar_tabla_visual(datos if datos else [])
        except Exception as err:
            self.mb.message_box(self, "error", "Error de Base de Datos", f"No se pudieron cargar los medicamentos:\n{err}")

    def actualizar_tabla_visual(self, datos):
        """Inserta los registros en la QTableWidget del .ui."""
        if not hasattr(self, "tableMedicamentos"):
            return
        tabla = self.tableMedicamentos
        tabla.setRowCount(len(datos))

        for fila, med in enumerate(datos):
            item_id = QTableWidgetItem(str(med.get("id_medicamento", "")))
            item_nombre = QTableWidgetItem(str(med.get("medicamento_name", "")))
            item_stock = QTableWidgetItem(str(med.get("medicamento_cantidad", "")))
            item_min = QTableWidgetItem(str(med.get("medicamento_min", "")))
            item_cad = QTableWidgetItem(str(med.get("medicamento_caducidad", "")))
            item_costo = QTableWidgetItem(str(med.get("medicamento_costo", "")))

            # diccionario completo para consulta rapida 
            item_id.setData(Qt.ItemDataRole.UserRole, med)

            tabla.setItem(fila, 0, item_id)
            tabla.setItem(fila, 1, item_nombre)
            tabla.setItem(fila, 2, item_stock)
            tabla.setItem(fila, 3, item_min)
            tabla.setItem(fila, 4, item_cad)
            tabla.setItem(fila, 5, item_costo)

        if hasattr(self, "lblDetalle"):
            self.lblDetalle.setText("Seleccione un medicamento para ver sus detalles.")

    def mostrar_detalle_medicamento(self):
        """Muestra la información detallada en el apartado lblDetalle del .ui."""
        tabla = self.tableMedicamentos
        seleccion = tabla.selectedItems()
        if not seleccion:
            return

        fila = seleccion[0].row()
        item_id = tabla.item(fila, 0)
        med = item_id.data(Qt.ItemDataRole.UserRole)

        if med and hasattr(self, "lblDetalle"):
            detalle = (
                f"<b>Nombre:</b> {med.get('medicamento_name')}<br>"
                f"<b>Cantidad en Stock:</b> {med.get('medicamento_cantidad')} (Mínimo: {med.get('medicamento_min')})<br>"
                f"<b>Costo Unitario:</b> ${med.get('medicamento_costo')}<br>"
                f"<b>Caducidad:</b> {med.get('medicamento_caducidad')}<br>"
                f"<b>Dosis Predeterminada:</b> {med.get('medicamento_dosis')}<br>"
                f"<b>Vía de Administración:</b> {med.get('via_administrar_medicamento')}<br>"
                f"<b>Consultorio:</b> {med.get('consultorio_name')}"
            )
            self.lblDetalle.setText(detalle)

    def filtrar_medicamentos(self):
        """Filtra las filas de la tabla según el texto ingresado en txtBuscar."""
        if not hasattr(self, "txtBuscar") or not hasattr(self, "tableMedicamentos"):
            return
        texto = self.txtBuscar.text().lower()
        tabla = self.tableMedicamentos
        for fila in range(tabla.rowCount()):
            item_nombre = tabla.item(fila, 1)
            if item_nombre:
                match = texto in item_nombre.text().lower()
                tabla.setRowHidden(fila, not match)

    def generar_medicamento(self):
        """Acción para dar de alta un medicamento (conectarse con formulario de registro si se requiere)."""
        self.mb.message_box(self, "info", "Alta de Medicamento", "Aquí se abrirá el formulario para registrar un nuevo medicamento.")

    def modificar_medicamento(self):
        """Acción para modificar el medicamento seleccionado."""
        tabla = self.tableMedicamentos
        if not tabla.selectedItems():
            self.mb.message_box(self, "info", "Atención", "Seleccione un medicamento de la tabla para modificar.")
            return
        fila = tabla.selectedItems()[0].row()
        id_med = tabla.item(fila, 0).text()
        self.mb.message_box(self, "info", "Modificar Medicamento", f"Modificar el medicamento con ID: {id_med}")

    def eliminar_medicamento(self):
        """Elimina el medicamento seleccionado tras confirmación."""
        tabla = self.tableMedicamentos
        if not tabla.selectedItems():
            self.mb.message_box(self, "info", "Atención", "Seleccione un medicamento de la tabla para eliminar.")
            return

        fila = tabla.selectedItems()[0].row()
        item_id = tabla.item(fila, 0)
        med = item_id.data(Qt.ItemDataRole.UserRole)
        id_med = med.get('id_medicamento')
        nombre_med = med.get('medicamento_name')

        if self.mb.message_box(self, "question", "Confirmar Eliminación", f"¿Está seguro de eliminar el medicamento '{nombre_med}'?"):
            try:
                query = "DELETE FROM Medicamento WHERE id_medicamento = %s"
                filas = self.db.execute(query, (id_med,))
                if filas is not None and filas > 0:
                    self.mb.message_box(self, "info", "Éxito", "Medicamento eliminado correctamente.")
                    self.cargar_medicamentos()
                else:
                    self.mb.message_box(self, "warning", "Atención", "No se pudo eliminar el medicamento.")
            except Exception as err:
                self.mb.message_box(self, "error", "Error", f"No se pudo eliminar (podría estar vinculado a una receta):\n{err}")
