from os import stat

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
                sql_select_duplicados_consultorio = "SELECT COUNT(consultorio_name) AS 'cantidad_consultorio' FROM Consultorio WHERE BINARY consultorio_name LIKE %s;"
                cursor.execute(sql_select_duplicados_consultorio, dato)
                resultado_cantida_consultorio = cursor.fetchone()
                print("Cantidad consutlorio: ",resultado_cantida_consultorio)
                return resultado_cantida_consultorio.get("cantidad_consultorio") if resultado_cantida_consultorio else None
        except Exception as e:
            print(f"Error critico: {e}")
            return {}

    @staticmethod
    def obtener_datos_consultorio_modificar(db: MySqlManager, consul_lista: list):
        try:
            with db.obtener_cursor() as cursor:
                sql_select_datos_consultorio = "SELECT consultorio_name AS 'Name', consultorio_calle AS 'Calle', consultorio_colonia AS 'Colonia', consultorio_num_exterior AS 'Num_Ext', consultorio_num_interior AS 'Num_Int', id_estado AS 'Estado', consultorio_telefono AS 'Tel_Uno', consultorio_telefono_dos AS 'Tel_Dos', consultorio_municipio AS 'Municipio', consultorio_cp AS 'CP', consultorio_localidad AS 'Localidad' FROM Consultorio WHERE id_consultorio = %s;"
                cursor.execute(sql_select_datos_consultorio, consul_lista)
                reusltado_datos_consultorio = cursor.fetchone()
                return reusltado_datos_consultorio if reusltado_datos_consultorio else {}
        except Exception as e:
            print(f"Eror: {e}")
            return {}

    @staticmethod
    def obtener_datos_sub_conusltorio_modificar(db: MySqlManager, sub_consul_consult_ids: list):
        """ Pasar como parametros en lista id_consultorio y id_sub_consultorio  """
        try:
            with db.obtener_cursor() as cursor:
                sql_select_datos_sub_consultorio = """
SELECT
    sc.sub_consultorio_name AS 'S_NAME',
    sc.sub_consultorio_calle AS 'S_CALLE',
    sc.sub_consultorio_colonia AS 'S_COLONIA',
    sc.sub_consultorio_num_interior AS 'S_INT',
    sc.sub_consultorio_num_exterior AS 'S_EXT',
    sc.sub_consultorio_telefono AS 'S_TEL',
    sc.sub_consultorio_telefono_dos AS 'S_TEL_DOS',
    sc.sub_consultorio_cp AS 'S_CP',
    sc.sub_consultorio_municipio AS 'S_MUN',
    sc.id_estado AS 'S_EST'
FROM Sub_Consultorio sc
INNER JOIN Consultorio c
ON c.id_consultorio = sc.id_consultorio
WHERE sc.id_consultorio = %s AND sc.id_consultorio = %s;
                """
                cursor.execute(sql_select_datos_sub_consultorio, sub_consul_consult_ids)
                resultado_datos_sub_consultorio = cursor.fetchone()
                return resultado_datos_sub_consultorio if resultado_datos_sub_consultorio else {}
        except Exception as e:
            print(f"Error: {e} ")
            return {}


    @staticmethod
    def encontrar_duplicados_sub_consultorio(db: MySqlManager, dato: list):
        try:
            with db.obtener_cursor() as cursor:
                sql_select_duplicados_sub_consultorio = "SELECT COUNT(sub_consultorio_name) AS 'cantidad_consultorio' FROM Sub_Consultorio WHERE BINARY sub_consultorio_name LIKE %s;"
                cursor.execute(sql_select_duplicados_sub_consultorio, dato)
                resultado_cantida_consultorio = cursor.fetchone()
                print("Cantidad consutlorio: ",resultado_cantida_consultorio)
                return resultado_cantida_consultorio.get("cantidad_consultorio") if resultado_cantida_consultorio else None
        except Exception as e:
            print(f"Error critico: {e}")
            return {}

    @staticmethod
    def obtener_consultorio(db: MySqlManager, consultorio_lista: list):
        try:
            with db.obtener_cursor() as cursor:
                sql_select_consultorio = """

SELECT
    id_consultorio AS 'ID',
    consultorio_name AS 'CON'
FROM Consultorio
WHERE id_consultorio = %s;
                """
                cursor.execute(sql_select_consultorio, consultorio_lista)
                resultado_consultorio = cursor.fetchone()
                return resultado_consultorio if resultado_consultorio else {}
        except Exception as e:
            print(f"Error critico: {e}")
            return {}


    @staticmethod
    def obtener_sub_consultorio(db: MySqlManager, consultorio_sub_lista: list):
        """ mandar id_consultorio y id_sub_consultorio """
        try:
            with db.obtener_cursor() as cursor:
                sql_select_consultorio = """

SELECT
    id_sub_consultorio AS 'ID',
    sub_consultorio_name AS 'CON'
FROM Sub_Consultorio
WHERE id_consultorio = %s;
                """
                cursor.execute(sql_select_consultorio, consultorio_sub_lista)
                resultado_consultorio = cursor.fetchall()
                return resultado_consultorio if resultado_consultorio else {}
        except Exception as e:
            print(f"Error critico: {e}")
            return {}
