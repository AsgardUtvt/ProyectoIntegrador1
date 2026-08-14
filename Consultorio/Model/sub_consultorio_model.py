from pymysql import MySQLError, cursors

from BaseDatos.MySqlManager import MySqlManager
from almacendar_id_us_con import Almacenar_Id_Usuario_Consultorio_SG as AIUCSG

class Sub_Consultorio_Model:

    def __init__(self,
                 c_name: str,
                 c_calle: str,
                 c_colonia: str,
                 c_num_exterior: str,
                 c_num_interior: str,
                 c_localidad: str,
                 c_id_estado: int,
                 c_telefono: str,
                 c_telefono_dos: str,
                 c_municipio: str ,
                 c_cp: str) -> None:
        self.consultorio_name = c_name
        self.consultorio_calle = c_calle
        self.consultorio_colonia = c_colonia
        self.consultorio_num_exterior = c_num_exterior
        self.consultorio_num_interior = c_num_interior
        self.consultorio_localidad = c_localidad
        self.id_estado = c_id_estado
        self.consultorio_telefono = c_telefono
        self.consultorio_telefono_dos = c_telefono_dos
        self.consultorio_municipio = c_municipio
        self.consultorio_cp = c_cp

        self.tupla_datos = (
            self.consultorio_name,
            self.consultorio_calle,
            self.consultorio_colonia,
            self.consultorio_num_exterior,
            self.consultorio_num_interior,
            self.consultorio_localidad,
            self.consultorio_telefono,
            self.consultorio_telefono_dos,
            self.consultorio_cp,
            self.consultorio_municipio,
            self.id_estado,
            AIUCSG.obetner_id_consultorio()
                       )

    def insertar_datos(self, db: MySqlManager) -> bool:
        try:
            with db.obtener_cursor() as cursor:
                sql_insert = """
INSERT INTO Sub_Consultorio(
sub_consultorio_name,
sub_consultorio_calle,
sub_consultorio_colonia,
sub_consultorio_num_exterior,
sub_consultorio_num_interior,
sub_consultorio_localidad,
sub_consultorio_telefono,
sub_consultorio_telefono_dos,
sub_consultorio_cp,
sub_consultorio_municipio,
id_estado,
id_consultorio
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """
                print(f"sub_consultorio tupla_datos: {self.tupla_datos}")
                cursor.execute(sql_insert, self.tupla_datos)
                db.commit_conexion()
            return True
        except Exception as e:
            print(f"Erorr critico: {e}")
            return False


    @staticmethod
    def actualizar_datos( db: MySqlManager, name_update, calle_update, colonia_update, num_ext_update, num_int_update, localidad_update, id_estado_update, tel_update, tel_dos_update, municipio_update, cp_update) -> bool:
        __TUPLA_ACTUALIZAR = (
            name_update,
            calle_update,
            colonia_update,
            num_ext_update,
            num_int_update,
            localidad_update,
            id_estado_update,
            tel_update,
            tel_dos_update,
            municipio_update,
            cp_update,
            AIUCSG.obetner_id_consultorio()
        )
        try:
            with db.obtener_cursor() as cursor:
                slq_update_consultorio = """
UPDATE Sub_Consultorio
SET sub_consultorio_name = %s,
    sub_consultorio_calle = %s,
    sub_consultorio_colonia = %s,
    sub_consultorio_num_exterior = %s,
    sub_consultorio_num_interior = %s,
    sub_consultorio_localidad = %s,
    id_estado = %s,
    sub_consultorio_telefono = %s,
    sub_consultorio_telefono_dos = %s,
    sub_consultorio_municipio = %s,
    sub_consultorio_cp = %s
WHERE id_consultorio = %s;

                """
                cursor.execute(slq_update_consultorio, __TUPLA_ACTUALIZAR)
                db.commit_conexion()
            return True
        except Exception as e:
            print(f"Error critico: {e}")
            return False
    @staticmethod
    def eliminar_sub_consultorio(db: MySqlManager, consultorio_sub_lisa: list):
        """ Mandar una lista con el orden id_consultorio y id_sub_consultorio  """
        try:
            with db.obtener_cursor() as cursor:
                sql_delete_sub_consultorio = "DELETE FROM Sub_Consultorio WHERE id_consultorio = %s AND id_sub_consultorio = %s"
                cursor.execute(sql_delete_sub_consultorio, consultorio_sub_lisa)
                db.commit_conexion()
                return True
        except Exception as e:
            print(f"Error: {e}")
            return False


