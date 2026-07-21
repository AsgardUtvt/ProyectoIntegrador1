from BaseDatos.MySqlManager import MySqlManager
from Documentacion.QtDesigner.login_ui import Ui_MainWindow
from Documentacion.QtDesigner.menu_principal_ui import  Ui_d_menu_principal
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox

class Login_App():

    def __init__(self, db: MySqlManager):
        self.main_window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        self.main_venta_base = QMainWindow()
        self.venta_menu = Ui_d_menu_principal()
        self.venta_menu.setupUi(self.main_venta_base)
        self.ui.pb_ingresar.clicked.connect(lambda: self.bt_ingresar_logica(self.ui.le_usuario.text(),self.ui.le_contrasena.text()))


    def bt_ingresar_logica(self, le_usuario, le_password):
        usuario = le_usuario.strip()
        password =  le_password.strip()
        if not usuario or not password:
            QMessageBox.information(self.main_window, "Error", "Faltan datos por llenar")
        elif usuario == "Asgard" and password == "1234":
            self.main_venta_base.show()
            self.main_window.close()
        else:
            QMessageBox.information(self.main_window, "Error", "Usuairo no encontrado")

