from abc import ABC, abstractmethod
from contextlib import contextmanager
from typing import Any, Generator
class DataBaseInterface(ABC):

    def __init__(self, config) -> None:
        self.config = config
        self.conexion = None

    @abstractmethod
    def open_db(self):
        ''' Metodo para abrir una conexion '''
        pass

    @abstractmethod
    def close_db(self):
        ''' Metodo para cerrar una conexion '''
        pass

    @contextmanager
    @abstractmethod
    def obtener_cursor(self) -> Generator[Any, None, None]:
        yield

    @abstractmethod
    def commit_conexion(self):
        ''' Metodo para confirmar que se guardaron los datos '''
        pass
