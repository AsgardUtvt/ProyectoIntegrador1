from PyQt6.uic.uiparser import QtWidgets
from BaseDatos.MySqlManager import MySqlManager
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget
from PyQt6 import uic
import os

class Ventana_Menu_Principal(QWidget):

    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.navegar = navegar
        self.db = db
        uic.loadUi("Documentacion/QtDesigner/menu_con_lista.ui", self)

        self.rutas_interfaces = {
            "menu_principal": "../Documentacion/QtDesigner/menu_con_lista.ui",
            "menu_pacientes": "../"
            "recetas": "../Recetas/Recetas.ui"
        }
        self.mapeo_menu = {
            0: "menu",
            1: "pacientes",
            2: "recetas",
            3: "inventario",
            4: "ventas",
            5: "usuario",
            6: "reportes",
            7: "configuración"
        }

        self.venta_indice = {}
        self.cargar_ventanas()
        self.listWideget.currentRowChanged.connect (self.cambiar_pestana)
        self.listWideget.setCurrentRow(0)

    def cargar_ventanas(self):

        dir_actual = os.path.dirname(os.path.abspath(__file__))
        for indice, (nombre, ruta_ui) in enumerate(self.rutas_interfaces.items()):
            sub_widet = QWidget()
            ruta_absoluta_ui = os.path.normpath(os.path.join(dir_actual, ruta_ui))
            if not os.path.exists(ruta_absoluta_ui):
                print(f"Error: no se encontro el archivo UI en {ruta_absoluta_ui}")
                continue
            uic.loadUi(ruta_absoluta_ui, sub_widet)
            self.stackedWidget.addWidget(sub_widet)
            self.venta_indice[nombre] = indice

    def cambiar_pestana(self, fila):

        if fila in self.mapeo_menu:
            nombre_ventana = self.mapeo_menu[fila]
            self.ir_a_sub_ventana(nombre_ventana)

    def ir_a_sub_ventana(self, nombre_ventana):

        if nombre_ventana in self.venta_indice:
            indice = self.venta_indice[nombre_ventana]
            self.stackedWidget.setCurrentIndex(indice)
            widget_actual = self.stackedWidget.widget(indice)
            titulo = widget_actual.windowTitle() if widget_actual.windowTitle() else "SIHMED"
            self.window().setWindowTitle(titulo)

