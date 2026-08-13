import sys
import os

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QPushButton, QLabel, QMessageBox, QInputDialog, QListWidget
)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), ".." )))
from BaseDatos.MySqlManager import MySqlManager

class MedicamentosWindow(QMainWindow):
    def __init__(self, db: MySqlManager, menu_principal_callback=None):
        super().__init__()
        self.db = db
        self.menu_principal_callback = menu_principal_callback
        
        self.init_ui()
        
    def init_ui(self):
        self.setWindowTitle("SIHMED - Menú de Medicamentos")
        self.resize(800, 500)
        
        central_widget = QWidget()
        main_layout = QHBoxLayout(central_widget)

        # --- SECCIÓN IZQUIERDA: Listado e Inventario de Medicamentos ---
        left_layout = QVBoxLayout()
        
        self.label_titulo = QLabel("Gestión de Inventario de Medicamentos")
        self.label_titulo.setStyleSheet("font-size: 16px; font-weight: bold;")
        left_layout.addWidget(self.label_titulo)

        self.label_info_meds = QLabel("Lista de Medicamentos Registrados:")
        self.label_info_meds.setStyleSheet("font-weight: bold; margin-top: 10px;")
        left_layout.addWidget(self.label_info_meds)

        # Lista visual de medicamentos
        self.list_medicamentos = QListWidget()
        self.list_medicamentos.itemClicked.connect(self.mostrar_detalle_medicamento)
        left_layout.addWidget(self.list_medicamentos)

        # Etiqueta para detalles extendidos del medicamento seleccionado
        self.label_detalle = QLabel("Selecciona un medicamento de la lista para ver sus detalles.")
        self.label_detalle.setStyleSheet("background-color: #f8f9fa; border: 1px solid #ddd; padding: 10px;")
        left_layout.addWidget(self.label_detalle)

        main_layout.addLayout(left_layout, stretch=2)

        # --- SECCIÓN DERECHA: Botones de Acción ---
        right_layout = QVBoxLayout()
        right_layout.addStretch()

        # Botón Registrar Medicamento
        self.btn_generar = QPushButton("Registrar Medicamento")
        self.btn_generar.setStyleSheet("background-color: #2ecc71; color: white; padding: 10px; font-weight: bold;")
        self.btn_generar.clicked.connect(self.generar_medicamento)
        right_layout.addWidget(self.btn_generar)

        # Botón Modificar Medicamento
        self.btn_modificar = QPushButton("Modificar Medicamento")
        self.btn_modificar.setStyleSheet("background-color: #f39c12; color: white; padding: 10px; font-weight: bold;")
        self.btn_modificar.clicked.connect(self.modificar_medicamento)
        right_layout.addWidget(self.btn_modificar)

        # Botón Eliminar Medicamento
        self.btn_eliminar = QPushButton("Eliminar Medicamento")
        self.btn_eliminar.setStyleSheet("background-color: #e74c3c; color: white; padding: 10px; font-weight: bold;")
        self.btn_eliminar.clicked.connect(self.eliminar_medicamento)
        right_layout.addWidget(self.btn_eliminar)

        right_layout.addStretch()

        # Botón Volver al Menú Principal
        self.btn_volver = QPushButton("Volver al Menú")
        self.btn_volver.setStyleSheet("background-color: #95a5a6; color: white; padding: 10px;")
        self.btn_volver.clicked.connect(self.volver_menu)
        right_layout.addWidget(self.btn_volver)

        main_layout.addLayout(right_layout, stretch=1)

        self.setCentralWidget(central_widget)
        
        # Cargar los medicamentos al iniciar la ventana
        self.cargar_medicamentos()

    # --- LÓGICA DE LAS ACCIONES CONECTADA A LA BD ---

    def cargar_medicamentos(self):
        """Consulta la base de datos y llena la lista visual con los medicamentos existentes."""
        self.list_medicamentos.clear()
        try:
            query = """
                SELECT m.id_medicamento, m.medicamento_name, m.medicamento_cantidad, 
                       m.medicamento_min, m.medicamento_caducidad, m.medicamento_costo,
                       co.consultorio_name, v.via_administrar_medicamento
                FROM Medicamento m
                JOIN Consultorio co ON m.id_consultorio = co.id_consultorio
                JOIN Via_Administrar_Medicamento v ON m.id_via_administrar_medicamento = v.id_via_administrar_medicamento
            """
            datos = self.db.fetchall(query)
            if datos:
                for med in datos:
                    item_text = f"[ID: {med.get('id_medicamento')}] {med.get('medicamento_name')} (Stock: {med.get('medicamento_cantidad')})"
                    self.list_medicamentos.addItem(item_text)
                    # Almacenamos el diccionario con los datos completos en el item
                    self.list_medicamentos.item(self.list_medicamentos.count() - 1).setData(0x0100, med)
                
        except Exception as err:
            QMessageBox.warning(self, "Error", f"No se pudieron cargar los medicamentos:\n{err}")

    def mostrar_detalle_medicamento(self, item):
        """Muestra la información detallada del medicamento seleccionado."""
        med = item.data(0x0100)
        if med:
            detalle = (
                f"<b>Nombre:</b> {med.get('medicamento_name')}<br>"
                f"<b>Cantidad en Stock:</b> {med.get('medicamento_cantidad')} (Mínimo: {med.get('medicamento_min')})<br>"
                f"<b>Costo Unitario:</b> ${med.get('medicamento_costo')}<br>"
                f"<b>Caducidad:</b> {med.get('medicamento_caducidad')}<br>"
                f"<b>Vía de Administración:</b> {med.get('via_administrar_medicamento')}<br>"
                f"<b>Consultorio:</b> {med.get('consultorio_name')}"
            )
            self.label_detalle.setText(detalle)

    def generar_medicamento(self):
        """Registra un nuevo medicamento en la base de datos."""
        nombre, ok = QInputDialog.getText(self, "Nuevo Medicamento", "Nombre del medicamento:")
        if not ok or not nombre.strip(): return
        
        cantidad, ok = QInputDialog.getInt(self, "Nuevo Medicamento", "Cantidad disponible en stock:", 10, 0, 10000)
        if not ok: return
        
        min_stock, ok = QInputDialog.getInt(self, "Nuevo Medicamento", "Cantidad mínima de alerta (Stock min):", 2, 0, 500)
        if not ok: return

        caducidad, ok = QInputDialog.getText(self, "Nuevo Medicamento", "Fecha de caducidad (YYYY-MM-DD):", text="2027-12-31")
        if not ok: return

        dosis, ok = QInputDialog.getText(self, "Nuevo Medicamento", "Dosis general predeterminada:", text="1 cada 8 horas")
        if not ok: return

        costo, ok = QInputDialog.getDouble(self, "Nuevo Medicamento", "Costo unitario ($):", 0.0, 0.0, 9999.99, 2)
        if not ok: return

        id_consultorio, ok = QInputDialog.getInt(self, "Nuevo Medicamento", "ID del Consultorio al que pertenece:")
        if not ok: return

        id_via, ok = QInputDialog.getInt(self, "Nuevo Medicamento", "ID de la Vía de Administración (ej. 1):", 1)
        if not ok: return

        try:
            query = """
                INSERT INTO Medicamento 
                (medicamento_name, medicamento_cantidad, medicamento_min, medicamento_caducidad, 
                 medicamento_dosis, medicamento_costo, id_consultorio, id_via_administrar_medicamento)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            filas = self.db.execute(query, (nombre, cantidad, min_stock, caducidad, dosis, costo, id_consultorio, id_via))
            if filas is not None and filas > 0:
                QMessageBox.information(self, "Éxito", "Medicamento registrado correctamente.")
                self.cargar_medicamentos()
            else:
                QMessageBox.warning(self, "Atención", "No se pudo registrar el medicamento.")
        except Exception as err:
            QMessageBox.critical(self, "Error", f"No se pudo registrar:\n{err}")

    def modificar_medicamento(self):
        """Modifica el stock y costo del medicamento seleccionado."""
        item_actual = self.list_medicamentos.currentItem()
        if not item_actual:
            QMessageBox.warning(self, "Atención", "Seleccione un medicamento de la lista para modificar.")
            return

        med = item_actual.data(0x0100)
        id_med = med.get('id_medicamento')

        nueva_cantidad, ok = QInputDialog.getInt(self, "Modificar Medicamento", f"Actualizar stock para '{med.get('medicamento_name')}':", med.get('medicamento_cantidad', 0), 0, 10000)
        if not ok: return

        nuevo_costo, ok = QInputDialog.getDouble(self, "Modificar Medicamento", "Actualizar costo unitario ($):", float(med.get('medicamento_costo', 0.0)), 0.0, 9999.99, 2)
        if not ok: return

        try:
            query = "UPDATE Medicamento SET medicamento_cantidad = %s, medicamento_costo = %s WHERE id_medicamento = %s"
            filas = self.db.execute(query, (nueva_cantidad, nuevo_costo, id_med))
            if filas is not None and filas > 0:
                QMessageBox.information(self, "Éxito", "Medicamento actualizado correctamente.")
                self.cargar_medicamentos()
            else:
                QMessageBox.warning(self, "Atención", "No se realizaron cambios en el medicamento.")
        except Exception as err:
            QMessageBox.critical(self, "Error", f"No se pudo actualizar:\n{err}")

    def eliminar_medicamento(self):
        """Elimina un medicamento de la base de datos."""
        item_actual = self.list_medicamentos.currentItem()
        if not item_actual:
            QMessageBox.warning(self, "Atención", "Seleccione un medicamento de la lista para eliminar.")
            return

        med = item_actual.data(0x0100)
        
        confirmacion = QMessageBox.question(
            self, "Confirmar Eliminación", 
            f"¿Está seguro de eliminar el medicamento '{med.get('medicamento_name')}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if confirmacion == QMessageBox.StandardButton.Yes:
            try:
                query = "DELETE FROM Medicamento WHERE id_medicamento = %s"
                filas = self.db.execute(query, (med.get('id_medicamento'),))
                if filas is not None and filas > 0:
                    QMessageBox.information(self, "Éxito", "Medicamento eliminado.")
                    self.cargar_medicamentos()
                    self.label_detalle.setText("Selecciona un medicamento de la lista para ver sus detalles.")
                else:
                    QMessageBox.warning(self, "Atención", "No se pudo eliminar el medicamento.")
            except Exception as err:
                QMessageBox.critical(self, "Error", f"No se pudo eliminar (podría estar vinculado a una receta):\n{err}")

