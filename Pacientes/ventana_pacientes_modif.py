from typing import _ProtocolMeta

from Login.Functions.Encrypt import Encrypt
from BaseDatos.MySqlManager import MySqlManager
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget, QTableView, QHeaderView, QTableWidget, QTableWidgetItem, QHBoxLayout, QHeaderView, QVBoxLayout, QDialog
from PyQt6 import uic
from PyQt6.QtCore import Qt, QAbstractTableModel
from message_box import Message_Box as MB
from Pacientes.ventana_crear_paciente import Ventana_Crear_Paciente as VCP
from Pacientes.ventana_modificar_paciente import Ventana_Modificar_Pacientes as VMP
from almacendar_id_us_con import Almacenar_Id_Usuario_Consultorio_SG as AIUC

class Ventana_Modificar_Paciente(QWidget):

    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.navegar = navegar
        self.db = db
        self.mb = MB()
        self.e = Encrypt()
        uic.loadUi("Documentacion/QtDesigner/pacientes_lista_modificar.ui", self)
        self.pb_nuevo_paciente.clicked.connect(lambda: self.btn_nuevo_paciente())
        self.tw_modificar_paciente.setColumnCount(3)
        self.tw_modificar_paciente.show()
        self.columnas_table_view = ["Id", "Paciente", "Opciones"]
        self.tw_modificar_paciente.setHorizontalHeaderLabels(self.columnas_table_view)

        self.tw_modificar_paciente.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        self.tw_modificar_paciente.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.tw_modificar_paciente.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)

        self.cargar_datos()

    def cargar_datos(self):
        self.tw_modificar_paciente.setRowCount(0)
        datos = General_Paciente_Service.obtener_todos_pacientes(self.db)
        if datos:
            for fila, paciente in enumerate(datos):
                self.tw_modificar_paciente.insertRow(fila)

                id_val = paciente["IP"]
                nombre = paciente["Nombre Completo"]

                self.tw_modificar_paciente.setItem(fila, 0, QTableWidgetItem(str(id_val)))
                self.tw_modificar_paciente.setItem(fila, 1, QTableWidgetItem(nombre))
                contenedor = QWidget()
                layout_btn = QHBoxLayout(contenedor)
                layout_btn.setContentsMargins(2,2,2,2)
                btn_mod = QPushButton("Modificar")
                btn_del = QPushButton("Eliminar")

                btn_mod.clicked.connect(lambda checked, r=id_val: self.modificar(r))
                btn_del.clicked.connect(lambda checked, r=id_val: self.eliminar(r))

                layout_btn.addWidget(btn_mod)
                layout_btn.addWidget(btn_del)

                self.tw_modificar_paciente.setCellWidget(fila, 2, contenedor)
        else:
            print("No hay datos que cargar")


    def modificar(self, val):
        dialog_modificar = VMP(self.db, val)
        if dialog_modificar.exec():
            print("Modificar")
            self.cargar_datos


    def eliminar(self,val):
        print(f"Eliminar {val}")
        if self.mb.message_box(self,"question","Eliminar","¿Estas seguro de eliminar a este paciente?") == QMessageBox.StandardButton.Yes:
            try:
                with self.db.obtener_cursor() as cursor:
                    cursor.execute("DELETE FROM Paciente WHERE id_paciente = %s;", (val,))
                    self.db.conexion.commit()
                    
                self.mb.message_box(self, "info", "Eliminado", "Se elimino el paciente con exito.")
                self.cargar_datos()
            except Exception as E:
                print("Error al eliminar:", E)
                self.mb.message_box(self, "error", "Error", "Ocurrio un error al eliminar el paciente.")


    def btn_nuevo_paciente(self):
        dialog_nuevo = VCP(self.db)
        if dialog_nuevo.exec():
            print("Guardado")

class General_Paciente_Service:
    def obtener_todos_pacientes(DB: MySqlManager):
        try:
            valores= [AIUC.obetner_id_consultorio()]
            with DB.obtener_cursor() as cursor:
                sql_select_todos_pacientes="""
                    SELECT id_paciente AS 'IP', concat_ws(' ',paciente_name,paciente_paterno,paciente_materno) AS 'Nombre Completo' FROM Paciente
                    WHERE id_consultorio = %s;
                """
                #ejecutar
                cursor.execute(sql_select_todos_pacientes,valores)
                resultados=cursor.fetchall()
                print("resultados: ", resultados)
                return resultados if resultados else ()
            pass
        except Exception as E:
            print("Error.",E)
            return ()

