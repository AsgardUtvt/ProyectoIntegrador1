import sys
import os
from PyQt6.QtWidgets import QWidget, QTableWidgetItem
from PyQt6 import uic
from PyQt6.QtCore import QDate
from BaseDatos.MySqlManager import MySqlManager
from message_box import Message_Box  # Importamos el servicio del tío Asgard

class CitasWindow(QWidget):
    def __init__(self, db: MySqlManager, navegar): 
        super().__init__()
        self.db = db
        self.navegar = navegar
        self.mb = Message_Box() # Servicio de mensajes juntaditos pa que , ni yo se pero en los tutos asi le hacian
        uic.loadUi("../Documentacion/QtDesigner/citasWidget.ui",self)
        self.configurar_tabla()
        self.calendar.setSelectedDate(QDate.currentDate())

        #  botones pa la ui
        self.btnAct.clicked.connect(self.cargar_citas)
        self.btnGen.clicked.connect(self.generar_cita)
        self.btnMod.clicked.connect(self.modificar_cita)
        self.btnEli.clicked.connect(self.eliminar_cita)
        self.btnVolver.clicked.connect(lambda: self.navegar.ir_a_ventana("menu_principal")) # Estilo de navegación Asgard

        self.calendar.selectionChanged.connect(self.cargar_citas)
        self.tableCitas.itemSelectionChanged.connect(self.mostrar_detalle_cita)

        self.cargar_citas()


    def configurar_tabla(self):
        tabla = self.tableCitas
        tabla.setColumnCount(5)
        tabla.setHorizontalHeaderLabels(["ID Cita", "Fecha y Hora", "Paciente", "Consultorio", "Estado"])
        tabla.verticalHeader().setVisible(False)
        tabla.setSelectionBehavior(tabla.SelectionBehavior.SelectRows)
        tabla.setEditTriggers(tabla.EditTrigger.NoEditTriggers)

    def cargar_citas(self):
        fecha = self.calendar.selectedDate().toString("yyyy-MM-dd")
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
            """
            datos = self.db.fetchall(query, (fecha,))
            self.actualizar_tabla_visual(datos if datos else [])
        except Exception as e:
            self.mb.message_box(self, "error", "Error de Base de Datos", str(e))

    def actualizar_tabla_visual(self, datos):
        tabla = self.tableCitas
        tabla.setRowCount(len(datos))
        for fila, cita in enumerate(datos):
            tabla.setItem(fila, 0, QTableWidgetItem(str(cita.get("id_cita"))))
            tabla.setItem(fila, 1, QTableWidgetItem(str(cita.get("cita_date"))))
            tabla.setItem(fila, 2, QTableWidgetItem(str(cita.get("paciente_completo"))))
            tabla.setItem(fila, 3, QTableWidgetItem(str(cita.get("consultorio_name"))))
            tabla.setItem(fila, 4, QTableWidgetItem(str(cita.get("estado_cita"))))

    def mostrar_detalle_cita(self):
        tabla = self.tableCitas
        seleccion = tabla.selectedItems()
        if not seleccion: return
        
        id_cita = tabla.item(seleccion[0].row(), 0).text()
        try:
            query = "SELECT c.*, CONCAT(p.paciente_name, ' ', p.paciente_paterno) as paciente FROM Cita c JOIN Paciente p ON c.id_paciente = p.id_paciente WHERE c.id_cita = %s"
            res = self.db.fetchone(query, (id_cita,))
            if res:
                self.lblDet.setText(f"Paciente: {res.get('paciente')}\nNota: {res.get('cita_nota')}")
        except Exception as e:
            self.mb.message_box(self, "error", "Error", "No se pudo obtener detalle")

    def eliminar_cita(self):
        # Estilo Asgard de confirmación asi bien perron :v
        if not self.tableCitas.selectedItems():
            self.mb.message_box(self, "info", "Advertencia", "Seleccione una cita")
            return
        
        id_cita = self.tableCitas.item(self.tableCitas.selectedItems()[0].row(), 0).text()
        if self.mb.message_box(self, "question", "Confirmar", "¿Eliminar cita?"): # Asumiendo implementación en Message_Box
            self.db.execute("DELETE FROM Cita WHERE id_cita = %s", (id_cita,))
            self.cargar_citas()