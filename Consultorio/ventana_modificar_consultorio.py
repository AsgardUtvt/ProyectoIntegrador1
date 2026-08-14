from BaseDatos.MySqlManager import MySqlManager
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget, QTableView, QHeaderView, QTableWidget, QTableWidgetItem, QHBoxLayout, QHeaderView, QVBoxLayout, QDialog
from PyQt6 import uic
from limitar_intput import Limitar_Intput as LI
from Usuario.Servicio.general_usuario_service  import General_Usuario_Service as GUS
from message_box import Message_Box
from almacendar_id_us_con import Almacenar_Id_Usuario_Consultorio_SG as AIUCSG
from Consultorio.ventana_nuevo_consultorio_dialog import Ventana_Nuevo_Consultorio_Dialog as VNCD
from Consultorio.ventana_modificar_consultorio_dialog import Ventana_Modificar_Consultorio_Dialog as VMCD
from Consultorio.Model.consultorio_model import  Consultorio_Model as CM
from Consultorio.Model.sub_consultorio_model import Sub_Consultorio_Model as SCM
from Consultorio.Servicio.general_consultorio_service import General_Consultorio_Service as GCS
from Consultorio.ventana_modificar_sub_consultorio_dialog import Ventana_Modificar_Sub_Consultorio_Dialog as VMSCD

class Ventana_Modificar_Consultorio(QWidget):
    _TUPLA_DATOS = ()
    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.navegar = navegar
        self.db = db
        self.mb = Message_Box()
        uic.loadUi("Documentacion/QtDesigner/consultorio_modificar.ui", self)
        self.pb_nueva_clinica.clicked.connect(lambda: self.btn_nuevo_usuario())
        # --- BLOQUE DE DEPURACIÓN ---
        print("Tipo de widget:", type(self.tw_clinica))
        print("Tamaño de la tabla:", self.tw_clinica.size())
        print("Es visible?:", self.tw_clinica.isVisible())
        print("Filas antes de cargar:", self.tw_clinica.rowCount())
        # ----------------------------
        self.tw_clinica.setColumnCount(3)
        self.columnas_table_view = ["Id", "Clínica", "Opciones"]
        self.tw_clinica.setHorizontalHeaderLabels(self.columnas_table_view)

        self.tw_clinica.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.tw_clinica.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.tw_clinica.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)


        self.tw_sub_clinica.setColumnCount(3)
        self.columnas_table_view2 = ["Id", "Sub clínica", "Opciones"]
        self.tw_sub_clinica.setHorizontalHeaderLabels(self.columnas_table_view2)

        self.tw_sub_clinica.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.tw_sub_clinica.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.tw_sub_clinica.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)


        self.cargar_datos()
        self.cargar_datos_sub_clinica()

    def cargar_datos(self):
        datos = GCS.obtener_consultorio(self.db, [AIUCSG.obetner_id_consultorio()])
        if datos:
            self.tw_clinica.insertRow(0)

            id_val:str = datos["ID"]
            nombre:str = datos["CON"]

            self.tw_clinica.setItem(0, 0, QTableWidgetItem(str(id_val)))
            self.tw_clinica.setItem(0, 1, QTableWidgetItem(nombre))
            contenedor = QWidget()
            layout_btn = QHBoxLayout(contenedor)
            layout_btn.setContentsMargins(2,2,2,2)
            btn_mod = QPushButton("Modificar")

            btn_mod.clicked.connect(lambda checked, r=id_val: self.modificar(r))

            layout_btn.addWidget(btn_mod)

            self.tw_clinica.setCellWidget(0, 2, contenedor)
        else:
            self.tw_clinica.insertRow(0)
            print("No hay datos que cargar")


    def cargar_datos_sub_clinica(self):
        datos = GCS.obtener_sub_consultorio(self.db, [AIUCSG.obetner_id_consultorio()])
        if datos:
            for fila, sub_consultorio in enumerate(datos):
                self.tw_sub_clinica.insertRow(fila)

                id_val = sub_consultorio["ID"]
                nombre = sub_consultorio["CON"]

                self.tw_sub_clinica.setItem(fila, 0, QTableWidgetItem(str(id_val)))
                self.tw_sub_clinica.setItem(fila, 1, QTableWidgetItem(nombre))
                contenedor = QWidget()
                layout_btn = QHBoxLayout(contenedor)
                layout_btn.setContentsMargins(2,2,2,2)
                btn_mod_sub = QPushButton("Modificar")
                btn_del_sub = QPushButton("Eliminar")

                btn_mod_sub.clicked.connect(lambda checked, r=id_val: self.modificar_sub(r))
                btn_del_sub.clicked.connect(lambda checked, r=id_val: self.eliminar_sub(r))

                layout_btn.addWidget(btn_mod_sub)
                layout_btn.addWidget(btn_del_sub)

                self.tw_sub_clinica.setCellWidget(fila, 2, contenedor)
        else:
            self.tw_sub_clinica.insertRow(0)
            print("No hay datos que cargar")


    def modificar(self, val):
        val_int = int(val)
        dialog_modificar = VMCD(self.db, val_int)
        if dialog_modificar.exec():
            self.refrescar_datos()

    def modificar_sub(self, val):
        dialog_modificar = VMSCD(self.db, val)
        if dialog_modificar.exec():
            print("Modificar")
            self.refrescar_datos()


    def eliminar_sub(self,val):
        print(f"Eliminar {val}")
        list_id = [AIUCSG.obetner_id_consultorio(),val]
        if self.mb.message_box(self,"question","Eliminar","Estas seguro de eliminar a este usuario") == QMessageBox.StandardButton.Yes:

            if SCM.eliminar_sub_consultorio(self.db,list_id):
                self.mb.message_box(self, "info","Eliminado", "Se elimino el usuario con exito")
                self.refrescar_datos()
            else:
                self.mb.message_box(self, "error", "Error", "Ocurrio un error en al eliminar el usuario")

    def btn_nuevo_usuario(self):
        dialog_nuevo = VNCD(self.db)
        if dialog_nuevo.exec():
            print("Guardado")
            self.refrescar_datos()

    def refrescar_datos(self):
        self.cargar_datos_sub_clinica()
