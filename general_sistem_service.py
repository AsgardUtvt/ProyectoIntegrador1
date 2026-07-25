

<<<<<<< HEAD
from BaseDatos.MySqlManager import MySqlManager


=======
>>>>>>> c2983caab5b8c6a3f8beff40b13f4603256eb540
class General_Sistem_Service:

    @staticmethod
    def obtener_solo_numeros(lista_cosas: str):
        digitos_en = []
        for letras in lista_cosas:
            if letras.isdigit():
                digitos_en.append(letras)
        if digitos_en is None:
<<<<<<< HEAD
            raise ValueError(f"No hay elementos en la lista {digitos_en}")
        else:
            digitos = int("".join(digitos_en))
            return digitos

    @staticmethod
    def validar_si_existe_propietario(db: MySqlManager):
        try:
            with db.obtener_cursor() as cursor:
                slq_select_usuario_existente = "SELECT COUNT(id_tipo_usuario) AS 'cantida_usuarios' FROM Usuario WHERE id_tipo_usuario = 3;"
                cursor.execute(slq_select_usuario_existente)
                cantidad_usuario = cursor.fetchone()
                return cantidad_usuario["cantida_usuarios"] if cantidad_usuario else None
        except Exception as e:
            print(f"Error critico: {e}")

=======
            raise ValueError("No hay elementos en la lista {digitos_en}")
        else:
            digitos = int("".join(digitos_en))
            return digitos
>>>>>>> c2983caab5b8c6a3f8beff40b13f4603256eb540
