import os
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QTableWidgetItem, QMessageBox
from PyQt6.QtCore import QDate

class Ventana_Ticket_Pago(QWidget):
    def __init__(self, db, navegar=None):
        super().__init__()
        self.db = db
        self.navegar = navegar

        #cargar .ui
        dir_actual = os.path.dirname(__file__)
        ruta_ui = os.path.join(dir_actual, "ticket_pago.ui")
        uic.loadUi(ruta_ui, self)

        #valores por defecto
        self.date_ticket.setDate(QDate.currentDate())
        self.medicamentos_db = {}  #{id: {'nombre': x, 'precio': y}}
        
        #eventos
        self.cmb_buscar_medicamento.currentIndexChanged.connect(self._actualizar_precio_medicamento)
        self.btn_agregar_item.clicked.connect(self._agregar_producto_tabla)
        self.spin_paga_con.valueChanged.connect(self._calcular_cambio)
        self.btn_cancelar_ticket.clicked.connect(self._limpiar_formulario)
        self.btn_guardar_imprimir_ticket.clicked.connect(self._guardar_ticket)

        #cargar datos iniciales de BD
        self._cargar_siguiente_folio()
        self._cargar_pacientes()
        self._cargar_medicamentos()

    def _cargar_siguiente_folio(self):
        """Consulta el último ID de ticket registrado y asigna el siguiente."""
        query = "SELECT IFNULL(MAX(id_ticket), 0) + 1 AS siguiente_folio FROM ticket"
        try:
            with self.db.obtener_cursor() as cursor:
                cursor.execute(query)
                res = cursor.fetchone()
                siguiente = res['siguiente_folio'] if res else 1
                self.lbl_num_ticket.setText(str(siguiente))
        except Exception as e:
            self.lbl_num_ticket.setText("1")

    def _cargar_pacientes(self):
        """Carga los pacientes en el ComboBox."""
        self.cmb_paciente_ticket.clear()
        self.cmb_paciente_ticket.addItem("Seleccionar paciente...", None)
        query = "SELECT id_paciente, CONCAT(nombre, ' ', primer_apellido) AS nombre_completo FROM paciente ORDER BY nombre_completo"
        try:
            with self.db.obtener_cursor() as cursor:
                cursor.execute(query)
                pacientes = cursor.fetchall()
                for p in pacientes:
                    self.cmb_paciente_ticket.addItem(p['nombre_completo'], p['id_paciente'])
        except Exception as e:
            print(f"Error al cargar pacientes: {e}")

    def _cargar_medicamentos(self):
        """Carga la lista de medicamentos y sus precios desde BD."""
        self.cmb_buscar_medicamento.clear()
        self.cmb_buscar_medicamento.addItem("Seleccionar medicamento...", None)
        self.medicamentos_db = {}

        query = "SELECT id_medicamento, nombre_medicamento, precio FROM medicamento ORDER BY nombre_medicamento"
        try:
            with self.db.obtener_cursor() as cursor:
                cursor.execute(query)
                meds = cursor.fetchall()
                for m in meds:
                    id_med = m['id_medicamento']
                    precio = float(m['precio']) if m['precio'] else 0.0
                    self.medicamentos_db[id_med] = {'nombre': m['nombre_medicamento'], 'precio': precio}
                    self.cmb_buscar_medicamento.addItem(m['nombre_medicamento'], id_med)
        except Exception as e:
            print(f"Error al cargar medicamentos: {e}")

    def _actualizar_precio_medicamento(self):
        """Coloca el precio unitario en el spinbox según el medicamento seleccionado."""
        id_med = self.cmb_buscar_medicamento.currentData()
        if id_med in self.medicamentos_db:
            precio = self.medicamentos_db[id_med]['precio']
            self.spin_precio_unitario.setValue(precio)
        else:
            self.spin_precio_unitario.setValue(0.0)

    def _agregar_producto_tabla(self):
        """Agrega el medicamento seleccionado a la QTableWidget."""
        id_med = self.cmb_buscar_medicamento.currentData()
        if not id_med:
            QMessageBox.warning(self, "Atención", "Por favor selecciona un medicamento.")
            return

        cantidad = self.spin_piezas.value()
        precio = self.spin_precio_unitario.value()

        if cantidad <= 0 or precio <= 0:
            QMessageBox.warning(self, "Atención", "La cantidad y el precio deben ser mayores a 0.")
            return

        subtotal_item = cantidad * precio
        nombre_med = self.medicamentos_db[id_med]['nombre']

        # Insertar fila en la tabla
        row = self.tbl_ticket_detalle.rowCount()
        self.tbl_ticket_detalle.insertRow(row)

        self.tbl_ticket_detalle.setItem(row, 0, QTableWidgetItem(str(id_med)))
        self.tbl_ticket_detalle.setItem(row, 1, QTableWidgetItem(nombre_med))
        self.tbl_ticket_detalle.setItem(row, 2, QTableWidgetItem(str(cantidad)))
        self.tbl_ticket_detalle.setItem(row, 3, QTableWidgetItem(f"${precio:,.2f}"))
        self.tbl_ticket_detalle.setItem(row, 4, QTableWidgetItem(f"${subtotal_item:,.2f}"))

        # Recalcular totales generales
        self._recalcular_totales()

        # Resetear controles de medicamento
        self.cmb_buscar_medicamento.setCurrentIndex(0)
        self.spin_piezas.setValue(1)
        self.spin_precio_unitario.setValue(0.0)

    def _recalcular_totales(self):
        """Suma los subtotales de la tabla y actualiza Subtotal y Total."""
        total = 0.0
        for r in range(self.tbl_ticket_detalle.rowCount()):
            # Obtenemos la columna 4 (Subtotal MXN) y le quitamos el símbolo $
            val_str = self.tbl_ticket_detalle.item(r, 4).text().replace('$', '').replace(',', '')
            total += float(val_str)

        self.txt_subtotal.setText(f"${total:,.2f}")
        self.txt_total.setText(f"${total:,.2f}")
        self._calcular_cambio()

    def _calcular_cambio(self):
        """Calcula el cambio restando Paga Con - Total."""
        try:
            str_total = self.txt_total.text().replace('$', '').replace(',', '')
            total = float(str_total) if str_total else 0.0
            paga_con = self.spin_paga_con.value()

            cambio = paga_con - total
            if cambio >= 0 and total > 0:
                self.txt_cambio.setText(f"${cambio:,.2f}")
            else:
                self.txt_cambio.setText("$0.00")
        except Exception:
            self.txt_cambio.setText("$0.00")

    def _limpiar_formulario(self):
        """Limpia la tabla y reinicia los campos."""
        self.cmb_paciente_ticket.setCurrentIndex(0)
        self.date_ticket.setDate(QDate.currentDate())
        self.cmb_buscar_medicamento.setCurrentIndex(0)
        self.spin_piezas.setValue(1)
        self.spin_precio_unitario.setValue(0.0)
        self.tbl_ticket_detalle.setRowCount(0)
        self.txt_subtotal.setText("$0.00")
        self.txt_total.setText("$0.00")
        self.spin_paga_con.setValue(0.0)
        self.txt_cambio.setText("$0.00")
        self._cargar_siguiente_folio()

    def _guardar_ticket(self):
        """Almacena el ticket y sus detalles en las tablas `ticket` y `ticket_medicamento`."""
        id_paciente = self.cmb_paciente_ticket.currentData()
        if not id_paciente:
            QMessageBox.warning(self, "Atención", "Selecciona un paciente antes de guardar.")
            return

        if self.tbl_ticket_detalle.rowCount() == 0:
            QMessageBox.warning(self, "Atención", "Agrega al menos un medicamento a la tabla.")
            return

        str_total = self.txt_total.text().replace('$', '').replace(',', '')
        total = float(str_total)
        paga_con = self.spin_paga_con.value()

        if paga_con < total:
            QMessageBox.warning(self, "Atención", "El monto ingresado en 'Paga con' es menor al Total.")
            return

        fecha_str = self.date_ticket.date().toString("yyyy-MM-dd")

        try:
            # 1. Insertar el ticket cabecera
            q_ticket = """
                INSERT INTO ticket (id_paciente, ticket_date) 
                VALUES (%s, %s)
            """
            with self.db.obtener_cursor() as cursor:
                cursor.execute(q_ticket, (id_paciente, fecha_str))
                id_ticket_creado = cursor.lastrowid

                # 2. Insertar los medicamentos del ticket
                q_detalle = """
                    INSERT INTO ticket_medicamento (id_ticket, id_medicamento, cant_medicamento, medicina_costo_unidad)
                    VALUES (%s, %s, %s, %s)
                """
                for r in range(self.tbl_ticket_detalle.rowCount()):
                    id_med = int(self.tbl_ticket_detalle.item(r, 0).text())
                    cant = int(self.tbl_ticket_detalle.item(r, 2).text())
                    precio_str = self.tbl_ticket_detalle.item(r, 3).text().replace('$', '').replace(',', '')
                    precio = float(precio_str)

                    cursor.execute(q_detalle, (id_ticket_creado, id_med, cant, precio))

            QMessageBox.information(self, "Éxito", f"¡Ticket #{id_ticket_creado} registrado correctamente!")
            self._limpiar_formulario()

        except Exception as e:
            QMessageBox.critical(self, "Error BD", f"No se pudo guardar el ticket:\n{e}")