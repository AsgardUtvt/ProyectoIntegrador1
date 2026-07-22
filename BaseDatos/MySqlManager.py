from contextlib import contextmanager
from typing import Any, ContextManager, Generator

import pymysql
from BaseDatos.DataBaseInterface import DataBaseInterface


class MySqlManager(DataBaseInterface):


    def open_db(self):
        if not self.conexion:
            self.conexion = pymysql.connect(**self.config)
            print("conexion exitosa")

    def close_db(self):
        if self.conexion:
            self.conexion.close()

    @contextmanager
    def obtener_cursor(self) :
        if not self.conexion:
            raise pymysql.OperationalError
        cursor = self.conexion.cursor(pymysql.cursors.DictCursor)
        try:
            yield cursor
        finally:
            cursor.close()
            print("Se cerro la conexion atumaticamente")

    def commit_conexion(self):
       self.conexion.commit()
