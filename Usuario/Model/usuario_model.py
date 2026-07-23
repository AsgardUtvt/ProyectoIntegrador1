''' Se importan clases a utilizar '''
from almacendar_id_us_con import Almacenar_Id_Usuario_Consultorio_SG as AIUCSG
from BaseDatos.MySqlManager import MySqlManager

class Usuario_Model:
    ''' Se genera una clase model para entidad Usuario de la base '''
    def __init__(
        self,
        name: str,
        paterno: str,
        materno: str,
        password: str,
        cedula_profesional: str,
        cedula_especialidad: str,
        id_tipo_usuario: int,
        id_consultorio: int,
        id_esucela: int ) -> None:

        self.name = name
        self.paterno = paterno
        self.materno = materno
        self.password = password
        self.cedula_profesional = cedula_profesional
        self.cedula_especialidad = cedula_especialidad
        self.id_tipo_usuario = id_tipo_usuario
        self.id_consultorio = id_consultorio
        self.id_esucela = id_esucela

    def crear_usuario(self, db: MySqlManager):
        '''
        Para usar esta funcion se necesita cerar el consturcto de la clase
        '''
        try:
            with db.obtener_cursor()  as cursor:
                sql_instert = "INSERT INTO Usuario(usuario_name, usuario_paterno, usuario_materno, usuario_password, usuario_cedula_profesional, usuario_cedula_especialidad, id_tipo_usuario, id_consultorio, id_escuela) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql_instert, )
                user = cursor.lastrowid
                AIUCSG.agregar_id("use", user)
                print(AIUCSG.obtener_id())
        except Exception as e:
            print(f"Error critio: {e}")
