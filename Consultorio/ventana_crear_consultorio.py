from BaseDatos.MySqlManager import MySqlManager
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget
from PyQt6 import uic
from Consultorio.Model.consultorio_model import Consultorio_Model
from Consultorio.Servicio.estado_servicio import Estado_Servicio
from message_box import Message_Box
from limitar_intput import Limitar_Intput

class Vetana_Crear_Consultorio(QWidget):

    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.navegar = navegar
        self.db = db
        uic.loadUi("Documentacion/QtDesigner/consultorio_crear.ui", self)
        self.mb = Message_Box()
        self.es = Estado_Servicio()
        self.cb_estado.addItems(self.llenar_cbx_estado())
        self.le_nombre_consultorio.setValidator(Limitar_Intput.limitar_caracteres("regular"))



    def llenar_cbx_estado(self) -> list:
        try:
            tupla_estado = self.es.obtener_estado(self.db)
            lista_texto = [fila["concat"] for fila in tupla_estado]

            return  lista_texto
        except Exception as e:
            print(f"Erorr critico: {e}")
            self.mb.message_box("info", "Error", "No se logro cargar los estados")
            self.navegar.ir_a_ventan("login")
            return []

    def btn_crear_usuario(self):
        pass
