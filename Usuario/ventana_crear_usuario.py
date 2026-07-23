from PyQt6.uic.uiparser import QtWidgets

from BaseDatos.MySqlManager import MySqlManager
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget
from PyQt6 import uic
from limitar_intput import Limitar_Intput as LI
import limitar_intput

class Ventana_Crear_Usuario(QWidget):

    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.navegar = navegar
        self.db = db
        uic.loadUi("Documentacion/QtDesigner/usuario_crear.ui", self)
        self.le_apellido_paterno.setValidator(LI.limitar_caracteres("datos_generales"))
        self.le_apellido_materno.setValidator(LI.limitar_caracteres("datos_generales"))
        self.le_cedula_profesional.setValidator(LI.limitar_caracteres("datos_generales"))
        self.le_cedula_especialidad.setValidator(LI.limitar_caracteres("cedula"))
        self.le_contrasena.setValidator(LI.limitar_caracteres("cedula"))
        self.le_nombre_usuario.setValidator(LI.limitar_caracteres("datos_generales"))
        self.cb_escuela.addItems(self.espera_funcion())
        self.id_tipo_usuario =  self.espera_funcion()
        self.pb_crear_usuario.clicked.connect(lambda: self.psb_crear_usuario())

    def psb_crear_usuario(self):
        pass

    def espera_funcion(self):
        pass

