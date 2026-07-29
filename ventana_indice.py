''' se importan las librerias necesarias '''
from BaseDatos.MySqlManager import MySqlManager
from Login.LoginApp import Login_App
from Usuario.ventana_crear_usuario import Ventana_Crear_Usuario
from Consultorio.ventana_crear_consultorio import Vetana_Crear_Consultorio
from Menu.ventana_menu import Ventana_Menu_Principal


from PyQt6.QtWidgets import QMainWindow, QStackedWidget


class Ventana_Indice(QMainWindow):
    ''' Para mantener el orden  de las diferentes ventanas del sistema '''
    def __init__(self, db: MySqlManager) -> None:
        super().__init__()
        # Si queremos cambiar el tamaño maximo de la pantalla movemos estos atributos
        self.setMinimumSize(800,600)
        self.stacked = QStackedWidget()
        self.setCentralWidget(self.stacked)
        # Se agrega diccionario con indice de vetnanas
        self.ventana_indice = {
            "login": 0,
            "menu_principal": 1,
            "crear_consultorio": 2,
            "crear_usuario": 3,
            
            
            "
            
        }
        # Se generan las ventanas a ocupar
        self.main_window = Login_App( db, self)
        self.main_ventana_base = Ventana_Menu_Principal( db, self)
        self.main_ventana_crear_consultorio = Vetana_Crear_Consultorio(db, self)
        self.main_ventana_crear_usuario = Ventana_Crear_Usuario(db, self)
        # Al momento de agregar una vista nueva tambien se tiene que agregar en el mismo orden que el diccionario
        self.stacked.addWidget(self.main_window)
        self.stacked.addWidget(self.main_ventana_base)
        self.stacked.addWidget(self.main_ventana_crear_consultorio)
        self.stacked.addWidget(self.main_ventana_crear_usuario)
        self.ir_a_ventana("login")

    def ir_a_ventana(self, nombre_ventana):
        if nombre_ventana in self.ventana_indice:
            indice = self.ventana_indice[nombre_ventana]
            self.stacked.setCurrentIndex(indice)
            ventana_acual = self.stacked.widget(indice)
            titulo_ventan_ui = ventana_acual.windowTitle()
            if titulo_ventan_ui:
                self.setWindowTitle(titulo_ventan_ui)
            else:
                self.setWindowTitle("SIHMED")
        else:
            print(f"La ventana {nombre_ventana}, no existe en el diccionario")
            


