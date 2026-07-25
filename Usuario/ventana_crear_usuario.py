from PyQt6.uic.uiparser import QtWidgets
from Login.Functions.Encrypt import Encrypt
from BaseDatos.MySqlManager import MySqlManager
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget, QLineEdit
from PyQt6 import uic
from limitar_intput import Limitar_Intput as LI
from Usuario.Servicio.general_usuario_service  import General_Usuario_Service as GUS
from message_box import Message_Box
from general_sistem_service import General_Sistem_Service as GSS
from Usuario.Model.usuario_model import Usuario_Model as UM
from almacendar_id_us_con import Almacenar_Id_Usuario_Consultorio_SG as AIUCSG

class Ventana_Crear_Usuario(QWidget):

    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.navegar = navegar
        self.db = db
        self.gus = GUS
        self.mb = Message_Box()
        self.e = Encrypt()
        uic.loadUi("Documentacion/QtDesigner/usuario_crear.ui", self)
        self.le_apellido_paterno.setValidator(LI.limitar_caracteres("datos_generales"))
        self.le_apellido_materno.setValidator(LI.limitar_caracteres("datos_generales"))
        self.le_cedula_profesional.setValidator(LI.limitar_caracteres("cedula"))
        self.le_cedula_especialidad.setValidator(LI.limitar_caracteres("cedula"))
        self.le_contrasena.setValidator(LI.limitar_caracteres("regular"))
        self.le_nombre_usuario.setValidator(LI.limitar_caracteres("datos_generales"))
        self.cb_escuela.addItems(self.cbx_llenar_escuela())
        self.pb_crear_usuario.clicked.connect(lambda: self.psb_crear_usuario())
        self.le_contrasena.setEchoMode(QLineEdit.EchoMode.Password)
        self.id_tipo_usuario = self.obtener_id_usuario()

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
            tipo_usuario = self.id_tipo_usuario
            if not tipo_usuario:
                lista_faltan.append("No se encontro el usuario propietario")
            escuela = self.cb_escuela.currentText()
            digito_escuela = GSS.obtener_solo_numeros(escuela)
            if not digito_escuela:
                lista_faltan.append("Escuela")
            if len(lista_faltan) > 0:
<<<<<<< HEAD
                mensaje = "".join(lista_faltan)
                self.mb.message_box(self, "info", "Faltan datos", mensaje=mensaje)
            else:
=======
>>>>>>> c2983caab5b8c6a3f8beff40b13f4603256eb540
                try:
                    um = UM(
                        name=nombre,
                        paterno=paterno,
                        materno=materno,
                        password=has_password,
                        cedula_especialidad=ced_especialidad,
                        cedula_profesional=ced_profesional,
<<<<<<< HEAD
                        id_tipo_usuario=tipo_usuario,
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
                            self.navegar.ir_a_ventana("menu_principal")
                        else:
                            self.mb.message_box(self, "error", "Usuario no generado", "El usario no se pudo generar")
                            self.navegar.ir_a_ventana("login")
=======
                        id_tipo_usuario=AIUCSG.obtener_id_usuario(),
                        id_consultorio=AIUCSG.obetner_id_consultorio(),
                        id_esucela=digito_escuela
                    )
                    um.crear_usuario(self.db)
>>>>>>> c2983caab5b8c6a3f8beff40b13f4603256eb540
                except Exception as e:
                    print(f"Error critico: {e}")
                    self.navegar.ir_a_ventana("login")
        except Exception as e:
            print(f"Error critico {e}")
            self.mb.message_box(self,"error","Error", "Ocurrrio un error al crear el usuario")
            self.navegar.ir_a_ventana("login")

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
            self.navegar.ir_a_ventana("login")
            return []

    def obtener_id_usuario(self):
        # Cambia un la lógica cuando se usa fetch one
        usuario_id = GUS.obtener_usuario_primeravez(self.db)
        if not usuario_id:
<<<<<<< HEAD
            raise ValueError(f"No se encontro el tipo de usuario propietario de la base de datos")
=======
            raise ValueError(f"No se encontro el usuario de la base de datos")
>>>>>>> c2983caab5b8c6a3f8beff40b13f4603256eb540
        else:
            return usuario_id

    def obenter_consultorio(self):
       id_consultorio = AIUCSG.obetner_id_consultorio()
       return id_consultorio
<<<<<<< HEAD

    def cantidad_usuario_duplicado(self, lista_nombre):
       cantidad_duplicado = GUS.encontrar_duplicados_usuarios(self.db, lista_nombre)
       if cantidad_duplicado:
           return cantidad_duplicado
       else:
           return 0

=======
>>>>>>> c2983caab5b8c6a3f8beff40b13f4603256eb540
