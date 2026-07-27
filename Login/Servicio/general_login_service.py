
from almacendar_id_us_con import Almacenar_Id_Usuario_Consultorio_SG as AIUCSG 
from BaseDatos.MySqlManager import MySqlManager


class General_Login_Service:

    @staticmethod
    def obtener_password_hash_db(db: MySqlManager, lista_nombre: list):
        try:
            with db.obtener_cursor() as cursor:
                sql_select_password = "SELECT u.usuario_password AS 'password_hash' FROM Usuario u WHERE BINARY u.usuario_name LIKE %s;"
                cursor.execute(sql_select_password, lista_nombre)
                resultado_password_hash = cursor.fetchone()
                return resultado_password_hash["password_hash"] if resultado_password_hash else None
        except Exception as e:
            print(f"Error critico: {e}")

    @staticmethod
    def obtener_id_tipo_usuario_consultrio(db: MySqlManager, usuario: list):
        with db.obtener_cursor() as cursor:
            sql_select_tipo_usuario_consultrio = "SELECT id_tipo_usuario AS 'Tipo_Usuario', id_consultorio AS 'Consultorio' FROM Usuario WHERE BINARY usuario_name LIKE %s;"
            cursor.execute(sql_select_tipo_usuario_consultrio, usuario)
            resultado_usuario_consultrio = cursor.fetchone()
            if resultado_usuario_consultrio:
                AIUCSG.agregar_id_usuario(resultado_usuario_consultrio.get("Tipo_Usuario", 0))
                AIUCSG.agregar_id_consultorio(resultado_usuario_consultrio.get("Consultorio", 0))
                print(AIUCSG.obetner_id_consultorio(), AIUCSG.obtener_id_usuario())
            else:
                print(f"No tiene nada el {resultado_usuario_consultrio}")

