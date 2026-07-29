import sys
import os
import pymysql

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox,
    QTableWidgetItem,
    QFileDialog
)

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
from PySide6.QtGui import QColor

from openpyxl import Workbook

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle
)

from reportlab.lib import colors


class Reportes(QMainWindow):

    def __init__(self):
        super().__init__()

      
        archivo = QFile("reportes.ui")
        
        if not archivo.open(QFile.ReadOnly):
            QMessageBox.critical(
                None, 
                "Error crítico", 
                f"No se pudo abrir el archivo 'reportes.ui'.\nVerifica que esté en la carpeta: {os.getcwd()}"
            )
            sys.exit(1)

        self.ui = QUiLoader().load(archivo)
        archivo.close()

        if self.ui is None:
            QMessageBox.critical(None, "Error crítico", "El archivo 'reportes.ui' está vacío o corrupto.")
            sys.exit(1)

        self.ui.show()

        # -------------------------
        # Base de datos
        # -------------------------
        self.conexion = pymysql.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="sihmed",
            cursorclass=pymysql.cursors.DictCursor
        )

        self.cursor = self.conexion.cursor()

        # -------------------------
        # Configurar tabla
        # -------------------------
        self.configurarTabla()

        # -------------------------
        # Eventos
        # -------------------------
        self.ui.btnGenerar.clicked.connect(
            self.cargarInventario
        )

        self.ui.btnLimpiar.clicked.connect(
            self.limpiarTabla
        )

        self.ui.btnExcel.clicked.connect(
            self.exportarExcel
        )

        self.ui.btnPDF.clicked.connect(
            self.exportarPDF
        )

        # Configurar búsqueda en tiempo real si el campo existe
        if hasattr(self.ui, "txtBuscar"):
            self.ui.txtBuscar.textChanged.connect(
                self.buscarMedicamento
            )

        # Cargar datos automáticamente al iniciar
        self.cargarInventario()


    def configurarTabla(self):

        tabla = self.ui.tablaReporte

        tabla.setColumnCount(7)

        tabla.setHorizontalHeaderLabels([
            "ID",
            "Medicamento",
            "Cantidad",
            "Stock mínimo",
            "Caducidad",
            "Dosis",
            "Costo"
        ])

        tabla.verticalHeader().setVisible(False)
        tabla.setAlternatingRowColors(True)
        tabla.horizontalHeader().setStretchLastSection(True)

        tabla.setSelectionBehavior(
            tabla.SelectionBehavior.SelectRows
        )

        tabla.setEditTriggers(
            tabla.EditTrigger.NoEditTriggers
        )


    def cargarInventario(self):

        try:
            consulta = """
                SELECT
                    id_medicamento,
                    medicamento_name,
                    medicamento_cantidad,
                    medicamento_min,
                    medicamento_caducidad,
                    medicamento_dosis,
                    medicamento_costo
                FROM Medicamento
                ORDER BY medicamento_name
            """

            self.cursor.execute(consulta)
            datos = self.cursor.fetchall()

            self.actualizarTabla(datos)

        except Exception as error:
            QMessageBox.critical(
                self.ui,
                "Error",
                str(error)
            )


    def buscarMedicamento(self):

        try:
            texto = self.ui.txtBuscar.text().strip()

            consulta = """
                SELECT
                    id_medicamento,
                    medicamento_name,
                    medicamento_cantidad,
                    medicamento_min,
                    medicamento_caducidad,
                    medicamento_dosis,
                    medicamento_costo
                FROM Medicamento
                WHERE medicamento_name LIKE %s
                ORDER BY medicamento_name
            """

            self.cursor.execute(
                consulta,
                ("%" + texto + "%",)
            )

            datos = self.cursor.fetchall()
            self.actualizarTabla(datos)

        except Exception as error:
            QMessageBox.critical(
                self.ui,
                "Error",
                str(error)
            )


    def actualizarTabla(self, datos):

        tabla = self.ui.tablaReporte
        tabla.setRowCount(len(datos))

        for fila, medicamento in enumerate(datos):

            tabla.setItem(
                fila, 0,
                QTableWidgetItem(str(medicamento["id_medicamento"]))
            )

            tabla.setItem(
                fila, 1,
                QTableWidgetItem(medicamento["medicamento_name"])
            )

            tabla.setItem(
                fila, 2,
                QTableWidgetItem(str(medicamento["medicamento_cantidad"]))
            )

            tabla.setItem(
                fila, 3,
                QTableWidgetItem(str(medicamento["medicamento_min"]))
            )

            tabla.setItem(
                fila, 4,
                QTableWidgetItem(str(medicamento["medicamento_caducidad"]))
            )

            tabla.setItem(
                fila, 5,
                QTableWidgetItem(medicamento["medicamento_dosis"])
            )

            tabla.setItem(
                fila, 6,
                QTableWidgetItem(str(medicamento["medicamento_costo"]))
            )

            # ---------------------------------
            # Alerta de bajo stock
            # ---------------------------------
            if medicamento["medicamento_cantidad"] <= medicamento["medicamento_min"]:
                for columna in range(7):
                    item = tabla.item(fila, columna)
                    if item:
                        item.setBackground(QColor(255, 210, 210))
                        item.setForeground(QColor(170, 0, 0))

        self.ui.lblTotal.setText(
            f"Total de medicamentos: {len(datos)}"
        )


    def limpiarTabla(self):

        self.ui.tablaReporte.setRowCount(0)

        self.ui.lblTotal.setText(
            "Total de medicamentos: 0"
        )


    def exportarExcel(self):

        archivo, _ = QFileDialog.getSaveFileName(
            self.ui,
            "Guardar reporte",
            "",
            "Excel (*.xlsx)"
        )

        if not archivo:
            return

        libro = Workbook()
        hoja = libro.active
        hoja.title = "Inventario"

        for columna in range(self.ui.tablaReporte.columnCount()):
            hoja.cell(
                row=1,
                column=columna + 1
            ).value = self.ui.tablaReporte.horizontalHeaderItem(columna).text()

        for fila in range(self.ui.tablaReporte.rowCount()):
            for columna in range(self.ui.tablaReporte.columnCount()):
                item = self.ui.tablaReporte.item(fila, columna)
                if item:
                    hoja.cell(
                        row=fila + 2,
                        column=columna + 1
                    ).value = item.text()

        libro.save(archivo)

        QMessageBox.information(
            self.ui,
            "Éxito",
            "Reporte exportado correctamente."
        )


    def exportarPDF(self):

        archivo, _ = QFileDialog.getSaveFileName(
            self.ui,
            "Guardar PDF",
            "",
            "PDF (*.pdf)"
        )

        if not archivo:
            return

        datos = []
        encabezados = []

        for c in range(self.ui.tablaReporte.columnCount()):
            encabezados.append(
                self.ui.tablaReporte.horizontalHeaderItem(c).text()
            )

        datos.append(encabezados)

        for fila in range(self.ui.tablaReporte.rowCount()):
            registro = []
            for columna in range(self.ui.tablaReporte.columnCount()):
                item = self.ui.tablaReporte.item(fila, columna)
                if item:
                    registro.append(item.text())
                else:
                    registro.append("")
            datos.append(registro)

        pdf = SimpleDocTemplate(archivo)
        tabla = Table(datos)

        tabla.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1565C0")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10)
        ]))

        pdf.build([tabla])

        QMessageBox.information(
            self.ui,
            "Éxito",
            "PDF generado correctamente."
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Reportes()
    sys.exit(app.exec())