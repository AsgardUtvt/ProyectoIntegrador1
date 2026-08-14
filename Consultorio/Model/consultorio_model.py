from BaseDatos.MySqlManager import MySqlManager
from almacendar_id_us_con import Almacenar_Id_Usuario_Consultorio_SG as AIUCSG

class Consultorio_Model:

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

        self.tupla_datos = (self.consultorio_name,
                       self.consultorio_calle,
                       self.consultorio_colonia,
                       self.consultorio_num_exterior,
                       self.consultorio_num_interior,
                       self.consultorio_localidad,
                       self.id_estado,
                       self.consultorio_telefono,
                       self.consultorio_telefono_dos,
                       self.consultorio_municipio,
                       self.consultorio_cp)

    def insertar_datos(self, db: MySqlManager) -> bool:
        try:
            with db.obtener_cursor() as cursor:
                sql_insert = "INSERT INTO Consultorio(consultorio_name, consultorio_calle, consultorio_colonia, consultorio_num_exterior, consultorio_num_interior, consultorio_localidad, id_estado, consultorio_telefono, consultorio_telefono_dos, consultorio_municipio, consultorio_cp) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
                cursor.execute(sql_insert, self.tupla_datos)
            db.commit_conexion()
            consul = cursor.lastrowid
            AIUCSG.agregar_id_consultorio(consul)
            print(AIUCSG.obetner_id_consultorio())
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
UPDATE Consultorio
SET consultorio_name = %s ,
 consultorio_calle = %s,
 consultorio_colonia = %s,
 consultorio_num_exterior = %s,
 consultorio_num_interior = %s,
 consultorio_localidad = %s,
 id_estado = %s,
 consultorio_telefono = %s,
 consultorio_telefono_dos = %s,
 consultorio_municipio = %s,
 consultorio_cp = %s
WHERE id_consultorio = %s;
                """
                cursor.execute(slq_update_consultorio, __TUPLA_ACTUALIZAR)
                db.commit_conexion()
            return True
        except Exception as e:
            print(f"Error critico: {e}")
            return False

