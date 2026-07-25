

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
