from typing import _ProtocolMeta

from Login.Functions.Encrypt import Encrypt
from BaseDatos.MySqlManager import MySqlManager
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget, QTableView, QHeaderView, QTableWidget, QTableWidgetItem, QHBoxLayout, QHeaderView, QVBoxLayout, QDialog, QLineEdit
from PyQt6 import uic
from PyQt6.QtCore import Qt, QAbstractTableModel
from limitar_intput import Limitar_Intput as LI
from Usuario.Servicio.general_usuario_service  import General_Usuario_Service as GUS
from message_box import Message_Box as MB
from general_sistem_service import General_Sistem_Service as GSS
from Usuario.Model.usuario_model import Usuario_Model as UM
from almacendar_id_us_con import Almacenar_Id_Usuario_Consultorio_SG as AIUCSG

class Ventana_Nuevo_Usuario_Crear(QDialog):

    def __init__(self, db: MySqlManager):
        super().__init__()
        self.db = db
        self.gus = GUS
        self.mb = MB()
        self.e = Encrypt()
        uic.loadUi("Documentacion/QtDesigner/usuario_nuevo_crear.ui", self) # important

        self.le_apellido_paterno.setValidator(LI.limitar_caracteres("datos_generales"))
        self.le_apellido_materno.setValidator(LI.limitar_caracteres("datos_generales"))
        self.le_cedula_profesional.setValidator(LI.limitar_caracteres("cedula"))
        self.le_cedula_especialidad.setValidator(LI.limitar_caracteres("cedula"))
        self.le_contrasena.setValidator(LI.limitar_caracteres("regular"))
        self.le_nombre_usuario.setValidator(LI.limitar_caracteres("datos_generales"))
        self.cb_escuela.addItems(self.cbx_llenar_escuela())
        self.cb_tipo_usuario.addItems(self.llenar_cmb_tipo_usuario())
        self.pb_crear_usuario.clicked.connect(lambda: self.psb_crear_usuario())
        self.le_contrasena.setEchoMode(QLineEdit.EchoMode.Password)

    def psb_crear_usuario(self):
        try:
            lista_faltan = []
            nombre = self.le_nombre_usuario.text()
            nombre.strip()
            if not nombre:
                lista_faltan.append("Nombre")
            paterno = self.le_apellido_paterno.text()
            paterno.strip()
            if not paterno:
                lista_faltan.append("Apellido paterno")
            materno = self.le_apellido_materno.text()
            materno.strip()
            if not materno:
                lista_faltan.append("Apellido materno")
            password = self.le_contrasena.text()
            password.strip()
            has_password = self.e.generate_password_hash(password=password)
            if not has_password:
                lista_faltan.append("Contraseña")
            ced_profesional = self.le_cedula_profesional.text()
            ced_profesional.strip()
            if not ced_profesional:
                lista_faltan.append("Cedula profesional")
            ced_especialidad = self.le_cedula_especialidad.text()
            ced_especialidad.strip()
            if not ced_especialidad:
                lista_faltan.append("Cedula especialidad")
            tipo_usuario = self.le_cedula_especialidad.text().strip()
            if not tipo_usuario:
                lista_faltan.append("No se encontro el usuario propietario")
            escuela = self.cb_escuela.currentText()
            digito_escuela = GSS.obtener_solo_numeros(escuela)
            if not digito_escuela:
                lista_faltan.append("Escuela")
            tipo_usuario_cbx = self.cb_tipo_usuario.currentText()
            digito_tipo_usuario = GSS.obtener_solo_numeros(tipo_usuario_cbx)
            if not tipo_usuario_cbx:
                lista_faltan.append("Tipo usuario")
            if len(lista_faltan) > 0:
                mensaje = "".join(lista_faltan)
                self.mb.message_box(self, "info", "Faltan datos", mensaje=mensaje)
            else:
                try:
                    um = UM(
                        name=nombre,
                        paterno=paterno,
                        materno=materno,
                        password=has_password,
                        cedula_especialidad=ced_especialidad,
                        cedula_profesional=ced_profesional,
                        id_tipo_usuario=digito_tipo_usuario,
                        id_consultorio=AIUCSG.obetner_id_consultorio(),
                        id_esucela=digito_escuela
                    )
                    nombre_lista = [nombre]
                    cantidad = self.cantidad_usuario_duplicado(nombre_lista)
                    if cantidad > 0:
                        self.mb.message_box(self, "info", "Usuario duplicado", "Se encontro un usario duplicado, cambie el nombre de usuario")
                    else:
                        if um.crear_usuario(self.db):
                            self.mb.message_box(self, "info", "Usario generado", "Usuario generado con exito")
                            self.accept()
                        else:
                            self.mb.message_box(self, "error", "Usuario no generado", "El usario no se pudo generar")
                            self.accept()
                except Exception as e:
                    print(f"Error critico: {e}")
                    self.accept()
        except Exception as e:
            print(f"Error critico {e}")
            self.mb.message_box(self,"error","Error", "Ocurrrio un error al crear el usuario")
            self.accept()

    def cbx_llenar_escuela(self):
        try:
            tupla_estado = GUS.obtener_escuela(self.db)
            if tupla_estado is None:
                raise ValueError("No logro cargar la tupla")
            lista_texto = [fila["escuela"] for fila in tupla_estado]
            return  lista_texto
        except Exception as e:
            print(f"Erorr critico: {e}")
            self.mb.message_box(self,"info", "Error", "No se logro cargar las ecuelas")
            self.accept()
            return []

    def llenar_cmb_tipo_usuario(self):
        # Cambia un la lógica cuando se usa fietch one
        try:
            tupla_tipo_usuario = GUS.obtener_tipo_usuario(self.db)
            if tupla_tipo_usuario is None:
                raise ValueError("No se logro cargar la tupla")
            lista_texto_tipo_usuario = [fila["tipo_usuario"] for fila in tupla_tipo_usuario]
            return  lista_texto_tipo_usuario
        except Exception as e:
            print(f"Error critico: {e}")
            self.mb.message_box(self,"info","Error","No se logro cargar los tipos de usuario")
            self.accept()

    def obenter_consultorio(self):
       id_consultorio = AIUCSG.obetner_id_consultorio()
       return id_consultorio

    def cantidad_usuario_duplicado(self, lista_nombre):
       cantidad_duplicado = GUS.encontrar_duplicados_usuarios(self.db, lista_nombre)
       if cantidad_duplicado:
           return cantidad_duplicado
       else:
           return 0

