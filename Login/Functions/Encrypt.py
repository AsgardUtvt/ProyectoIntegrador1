# Se importan liberrias

from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
ph = PasswordHasher

class Encrypt:
    def __init__(self, password:str):
        self._password = password
    def parssword_hash(self, hash_bd:str):
        try:
            ph.verify(hash_bd, self._password)
            return True
        except VerifyMismatchError:
            return False
