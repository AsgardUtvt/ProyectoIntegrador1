# Se importan liberrias
import crypt


class Encrypt:
    def __init__(self, password):
        self._password = password
    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,password):
        if not password and password.strip():
            return  "La cadena esta vacia"
        else:
            



