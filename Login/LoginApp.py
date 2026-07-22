from PyQt6.uic.uiparser import QtWidgets
from message_box import Message_Box
from BaseDatos.MySqlManager import MySqlManager
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget
from PyQt6 import uic

class Login_App(QWidget):
    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.mb = Message_Box()
        self.navegar = navegar
        self.db = db
        uic.loadUi("Documentacion/QtDesigner/login.ui", self)
        self.pb_ingresar.clicked.connect(lambda: self.bt_ingresar_logica(self.le_usuario.text(),self.le_contrasena.text()))
        self.clb_crear_conultorio.clicked.connect(lambda: self.clb_crear_cuenta_usuario())


    def bt_ingresar_logica(self, le_usuario, le_password):
        usuario = le_usuario.strip()
        password =  le_password.strip()
        if not usuario or not password:
            self.mb.message_box("error", "Error", "Datos faltantes")

        elif usuario == "Asgard" and password == "1234":
            self.navegar.ir_a_ventana("menu_principal")
        else:
            self.mb.message_box("info", "Error", "Usuario no encontrado")

    def clb_crear_cuenta_usuario(self):
        self.navegar.ir_a_ventana("crear_consultorio")

