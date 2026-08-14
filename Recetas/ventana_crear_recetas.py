import os
from PyQt6.QtWidgets import QWidget, QTableWidgetItem
from PyQt6 import uic
from BaseDatos.MySqlManager import MySqlManager
<<<<<<< Updated upstream
=======
#from BaseDatos.MySqlManager import MySqlManager
>>>>>>> Stashed changes
from message_box import Message_Box

class Ventana_Crear_Recetas(QWidget):
    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.db = db
        self.navegar = navegar
        self.mb = Message_Box()
<<<<<<< Updated upstream
        #cargar ui
        uic.loadUi("Documentacion/QtDesigner/Recetas.ui", self)
=======

        #cargar ui
        dir_actual = os.path.dirname(__file__)
        ruta_ui = os.path.join(dir_actual, "Recetas.ui")
        uic.loadUi(ruta_ui, self)

>>>>>>> Stashed changes
        #botones con funciones
        self.pb_agregar_medicamento.clicked.connect(self.btn_agregar_medicamento)
        self.pb_imprimir_receta.clicked.connect(self.btn_guardar_receta)

        #funciones del boton
    def btn_agregar_medicamento(self):
        medicamento = self.cb_medicamento.currentText().strip()
        indicaciones = self.le_indicaciones.text().strip()

        if not medicamento or not indicaciones:
            self.mb.message_box(self, "info", "Faltan datos", "Debes ingresar un medicamento e indicaciones.")
            return

        #insertar fila en la tabla
        row_position = self.tw_medicamentos.rowCount()
        self.tw_medicamentos.insertRow(row_position)

        self.tw_medicamentos.setItem(row_position, 0, QTableWidgetItem(medicamento))
        self.tw_medicamentos.setItem(row_position, 1, QTableWidgetItem(indicaciones))
        self.tw_medicamentos.setItem(row_position, 2, QTableWidgetItem("1")) #1 es cantidad por defecto

        #limpiar campo de indicaciones para el siguiente medicamento
        self.le_indicaciones.clear()

    def btn_guardar_receta(self):
        datos_faltantes = []

        paciente = self.cb_paciente.currentText().strip()
        if not paciente:
            datos_faltantes.append("Paciente")

        diagnostico = self.te_diagnostico.toPlainText().strip()
        if not diagnostico:
            datos_faltantes.append("Diagnóstico")

        if self.tw_medicamentos.rowCount() == 0:
            datos_faltantes.append("Al menos un medicamento en la tabla")

        #mensaje de faltantes
        if len(datos_faltantes) > 0:
            mensaje = "Por favor completa: " + ", ".join(datos_faltantes)
            self.mb.message_box(self, "info", "Faltan datos", mensaje)
        else:
            try:
                #guardar en la base de datos
                self.mb.message_box(self, "info", "Éxito", "La receta se ha generado correctamente.")
            except Exception as e:
                print(f"Error crítico: {e}")
                self.mb.message_box(self, "error", "Error", "No se pudo guardar la receta.")
