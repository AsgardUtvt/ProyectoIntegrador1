from PyQt6.uic.uiparser import QtWidgets

from BaseDatos.MySqlManager import MySqlManager
from Documentacion.QtDesigner.usuario_crear_ui import Ui_d_crear_usuario
from Documentacion.QtDesigner.menu_principal_ui import  Ui_d_menu_principal
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget
from PyQt6 import uic

class Ventana_Crear_Usuario(QWidget):

    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.navegar = navegar
        self.db = db
        uic.loadUi("Documentacion/QtDesigner/usuario_crear.ui", self)
