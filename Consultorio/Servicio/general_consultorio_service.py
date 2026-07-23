from BaseDatos.MySqlManager import MySqlManager

class General_Consultorio_Service:

    @staticmethod
    def obtener_estado(db: MySqlManager) -> tuple:
        try:
            with db.obtener_cursor() as cursor:
                sql_select = "SELECT CONCAT(id_estado,' ', estado) AS 'concat' FROM Estado ORDER BY id_estado;"
                cursor.execute(sql_select)
                resultado = cursor.fetchall()
                cursor.close()
                resultado_tupla = tuple(resultado)
                return resultado_tupla
        except Exception as e:
            print(f"Error critico: {e}")
            return ()
