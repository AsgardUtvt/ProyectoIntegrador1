# Se importar librerias a usar
from os import stat

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
                slq_select_propietario = "SELECT id_tipo_usuario AS 'Propietario' FROM Tipo_Usuario WHERE tipo_usuario LIKE 'P%ropietario';"
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

    @staticmethod
    def obtener_datos_usuario_modificar(db: MySqlManager, id_usuario_consultorio: list):
        try:
            with db.obtener_cursor() as cursor:
                sql_select_datos_usuario = "SELECT usuario_name AS 'Nombre', usuario_paterno AS 'Paterno', usuario_materno AS 'Materno', usuario_cedula_profesional 'Cedula_Profesional', usuario_cedula_especialidad AS 'Cedula_Especialidad', id_tipo_usuario AS 'Tipo_Usuario', id_escuela AS 'Escuela' FROM Usuario WHERE id_usuario = %s AND id_consultorio = %s;"
                cursor.execute(sql_select_datos_usuario, id_usuario_consultorio)
                resultado_datos_usuario = cursor.fetchone()
                return resultado_datos_usuario if resultado_datos_usuario else None
        except Exception as e:
            print(f"Error critico: {e}")

    @staticmethod
    def obtener_todos_usuarios_consultorio(db: MySqlManager, id_consultorio_todos: int):
        try:
            with db.obtener_cursor() as cursor:
                sql_select_todos_usuarios_consultorio = "SELECT id_usuario AS 'id_val', CONCAT_WS(' ', usuario_name, usuario_paterno, usuario_materno) AS 'nombre' FROM Usuario WHERE id_consultorio = %s;"
                cursor.execute(sql_select_todos_usuarios_consultorio, (id_consultorio_todos,))
                resultado_todos_usuario_consultorio = cursor.fetchall()
                return resultado_todos_usuario_consultorio if resultado_todos_usuario_consultorio else {}
        except Exception as e:
            print(f"Erro critico: {e}")
            return {}

