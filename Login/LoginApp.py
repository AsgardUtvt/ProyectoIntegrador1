from PyQt6.uic.uiparser import QtWidgets

from BaseDatos.MySqlManager import MySqlManager
from Documentacion.QtDesigner.login_ui import Ui_MainWindow
from Documentacion.QtDesigner.menu_principal_ui import  Ui_d_menu_principal
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget
from PyQt6 import uic

class Login_App(QWidget):

    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.navegar = navegar
        self.db = db
        uic.loadUi("Documentacion/QtDesigner/login.ui", self)
        self.pb_ingresar.clicked.connect(lambda: self.bt_ingresar_logica(self.le_usuario.text(),self.le_contrasena.text()))


    def bt_ingresar_logica(self, le_usuario, le_password):
        usuario = le_usuario.strip()
        password =  le_password.strip()
        if not usuario or not password:
            QMessageBox.critical(self, "Error", "Faltan datos por llenar")
        elif usuario == "Asgard" and password == "1234":
            self.navegar.ir_a_ventana("menu_principal")
        else:
            QMessageBox.information(self, "Erorr", "Usuario no encontrado")

#    def lbt_crear_cuenta_usuario(self)
