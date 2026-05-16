import sys
import os


ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ruta_raiz not in sys.path:
    sys.path.append(ruta_raiz)

try:
    import Config as con


except ImportError:
    print("Error: No se encontró Config.py en la carpeta superior.")
    sys.exit(1)

class Conexion:

    def __init__(self):
        self.host = con.DB_HOST
        self.name = con.DB_NAME
        self.user = con.DB_USER
        self.passw = con.DB_PASS
        self.__conectionString = ""

    def OpenBD(self):
        print("Encendiendo conexion a base de datos")

    def CloseBD(self):
        print("Cerrando conexion a base de datos")
