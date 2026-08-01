from os.path import join
from typing import Container
from BaseDatos.MySqlManager import MySqlManager
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidge, QLineEdit
from PyQt6 import uic
from Consultorio.Model.consultorio_model import Consultorio_Model
from Consultorio.Servicio.general_consultorio_service import General_Consultorio_Service as GCS
from message_box import Message_Box
from limitar_intput import Limitar_Intput
from general_sistem_service import General_Sistem_Service as GSS

class Ventana_Cambiar_Contrasena(QWidget):
    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.navegar = navegar
        self.db = db
        uic.loadUi("Documentacion/QtDesigner/consultorio_crear.ui", self)
        self.mb = Message_Box()
        self.es = GCS()
        self.le_contrasena_nuev.setEchoMode(QLineEdit.EchoMode.Password)
        self.le_repetir_contrasena.setEchoMode(QLineEdit.EchoMode.Password)
