from BaseDatos.MySqlManager import MySqlManager
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QWidget
from PyQt6 import uic
from Consultorio.Model.consultorio_model import Consultorio_Model
from Consultorio.Servicio.general_consultorio_service import General_Consultorio_Service as GCS
from message_box import Message_Box
from limitar_intput import Limitar_Intput
from general_sistem_service import General_Sistem_Service as GSS
from almacendar_id_us_con import Almacenar_Id_Usuario_Consultorio_SG as AIUCSG
from Consultorio.Model.consultorio_model import Consultorio_Model as CM

class Ventana_Modificar_Consultorio(QWidget):
    _TUPLA_DATOS = ()
    def __init__(self, db: MySqlManager, navegar):
        super().__init__()
        self.navegar = navegar
        self.db = db
        uic.loadUi("Documentacion/QtDesigner/consultorio_modificar.ui", self)
        self.mb = Message_Box()
        self.es = GCS()
        self.cb_estado.addItems(self.llenar_cbx_estado())
        self.le_nombre_consultorio.setValidator(Limitar_Intput.limitar_caracteres("consultorio"))
        self.le_colonia.setValidator(Limitar_Intput.limitar_caracteres("calle_numero"))
        self.le_cp.setValidator(Limitar_Intput.limitar_caracteres("codigo_postal"))
        self.le_localidad.setValidator(Limitar_Intput.limitar_caracteres("calle_numero"))
        self.le_municipio.setValidator(Limitar_Intput.limitar_caracteres("calle_numero"))
        self.le_num_exterior.setValidator(Limitar_Intput.limitar_caracteres("numero_calle"))
        self.le_num_interior.setValidator(Limitar_Intput.limitar_caracteres("numero_calle"))
        self.le_calle.setValidator(Limitar_Intput.limitar_caracteres("calle"))
        self.le_telefono.setValidator(Limitar_Intput.limitar_caracteres("numero_telefonico"))
        self.le_telefono_dos.setValidator(Limitar_Intput.limitar_caracteres("numero_telefonico"))
        self.pb_modificar_consultorio.clicked.connect(lambda: self.btn_crear_consultorio())



    def llenar_cbx_estado(self) -> list:
        try:
            tupla_estado = self.es.obtener_estado(self.db)
            lista_texto = [fila["concat"] for fila in tupla_estado]

            return  lista_texto
        except Exception as e:
            print(f"Erorr critico: {e}")
            self.mb.message_box(self,"info", "Error", "No se logro cargar los estados")
            self.navegar.ir_a_ventana("login")
            return []

    def btn_crear_consultorio(self):
        """
        btn_crear_usuario()
        No se entiende ni venrga al código alv
        No resive ningun parametro
        Esta función lo que hace es comparar cada label edit
        de la interfas, en caso de no estar llevanada lo alamcena
        en una lista llamada datos faltantes y lo genra un join de datos faltantes
        para ser retornadnos en el mesnaje \"mb\", también
        para obtener los digitos del estado se manda usa casi la misma
        lógica pero compara si hay un numero y lo almacena en digitos_id_estado
        al final esta lista se une con un join a digitos
        esta madre se tiene que encapsuar para obtener todo este pedo con una funcion
        paragenerar el usuario.
        """
        try:
            datos_faltantes = []
            nombre_consultorio = self.le_nombre_consultorio.text()
            nombre_consultorio.strip()
            if not nombre_consultorio:
                datos_faltantes.append("Nombre")
            calle = self.le_calle.text()
            calle.strip()
            if not calle:
                datos_faltantes.append("Calle")
            colonia = self.le_colonia.text()
            colonia.strip()
            if not colonia:
                datos_faltantes.append("Colonia")
            num_exeterior = self.le_num_exterior.text()
            num_exeterior.strip()
            if not num_exeterior:
                datos_faltantes.append("Número exterior")
            num_interior = self.le_num_interior.text()
            num_interior.strip()
            if not num_interior:
                datos_faltantes.append("Número interior")
            localidad = self.le_localidad.text()
            localidad.strip()
            if not localidad:
                datos_faltantes.append("Localidad")
            estado = str(self.cb_estado.currentText())
            digitos = GSS.obtener_solo_numeros(estado)
            if not digitos:
                datos_faltantes.append("Estado")
            telefono = self.le_telefono.text()
            telefono.strip()
            if not telefono:
                datos_faltantes.append("Telefono 1")
            telefono_dos = self.le_telefono_dos.text()
            telefono_dos.strip()
            if not telefono_dos:
                datos_faltantes.append("Telefono 2")
            municipio = self.le_municipio.text()
            municipio.strip()
            if not municipio:
                datos_faltantes.append("Municipio")
            cp = self.le_cp.text()
            cp.strip()
            if not cp:
                datos_faltantes.append("Codigo Postal o C.P.")
            if len(datos_faltantes) > 0:
                mensaje = str(", ".join(datos_faltantes))
                self.message_box_datos_faltantes(mensaje=mensaje)
            else:
                try:
                    if self.cantidad_consultorio_duplicado(nombre_consultorio_list) > 0:
                        self.mb.message_box(self,"info", "Duplicado", "Ya hay un consultorio con ese nombre, cambien el nombre del consultorio")
                    else:
                        if CM.actualizar_datos(self.db, name_update=nombre_consultorio, calle_update=calle, colonia_update=colonia, num_ext_update=num_exeterior, num_int_update=num_interior, localidad_update=localidad, id_estado_update=digitos, tel_update=telefono, tel_dos_update=telefono_dos, municipio_update=municipio, cp_update=cp):
                            tipo, titulo, mensaje = "info", "Generado con exito", "Se genero con exito el consultorio"
                            self.mb.message_box(self, tipo=tipo, titulo=titulo, mensaje=mensaje)
                            self.navegar.ir_a_ventana("crear_usuario")
                        else:
                            self.mb.message_box(self,"error","Error", "Hubo un error al generar el consultorio")
                            self.navegar.ir_a_ventana("login")
                except Exception as e:
                    print(f"Error cirtico {e}")
                    tipo, titulo, mensaje = "error", "Consultorio", "No se pudo genrear el consultorio"
                    self.mb.message_box(self,tipo=tipo,titulo=titulo,mensaje=mensaje)
                    self.navegar.ir_a_ventana("login")
        except Exception as e:
            print(f"Error critico: {e}")
            self.navegar.ir_a_ventana("login")

    def message_box_datos_faltantes(self, mensaje):
        self.mb.message_box(self, "info", "Faltan datos", mensaje)

    def cantidad_consultorio_duplicado(self, lista_dato):
        cantidad_consultorio = GCS.encontrar_duplicados_consultorio(self.db, lista_dato)
        if cantidad_consultorio:
            return cantidad_consultorio
        else:
            return 0


    def showEvent(self, event):
        super().showEvent(event)
        lista_consultorio= [AIUCSG.obetner_id_consultorio()]
        obtener_datos_rellenar = GCS.obtener_datos_consultorio_modificar(self.db, lista_consultorio)
        if obtener_datos_rellenar:
            label, combo, num = "No encontrado", "1 No Asignado", "000"
            print("datos obtenidos: ", obtener_datos_rellenar)
            self.le_nombre_consultorio.setText(obtener_datos_rellenar.get("Nombre", label))
            self.le_calle.setText(obtener_datos_rellenar.get("Calle",label ))
            self.le_num_exterior.setText(obtener_datos_rellenar.get("Num_Ext", num))
            self.le_num_interior.setText(obtener_datos_rellenar.get("Num_Int", num))
            self.le_localidad.setText(obtener_datos_rellenar.get("Localidad", label))
            self.le_cp.setText(obtener_datos_rellenar.get("CP", num))
            self.le_municipio.setText(obtener_datos_rellenar.get("Municipio", label))
            self.le_colonia.setText(obtener_datos_rellenar.get("Colonia", label))
            self.le_telefono.setText(obtener_datos_rellenar.get("Tel_Uno", num))
            self.le_telefono_dos.setText(obtener_datos_rellenar.get("Tel_Dos", num))
            estado_txt = obtener_datos_rellenar.get("Estado", combo)

            indice_estado_encontrado = 0
            for i in range(self.cb_estado.count()):
                texto_item = self.cb_estado.itemText(i)
                id_item = GSS.obtener_solo_numeros(texto_item)
                if str(id_item) == str(estado_txt):
                    indice_estado_encontrado = i
                    break
            self.cb_estado.setCurrentIndex(indice_estado_encontrado)
        else:
            print("No se cargaron los datos")
