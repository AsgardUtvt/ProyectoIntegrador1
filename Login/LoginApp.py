from PyQt6.uic.uiparser import QtWidgets
from message_box import Message_Box
from BaseDatos.MySqlManager import MySqlManager
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget, QLineEdit
<<<<<<< HEAD
from PyQt6.QtCore import QTimer
from PyQt6 import uic
from Login.Functions.Encrypt import Encrypt
from Login.Servicio.general_login_service import General_Login_Service as GLS
import threading

=======
from PyQt6 import uic
>>>>>>> c2983caab5b8c6a3f8beff40b13f4603256eb540

class Login_App(QWidget):
    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.mb = Message_Box()
        self.navegar = navegar
        self.db = db
<<<<<<< HEAD
        self.en = Encrypt()
        self.intento = 0
        uic.loadUi("Documentacion/QtDesigner/login.ui", self)
        self.le_contrasena.setEchoMode(QLineEdit.EchoMode.Password)
        self.pb_ingresar.clicked.connect(lambda: self.bt_ingresar_logica())
        self.clb_crear_conultorio.clicked.connect(lambda: self.clb_crear_cuenta_usuario())


    def bt_ingresar_logica(self):
        print(f"Intento {self.intento}")
        if self.intento == 5:
            self.mb.message_box(self,"info","Se bloqueo el login","Dentro de 5 minutos vuela a ingresar el usuario y contraseña")
            QTimer.singleShot(300000, self.desbloquear_login)
        else:
            lista_faltan = []
            usuario = self.le_usuario.text()
            usuario.strip()
            if not usuario:
                lista_faltan.append("Usuario")
            contrasena = self.le_contrasena.text()
            contrasena.strip()
            if not contrasena:
                lista_faltan.append("Contraseña")
            if len(lista_faltan) > 0:
                mensaje = ", ".join(lista_faltan)
                self.mb.message_box(self, "info", "Faltan los datos", mensaje)
            else:
                try:
                    lista_nombre = [usuario]
                    hash_db = GLS.obtener_password_hash_db(self.db, lista_nombre)
                    if not hash_db:
                        print(f"No se encontro la contraseña en la bd {hash_db}")
                        self.mb.message_box(self,"error", "Error","No se encontro el usuario o contraseña incorrecta")
                        self.intento = self.intento + 1
                    else:
                        if not self.en.find_parssword_hash(hash_bd=hash_db, password=contrasena):
                            self.mb.message_box(self, "info", "Error", "Ingreso la contraseña incorrecta")
                            self.intento = self.intento + 1
                        else:
                            self.mb.message_box(self, "info","Bienvenido", f"Bienvenido {usuario}, redireccionando a el menu" )
                            self.navegar.ir_a_ventana("menu_principal")
                except Exception as e:
                    print(f"Error critico: {e}")
=======
        uic.loadUi("Documentacion/QtDesigner/login.ui", self)
        self.le_contrasena.setEchoMode(QLineEdit.EchoMode.Password)
        self.pb_ingresar.clicked.connect(lambda: self.bt_ingresar_logica(self.le_usuario.text(),self.le_contrasena.text()))
        self.clb_crear_conultorio.clicked.connect(lambda: self.clb_crear_cuenta_usuario())


    def bt_ingresar_logica(self, le_usuario, le_password):
        usuario = le_usuario.strip()
        password =  le_password.strip()
        if not usuario or not password:
            self.mb.message_box(self,"error", "Error", "Datos faltantes")

        elif usuario == "Asgard" and password == "1234":
            self.navegar.ir_a_ventana("menu_principal")
        else:
            self.mb.message_box(self,"info", "Error", "Usuario no encontrado")
>>>>>>> c2983caab5b8c6a3f8beff40b13f4603256eb540

    def clb_crear_cuenta_usuario(self):
        self.navegar.ir_a_ventana("crear_consultorio")

<<<<<<< HEAD
    def desbloquear_login(self):
        self.intento = 0
        self.mb.message_box(self,"info","Inicio de sesion desbloqueado", "Se desbloque el inicio de sesion")

=======
>>>>>>> c2983caab5b8c6a3f8beff40b13f4603256eb540
