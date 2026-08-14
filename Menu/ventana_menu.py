from PyQt6.uic.uiparser import QtWidgets
from BaseDatos.MySqlManager import MySqlManager
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget, QVBoxLayout, QSizePolicy
from PyQt6 import uic
import os
from Usuario.ventana_modificar_usuario import Ventana_Moficar_Usuario
from Recetas.ventana_crear_recetas import Ventana_Crear_Recetas
from Configuracion.ventana_cambiar_contrasena import Ventana_Cambiar_Contrasena
from Consultorio.ventana_modificar_consultorio import Ventana_Modificar_Consultorio
from Menu.ventana_bienvenida import Ventana_Bienvenida
from Medicamentos.Medicamentos import Ventana_Medicamentos
from Pacientes.ventana_pacientes_modif import Ventana_Modificar_Paciente

class Ventana_Menu_Principal(QWidget):

    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.navegar = navegar
        self.db = db
        uic.loadUi("Documentacion/QtDesigner/menu_con_lista.ui", self)

        print(f"lw_enlace_menu: {self.lw_enlace_menu}")
        self.rutas_interfaces = {
            "menu_principal": "../Documentacion/QtDesigner/menu_principal.ui",
            "citas": "../Documentacion/QtDesigner/citasWidget.ui",
            "menu_pacientes": "../Documentacion/QtDesigner/pacientes_lista_modificar.ui",
            "recetas": "../Documentacion/QtDesigner/Recetas.ui",
            "inventario": "../Documentacion/QtDesigner/Medicamentoswidget.ui",
            "ventas": "../Documentacion/QtDesigner/ticket_pago.ui",
            "usuario": "../Documentacion/QtDesigner/usuario_modificar.ui",
            "consultorio": "../Documentacion/QtDesigner/consultorio_modificar.ui",
            "reportes_caja": "../Documentacion/QtDesigner/reportes_caja.ui",
            "reportes_medicamento": "../Documentacion/QtDesigner/Reportes_widget.ui",
            "contrasena": "../Documentacion/QtDesigner/combiar_contrasena.ui" 
        }
        opciones_menu = ["Inicio", "Citas","Pacientes", "Recetas", "Inventario", "Ventas", "Personal", "Clínica", "Reportes caja", "Reportes medicamento", "Contraseña"]
        self.lw_enlace_menu.clear()
        self.lw_enlace_menu.addItems(opciones_menu)
        self.lw_enlace_menu.setMinimumWidth(200)
        self.lw_enlace_menu.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        print(f"Items en listaWidget {self.lw_enlace_menu.count()}")
        for i in range(self.lw_enlace_menu.count()):
            print(f"Item {i}: {self.lw_enlace_menu.item(i).text()}")

        # Mapeo para rutas .ui (vistas simples)
        self.mapeo_menu = {
            0: "menu_principal",
            1: "citas",
            2: "menu_pacientes",
            3: "recetas",
            4: "inventario",
            5: "ventas",
            6: "usuario",
            7: "consultorio",
            8: "reportes_caja",
            9: "reportes_medicamento",
            10: "contrasena"
        }

        # Mapeo para clases personalizadas (vistas con lógica)
        self.mapeo_menu_clases = {
            0: Ventana_Bienvenida,  # menu_principal
            1: None, # citas
            2: Ventana_Modificar_Paciente,  # menu_pacientes
            3: Ventana_Crear_Recetas,  # recetas
            4: Ventana_Medicamentos,  # inventario
            5: None,  # ventas
            6: Ventana_Moficar_Usuario,  # personal
            7: Ventana_Modificar_Consultorio, # consulotorio
            8: None,  # reportes_caja
            9: None, # reportes_medicamentoo
            10: Ventana_Cambiar_Contrasena  # contrasena
        }

        self.layout_vistas = self.w_ventana.layout()
        self.layout_vistas.setContentsMargins(0,0,0,0)

        self.lw_enlace_menu.currentRowChanged.connect(self.cargar_ventanas)

        self.sub_ventana_actual = None

        self.lw_enlace_menu.setCurrentRow(0)

    def cargar_ventanas(self, fila):
        if fila in self.mapeo_menu_clases:
            clase_ventana = self.mapeo_menu_clases[fila]

            if clase_ventana is None:
                # Cargar .ui normalmente para las otras opciones
                nombre_ventana = self.mapeo_menu[fila]
                ruta_relativa = self.rutas_interfaces[nombre_ventana]

                dir_actual = os.path.dirname(os.path.abspath(__file__))
                ruta_absoluta = os.path.normpath(os.path.join(dir_actual, ruta_relativa))
                print(f"Cargando: {ruta_absoluta}")

                if os.path.exists(ruta_absoluta):
                    self.mostrar_nueva_interfaz(ruta_absoluta)
                else:
                    print(f"Error: no se encontro el archivo .ui en {ruta_absoluta}")
            else:
                # Instanciar clase personalizada
                self.mostrar_clase_personalizada(clase_ventana)

    def mostrar_nueva_interfaz(self, ruta_ui):
        if self.sub_ventana_actual is not None:
            self.layout_vistas.removeWidget(self.sub_ventana_actual)
            self.sub_ventana_actual.deleteLater()
            self.sub_ventana_actual = None
        self.sub_ventana_actual = QWidget()
        uic.loadUi(ruta_ui, self.sub_ventana_actual)
        self.sub_ventana_actual.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.layout_vistas.addWidget(self.sub_ventana_actual)
        self.sub_ventana_actual.show()

        titulo = self.sub_ventana_actual.windowTitle()
        self.window().setWindowTitle(titulo if titulo else "SIHMED")

    def mostrar_clase_personalizada(self, clase):
        if self.sub_ventana_actual is not None:
            self.layout_vistas.removeWidget(self.sub_ventana_actual)
            self.sub_ventana_actual.deleteLater()
            self.sub_ventana_actual = None

        # Instanciar la clase con sus parámetros
        self.sub_ventana_actual = clase(self.db, self)
        self.sub_ventana_actual.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.layout_vistas.addWidget(self.sub_ventana_actual)
        self.sub_ventana_actual.show()

        titulo = self.sub_ventana_actual.windowTitle()
        self.window().setWindowTitle(titulo if titulo else "SIHMED")
