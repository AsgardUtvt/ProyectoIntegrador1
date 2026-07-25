from Usuario.ventana_modificar_usuario import Ventana_Moficar_Usuario
from BaseDatos.MySqlManager import MySqlManager
from PyQt6.QtWidgets import QWidget

class Lista_Indice(QWidget):
    def __init__(self, db: MySqlManager) -> None:
        super().__init__()
        self._LISTA_VENTAS = {
            "modificar_usuario": Ventana_Moficar_Usuario(db, self)
        }

        self._LISTA_MENU = {
            0: "menu_principal",
            1: "pacientes",
            2: "inventario",
            3: "ventas",
            4: "usuarios",
            5: "reportes",
            6: "configuracion"
        }

        self.ventana_indice = {}
        for 


