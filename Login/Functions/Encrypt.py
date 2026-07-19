# Se importan librerias

from dataclasses import dataclass
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
ph = PasswordHasher()


@dataclass
class Encrypt:
    '''
    Para encriptar contraseñas que esten en texto plano
    '''

    def find_parssword_hash(self, hash_bd: str, password: str) -> bool:
        '''
        Comprobar si existe una contraseña en la base de datos.
        '''
        try:
            ph.verify(hash_bd, password)
            return True
        except VerifyMismatchError:
            return False

    def generate_password_hash(self, password: str) -> str:
        '''
        Generar un hash de la contraseña he insertarlo en la base de datos,
        al momento de generar un usuario.
        '''
        hash_psw = ph.hash(password)
        return hash_psw
