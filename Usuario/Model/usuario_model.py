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

        self._TUPLA_USUARIO = (
            self.name,
            self.paterno,
            self.materno,
            self.password,
            self.cedula_profesional,
            self.cedula_especialidad,
            self.id_tipo_usuario,
            self.id_consultorio,
            self.id_esucela
        )

    def crear_usuario(self, db: MySqlManager):
        '''
        Para usar esta funcion se necesita cerar el consturcto de la clase
        '''
        try:
            with db.obtener_cursor()  as cursor:
                sql_instert = "INSERT INTO Usuario(usuario_name, usuario_paterno, usuario_materno, usuario_password, usuario_cedula_profesional, usuario_cedula_especialidad, id_tipo_usuario, id_consultorio, id_escuela) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql_instert,self._TUPLA_USUARIO)
                db.commit_conexion()
                user = cursor.lastrowid
                AIUCSG.agergar_id_usuario(user)
                print(AIUCSG.obtener_id_usuario())
                return True
        except Exception as e:
            print(f"Error critio: {e}")
            return False

    @staticmethod
    def eliminar_usuario( db: MySqlManager, id_usuario: list):
        try:
            with db.obtener_cursor() as cursor:
                sql_delete_usuario = "DELETE FROM Usuario WHERE id_usuario = %s;"
                cursor.execute(sql_delete_usuario, id_usuario)
                db.commit_conexion()
                return True
        except Exception as e:
            print(f"Error: {e}")
            return False

    @staticmethod
    def actualizar_datos(db: MySqlManager, name_par: str, paterno_par: str, materno_par: str, cedula_profesional_par: str, cedula_especialidad_par: str, id_tipo_usuario_par: int, id_escuela_par: int, id_usuario_par: int):
        try:
            _TUPLA_USUARIO_ACTUALIZAR = (
                name_par,
                paterno_par,
                materno_par,
                cedula_profesional_par,
                cedula_especialidad_par,
                id_tipo_usuario_par,
                id_escuela_par,
                id_usuario_par
            )
            with db.obtener_cursor() as cursor:
                slq_update_usuario = """
                    UPDATE Usuario
                    SET usuario_name = %s,
                        usuario_paterno = %s,
                        usuario_materno = %s,
                        usuario_cedula_profesional = %s,
                        usuario_cedula_especialidad = %s,
                        id_tipo_usuario = %s,
                        id_escuela = %s
                    WHERE id_usuario = %s
                                     """
                cursor.execute(slq_update_usuario, _TUPLA_USUARIO_ACTUALIZAR)
                db.commit_conexion()
                return True
        except Exception as e:
            print(f"Error: {e}")
            return  False
