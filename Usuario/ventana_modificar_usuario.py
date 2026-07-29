from typing import _ProtocolMeta

from Login.Functions.Encrypt import Encrypt
from BaseDatos.MySqlManager import MySqlManager
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget, QTableView, QHeaderView, QTableWidget, QTableWidgetItem, QHBoxLayout, QHeaderView, QVBoxLayout, QDialog
from PyQt6 import uic
from PyQt6.QtCore import Qt, QAbstractTableModel
from limitar_intput import Limitar_Intput as LI
from Usuario.Servicio.general_usuario_service  import General_Usuario_Service as GUS
from message_box import Message_Box as MB
from almacendar_id_us_con import Almacenar_Id_Usuario_Consultorio_SG as AIUCSG
from Usuario.ventana_nuevo_usuario_crear import Ventana_Nuevo_Usuario_Crear as VNUC
from Usuario.ventana_modificar_usuario_dialog import Vetana_Modificar_Usuario_Dialog as VMUD
from Usuario.Model.usuario_model import Usuario_Model as UM
class Ventana_Moficar_Usuario(QWidget):

    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.navegar = navegar
        self.db = db
        self.gus = GUS
        self.mb = MB()
        self.e = Encrypt()
        uic.loadUi("Documentacion/QtDesigner/usuario_modificar.ui", self) # importante
        self.pb_nuevo_usuario.clicked.connect(lambda: self.btn_nuevo_usuario())
        # --- BLOQUE DE DEPURACIÓN ---
        print("Tipo de widget:", type(self.tw_modificar_usuario))
        print("Tamaño de la tabla:", self.tw_modificar_usuario.size())
        print("Es visible?:", self.tw_modificar_usuario.isVisible())
        print("Filas antes de cargar:", self.tw_modificar_usuario.rowCount())
        # ----------------------------
        self.tw_modificar_usuario.setColumnCount(3)
        self.columnas_table_view = ["Id", "Usuario", "Opciones"]
        self.tw_modificar_usuario.setHorizontalHeaderLabels(self.columnas_table_view)

        self.tw_modificar_usuario.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.tw_modificar_usuario.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.tw_modificar_usuario.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

        self.cargar_datos()

    def cargar_datos(self):
        datos = GUS.obtener_todos_usuarios_consultorio(self.db, AIUCSG.obetner_id_consultorio())
        if datos:
            for fila, usuario in enumerate(datos):
                self.tw_modificar_usuario.insertRow(fila)

                id_val = usuario["id_val"]
                nombre = usuario["nombre"]

                self.tw_modificar_usuario.setItem(fila, 0, QTableWidgetItem(str(id_val)))
                self.tw_modificar_usuario.setItem(fila, 1, QTableWidgetItem(nombre))
                contenedor = QWidget()
                layout_btn = QHBoxLayout(contenedor)
                layout_btn.setContentsMargins(2,2,2,2)
                btn_mod = QPushButton("Modificar")
                btn_del = QPushButton("Eliminar")

                btn_mod.clicked.connect(lambda checked, r=id_val: self.modificar(r))
                btn_del.clicked.connect(lambda checked, r=id_val: self.eliminar(r))

                layout_btn.addWidget(btn_mod)
                layout_btn.addWidget(btn_del)

                self.tw_modificar_usuario.setCellWidget(fila, 2, contenedor)
        else:
            self.tw_modificar_usuario.insertRow(0)
            print("No hay datos que cargar")


    def modificar(self, val):
        dialog_modificar = VMUD(self.db, val)
        if dialog_modificar.exec():
            print("Modificar")


    def eliminar(self,val):
        print(f"Eliminar {val}")
        list_id = [val]
        if self.mb.message_box(self,"question","Eliminar","Estas seguro de eliminar a este usuario") == QMessageBox.StandardButton.Yes:
            if UM.eliminar_usuario(self.db,list_id):
                self.mb.message_box(self, "info","Eliminado", "Se elimino el usuario con exito")
            else:
                self.mb.message_box(self, "error", "Error", "Ocurrio un error en al eliminar el usuario")
                

    def btn_nuevo_usuario(self):
        dialog_nuevo = VNUC(self.db)
        if dialog_nuevo.exec():
            print("Guardado")
