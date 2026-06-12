class LoginFunction:
    def validar_datos(self, value:str):
        if not value.strip():
            return True
