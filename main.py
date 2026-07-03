from dotenv import load_dotenv
import pymysql
from BaseDatos.MySqlManager import MySqlManager
import sys
import os.path
import os

if __package__ is None and not getattr(sys, 'frozen', False):
    # Obtiene la ruta absoluta de este main.py
    path = os.path.realpath(os.path.abspath(__file__))
    # Agrega la carpeta raíz actual (ProyectoIntegrador1) a sys.path
    sys.path.insert(0, os.path.dirname(path))

def main():
    load_dotenv()
    config = {
        "user": os.getenv('DB_USER'),
        "password": os.getenv('DB_PASS'),
        "host": os.getenv("DB_HOST"),
        "port": int(os.getenv("DB_PORT")),
        "database": os.getenv('DB_NAME'),
        "cursorclass": pymysql.cursors.DictCursor
    }
    db = MySqlManager(config)
    print(config)
    try:
        db.open_db()
        print("Hay conexion a base de datos")
    except Exception as e:
        print(f"Error critico: {e}")



if __name__ == '__main__':
    main()
