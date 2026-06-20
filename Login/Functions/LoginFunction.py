class LoginFunction:
    def validar_datos(self, value:str):
        if not value.strip():
            return True
        else:
            return False

    def obtener_datos(self, usuario:str, contraseña:str):
        if self.validar_datos(usuario):
            return {"mensaje": "El usuario es invalido"}
        elif self.validar_datos(contraseña):
            return {"mensaje": "La contraseña es invalido"}
        else:
            return {"mesaje": "Datos no encontrados"}

