from BaseDatos.MySqlManager import MySqlManager
from PyQt6.QtWidgets import QWidget
from PyQt6 import uic
from Consultorio.Servicio.general_consultorio_service import General_Consultorio_Service as GCS
from message_box import Message_Box
from Login.Functions.Encrypt import Encrypt as ecy
from Configuracion.Service.general_contrasena_service import General_Contrasena_Service as GPS

class Ventana_Cambiar_Contrasena(QWidget):
    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.db = db
        uic.loadUi("Documentacion/QtDesigner/combiar_contrasena.ui", self)
        self.mb = Message_Box()
        self.es = GCS()
        self.le_contrasena_nuev
        self.le_repetir_contrasena
        self.pb_cambiar_contrasena.clicked.connect(lambda: self.comparar_contrasena())

    def comparar_contrasena(self):

        contrasena = self.le_contrasena_nuev.text().strip()
        contrasena_rep = self.le_repetir_contrasena.text().strip()
        lista_vacio = []
        if not contrasena:
            lista_vacio.append("Contraseña nueva")
        if not contrasena_rep:
            lista_vacio.append("Repetir contraseña")
        if len(lista_vacio):
            mensaje = ", ".join(lista_vacio)
            self.mb.message_box(self, "info", "Faltan los datos", mensaje)
        else:
            if contrasena == contrasena_rep:
                hash_pass = ecy.generate_password_hash(self, contrasena)
                if GPS.actualizar_contraseña(self.db, hash_pass):
                    self.mb.message_box(self, "info", "Cambiada", "Se cambio la contraseña exitosamente")
            else:
                self.mb.message_box(self,"info", "No coinciden", "Las contraseñas no coinciden")
