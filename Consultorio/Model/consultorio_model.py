


from BaseDatos.MySqlManager import MySqlManager


class Consultoiro_Model:

    def __init__(self) -> None:
        pass

    def obtener_estados(self, db: MySqlManager):
        pass

    def insertar_datos(self, tupla_datos: tuple, db: MySqlManager):
        try:
            with db.obtener_cursor() as cursor:
                sql_insert = "INSERT INTO Consultorio(consultorio_name, consultorio_calle, consultorio_colonia, consultorio_num_exterior, consultorio_num_interior, consultorio_localidad, id_estado, consultorio_telefono, consultorio_telefono_dos, consultorio_municipio, consultorio_cp) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(sql_insert, tupla_datos)
        except Exception as e:
            print(f"Erorr critico: {e}")
        finally:
            db.commit_conexion()

    def actualizar_datos(self, tupla_datos: tuple, db: MySqlManager):
        pass

