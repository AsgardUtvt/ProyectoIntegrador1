

class General_Sistem_Service:

    @staticmethod
    def obtener_solo_numeros(lista_cosas: str):
        digitos_en = []
        for letras in lista_cosas:
            if letras.isdigit():
                digitos_en.append(letras)
        if digitos_en is None:
            raise ValueError("No hay elementos en la lista {digitos_en}")
        else:
            digitos = int("".join(digitos_en))
            return digitos
