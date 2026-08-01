from BaseDatos.MySqlManager import MySqlManager
from almacendar_id_us_con import Almacenar_Id_Usuario_Consultorio_SG as AIUCSG

class General_Contrasena_Service:

    @staticmethod
    def actualizar_contraseña(db: MySqlManager, pswr: str):
        _DATOS_UPDATE = (
            pswr,
            AIUCSG.obtener_id_usuario(),
            AIUCSG.obetner_id_consultorio()
        )
        print(_DATOS_UPDATE)
        try:
            with db.obtener_cursor() as cursor:
                sql_update_password = """
                    UPDATE Usuario
                    SET usuario_password = %s
                    WHERE id_usuario = %s AND id_consultorio = %s;
                    """
                cursor.execute(sql_update_password, _DATOS_UPDATE)
                db.commit_conexion()
                return True
        except Exception as e:
            print(f"Erro: {e}")
            return False

