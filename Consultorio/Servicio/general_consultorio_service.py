from BaseDatos.MySqlManager import MySqlManager

class General_Consultorio_Service:

    @staticmethod
    def obtener_estado(db: MySqlManager) -> tuple:
        try:
            with db.obtener_cursor() as cursor:
                sql_select_estado = "SELECT CONCAT(id_estado,' ', estado) AS 'concat' FROM Estado ORDER BY id_estado;"
                cursor.execute(sql_select_estado)
                resultado = cursor.fetchall()
                resultado_tupla = tuple(resultado)
                return resultado_tupla
        except Exception as e:
            print(f"Error critico: {e}")
            return ()

    @staticmethod
    def encontrar_duplicados_consultorio(db: MySqlManager, dato: list):
        try:
            with db.obtener_cursor() as cursor:
                sql_select_duplicados_consultorio = "SELECT COUNT(consultorio_name) AS 'cantidad_consultorio' FROM Consultorio WHERE consultorio_name LIKE %s;"
                cursor.execute(sql_select_duplicados_consultorio, dato)
                resultado_cantida_consultorio = cursor.fetchone()
                return resultado_cantida_consultorio.get("cantidad_consultorio") if resultado_cantida_consultorio else None
        except Exception as e:
            print(f"Error critico: {e}")
            return {}
