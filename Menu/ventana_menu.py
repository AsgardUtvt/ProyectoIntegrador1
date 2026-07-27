from PyQt6.uic.uiparser import QtWidgets
from BaseDatos.MySqlManager import MySqlManager
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget, QVBoxLayout, QSizePolicy
from PyQt6 import uic
import os

class Ventana_Menu_Principal(QWidget):

    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.navegar = navegar
        self.db = db
        uic.loadUi("Documentacion/QtDesigner/menu_con_lista.ui", self)

        self.rutas_interfaces = {
            "menu_principal": "../Documentacion/QtDesigner/menu_principal.ui",
            "menu_pacientes": "../Pacientes/pacientes.ui",
            "recetas": "../Recetas/Recetas.ui",
            "inventario": "../Documentacion/QtDesigner/menu_principal.ui",
            "ventas": "../Reportes/Ticket/ticket_pago.ui",
            "usuario": "../Documentacion/QtDesigner/usuario_modificar.ui",
            "reportes": "../Reportes/Caja/reportes_caja.ui",
            "configuracion": "../Documentacion/QtDesigner/menu_principal.ui"
        }
        opciones_menu = ["Inicio", "Pacientes", "Recetas", "Inventario", "Ventas", "Usuario", "Reportes", "Configuración"]
        self.lw_enlace_menu.clear()
        self.lw_enlace_menu.addItems(opciones_menu)
        self.mapeo_menu = {
            0: "menu_principal",
            1: "menu_pacientes",
            2: "recetas",
            3: "inventario",
            4: "ventas",
            5: "usuario",
            6: "reportes",
            7: "configuracion"
        }

        self.layout_vistas = QVBoxLayout(self.w_ventana)
        self.layout_vistas.setContentsMargins(0,0,0,0)

        self.lw_enlace_menu.currentRowChanged.connect(lambda: self.cargar_ventanas)

        self.sub_ventana_actual = None

        self.lw_enlace_menu.setCurrentRow(0)

    def cargar_ventanas(self, fila):

        if fila in self.mapeo_menu[fila]:
            nombre_ventana = self.mapeo_menu[fila]
            ruta_relativa = self.rutas_interfaces[nombre_ventana]

            dir_actual = os.path.dirname(os.path.abspath(__file__))
            ruta_absoluta = os.path.normpath(os.path.join(dir_actual, ruta_relativa))

            if os.path.exists(ruta_absoluta):
                self.mostrar_nueva_interfaz(ruta_absoluta)
            else:
                print(f"Error: no se encontro el archivo .ui en {ruta_absoluta}")

    def mostrar_nueva_interfaz(self, ruta_ui):

        if self.sub_ventana_actual is not None:
            self.layout_vistas.removeWidget(self.sub_ventana_actual)
            self.sub_ventana_actual.deleteLater()

        self.sub_ventana_actual = QWidget(self)
        uic.loadUi(ruta_ui, self.sub_ventana_actual)
        self.sub_ventana_actual.selSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.layout_vistas.addWidget(self.sub_ventana_actual)
        self.sub_ventana_actual.show()

        titulo = self.sub_ventana_actual.windowTitle()
        self.window().setWindowTitle(titulo if titulo else "SIHMED")

