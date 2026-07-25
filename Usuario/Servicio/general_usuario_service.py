# Se importar librerias a usar
from BaseDatos.MySqlManager import MySqlManager

class General_Usuario_Service:

    @staticmethod
    def obtener_escuela(db: MySqlManager):
        """ Esta función trea las esuclas de la bd a un dict llamado escuela """
        try:
            with db.obtener_cursor() as cursor:
                sql_select_escuela = "SELECT CONCAT(e.id_escuela, ' ', e.escuela_name) AS 'escuela' FROM Escuela AS e ORDER BY e.id_escuela;"
                cursor.execute(sql_select_escuela)
                resultado = cursor.fetchall()
                return tuple(resultado)
        except Exception as e:
            print(f"Erorr critico: {e}")
            return ()

    @staticmethod
    def obtener_tipo_usuario(db: MySqlManager):
        """ Esta función trea los usuario de la base de datos a un dict llamado tipo_usuario """
        try:
            with db.obtener_cursor() as cursor:
                sql_select_tipo_usuario = "SELECT CONCAT(tu.id_tipo_usuario, ' ', tu.tipo_usuario) AS 'tipo_usuario' FROM Tipo_Usuario AS tu;"
                cursor.execute(sql_select_tipo_usuario)
                resultado = cursor.fetchall()
                return tuple(resultado)
        except Exception as e:
            print(f"Error critico: {e}")
            return ()

    @staticmethod
    def obtener_usuario_primeravez(db: MySqlManager):
        """
        Obtiene el id de tipo de usuario Propietario
        """
        try:
            with db.obtener_cursor() as cursor:
                slq_select_propietario = "SELECT id_tipo_usuario AS 'Propietario' FROM Tipo_Usuario WHERE tipo_usuario LIKE 'Propietario';"
                cursor.execute(slq_select_propietario)
                resultado = cursor.fetchone()
                return resultado.get("Propietario") if resultado else None
        except Exception as e:
            print(f"Erorr critico: {e}")
            return None 

    @staticmethod
    def encontrar_duplicados_usuarios(db: MySqlManager, nombre: list):
        try:
            with db.obtener_cursor() as cursor:
                sql_select_duplicados_usuario = "SELECT COUNT(usuario_name) AS 'cantidad_usuario' FROM Usuario WHERE usuario_name LIKE %s;"
                cursor.execute(sql_select_duplicados_usuario, nombre)
                resultado_cantidad_usuario = cursor.fetchone()
                return resultado_cantidad_usuario.get("cantidad_usuario") if resultado_cantidad_usuario else None
        except Exception as e:
            print(f"Error critico {e}")
