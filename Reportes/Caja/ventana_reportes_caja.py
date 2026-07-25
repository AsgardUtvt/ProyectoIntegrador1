import os
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtCore import QDate
from PyQt6.QtPrintSupport import QPrinter
from PyQt6.QtGui import QTextDocument
from PyQt6.QtWidgets import QWidget, QTableWidgetItem, QDateEdit
from PyQt6 import uic
from BaseDatos.MySqlManager import MySqlManager
from message_box import Message_Box

class Ventana_Reportes_Caja(QWidget):
    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.db = db
        self.navegar = navegar
        self.mb = Message_Box()
        
        #cargar .ui
        dir_actual = os.path.dirname(__file__)
        ruta_ui = os.path.join(dir_actual, "reportes_caja.ui")
        uic.loadUi(ruta_ui, self)
        
        #iniciar fechas en hoy
        self.de_fecha_inicio.setDate(QDate.currentDate())
        self.de_fecha_fin.setDate(QDate.currentDate())
        
        #solo lectura en el resumen
        self.le_total_ingresos.setReadOnly(True)
        self.le_total_egresos.setReadOnly(True)
        self.le_saldo_final.setReadOnly(True)
        
        #botones con funciones
        self.pb_generar_reporte.clicked.connect(self.btn_generar_reporte)
        self.pb_exportar_pdf.clicked.connect(self.btn_exportar_pdf)
        
    def btn_generar_reporte(self):
        fecha_inicio = self.de_fecha_inicio.date().toString("yyyy-MM-dd")
        fecha_fin = self.de_fecha_fin.date().toString("yyyy-MM-dd")
        tipo_reporte = self.cb_tipo_reporte.currentText()
        

        # Validación simple de rango de fechas
        if self.de_fecha_inicio.date() > self.de_fecha_fin.date():
            self.mb.message_box(self, "info", "Rango inválido", "La fecha de inicio no puede ser posterior a la fecha fin.")
            return

        if not self.db:
            self.mb.message_box(self, "error", "Sin Conexión", "No hay conexión activa con la base de datos.")
            return

        try:
            # 1. Limpiar la tabla de la interfaz
            self.tw_movimientos.setRowCount(0)

            # 2. Abrir conexión
            self.db.open_db()

            # 3. Consulta SQL (Pedimos la fecha directa sin DATE_FORMAT de MySQL)
            query_movimientos = """
                SELECT 
                    t.ticket_date AS fecha,
                    CONCAT('Ticket #', t.id_ticket) AS concepto,
                    'Ingreso' AS tipo,
                    IFNULL((
                        SELECT SUM(tm.medicina_costo_unidad * tm.cant_medicamento) 
                        FROM ticket_medicamento tm 
                        WHERE tm.id_ticket = t.id_ticket
                    ), 0) AS monto
                FROM ticket t
                WHERE DATE(t.ticket_date) BETWEEN %s AND %s
                ORDER BY t.ticket_date DESC
            """

            # 4. Ejecutar consulta
            with self.db.obtener_cursor() as cursor:
                cursor.execute(query_movimientos, (fecha_inicio, fecha_fin))
                movimientos = cursor.fetchall()

            total_ingresos = 0.0
            total_egresos = 0.0

            # 5. Insertar filas en la QTableWidget
            if movimientos:
                for row_idx, fila in enumerate(movimientos):
                    self.tw_movimientos.insertRow(row_idx)
                    monto_fila = float(fila['monto']) if fila['monto'] else 0.0
                    total_ingresos += monto_fila

                    # Formateamos la fecha directamente desde Python
                    fecha_str = fila['fecha'].strftime("%Y-%m-%d %H:%M") if fila['fecha'] else ""

                    self.tw_movimientos.setItem(row_idx, 0, QTableWidgetItem(fecha_str))
                    self.tw_movimientos.setItem(row_idx, 1, QTableWidgetItem(str(fila['concepto'])))
                    self.tw_movimientos.setItem(row_idx, 2, QTableWidgetItem(str(fila['tipo'])))
                    self.tw_movimientos.setItem(row_idx, 3, QTableWidgetItem(f"${monto_fila:,.2f}"))

            saldo_final = total_ingresos - total_egresos

            self.le_total_ingresos.setText(f"${total_ingresos:,.2f}")
            self.le_total_egresos.setText(f"${total_egresos:,.2f}")
            self.le_saldo_final.setText(f"${saldo_final:,.2f}")

            if not movimientos:
                self.mb.message_box(self, "info", "Sin movimientos", "No hay tickets registrados en las fechas seleccionadas.")

        except Exception as e:
            print(f"Error detallado de BD: {e}")
            self.mb.message_box(self, "error", "Error BD", f"Detalle: {e}")

    def btn_exportar_pdf(self):
        if self.tw_movimientos.rowCount() == 0 and not self.le_saldo_final.text():
            self.mb.message_box(self, "info", "Sin datos", "Primero debes generar un reporte antes de exportarlo.")
            return

        # 1. Abrir ventana para que el usuario elija dónde guardar el archivo
        ruta_guardar, _ = QFileDialog.getSaveFileName(
            self, 
            "Guardar Reporte de Caja", 
            "Reporte_Caja.pdf", 
            "Archivos PDF (*.pdf)"
        )

        # Si el usuario cancela la ventana de guardado
        if not ruta_guardar:
            return

        try:
            # 2. Construir el contenido en HTML para que se vea ordenado y bonito
            html_content = f"""
            <h1 style="text-align: center;">Reporte de Caja - SIHMED</h1>
            <hr>
            <h3>Resumen Financiero</h3>
            <ul>
                <li><b>Total Ingresos:</b> {self.le_total_ingresos.text()}</li>
                <li><b>Total Egresos:</b> {self.le_total_egresos.text()}</li>
                <li><b>Saldo Final:</b> {self.le_saldo_final.text()}</li>
            </ul>
            <br>
            <h3>Detalle de Movimientos</h3>
            <table border="1" cellspacing="0" cellpadding="5" width="100%">
                <thead>
                    <tr bgcolor="#f2f2f2">
                        <th>Fecha</th>
                        <th>Concepto</th>
                        <th>Tipo</th>
                        <th>Monto</th>
                    </tr>
                </thead>
                <tbody>
            """

            # Recorrer la tabla de la interfaz para agregar las filas al PDF
            for row in range(self.tw_movimientos.rowCount()):
                fecha = self.tw_movimientos.item(row, 0).text() if self.tw_movimientos.item(row, 0) else ""
                concepto = self.tw_movimientos.item(row, 1).text() if self.tw_movimientos.item(row, 1) else ""
                tipo = self.tw_movimientos.item(row, 2).text() if self.tw_movimientos.item(row, 2) else ""
                monto = self.tw_movimientos.item(row, 3).text() if self.tw_movimientos.item(row, 3) else ""

                html_content += f"""
                <tr>
                    <td>{fecha}</td>
                    <td>{concepto}</td>
                    <td>{tipo}</td>
                    <td>{monto}</td>
                </tr>
                """

            html_content += """
                </tbody>
            </table>
            """

            # 3. Renderizar el HTML y exportarlo como PDF utilizando QPrinter
            documento = QTextDocument()
            documento.setHtml(html_content)

            printer = QPrinter(QPrinter.PrinterMode.HighResolution)
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(ruta_guardar)

            documento.print(printer)

            self.mb.message_box(self, "info", "Exportación", "El reporte se ha exportado a PDF correctamente.")

        except Exception as e:
            print(f"Error al exportar PDF: {e}")
            self.mb.message_box(self, "error", "Error", "No se pudo generar el archivo PDF.")