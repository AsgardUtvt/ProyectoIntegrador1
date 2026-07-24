from PyQt6.uic.uiparser import QtWidgets
from Login.Functions.Encrypt import Encrypt
from BaseDatos.MySqlManager import MySqlManager
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget
from PyQt6 import uic
from limitar_intput import Limitar_Intput as LI
from Usuario.Servicio.general_usuario_service  import General_Usuario_Service as GUS
from message_box import Message_Box

class Ventana_Moficar_Usuario(QWidget):

    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.navegar = navegar
        self.db = db
        self.gus = GUS
        self.mb = Message_Box()
        self.e = Encrypt()
        uic.loadUi("Documentacion/QtDesigner/usuario_modificar.ui", self) # importante
