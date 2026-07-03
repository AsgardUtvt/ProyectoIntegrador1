# Se importan liberrias

from dataclasses import dataclass
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
ph = PasswordHasher()


@dataclass
class Encrypt:
    ''' Para encriptar contraseñas '''

    def parssword_hash(self, hash_bd: str, password: str) -> bool:
        '''Validar la existencia de la contraseña en la BD'''
        try:
            ph.verify(hash_bd, password)
            return True
        except VerifyMismatchError:
            return False

    def generate_password_hash(self, password: str) -> str:
        '''Para genera has de un usuario e insertarla en la base'''
        hash_psw = ph.hash(password)
        return hash_psw
