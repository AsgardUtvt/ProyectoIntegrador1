import sys
import os
from PyQt6.QtWidgets import QApplication

# Agregar ruta para imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ventana_pasaporte import Ventana_Pasaporte

class MySQLManager:
    def __init__(self, config):
        import pymysql
        self.config = config
        self.conexion = pymysql.connect(**config, autocommit=True)

    def obtener_cursor(self):
        import pymysql
        return self.conexion.cursor(pymysql.cursors.DictCursor)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'plagg',
        'database': 'sihmed',
        'port': 3306
    }

    try:
        db = MySQLManager(db_config)
        ventana = Ventana_Pasaporte(db=db)
        ventana.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"Error al iniciar la prueba del pasaporte: {e}")
        