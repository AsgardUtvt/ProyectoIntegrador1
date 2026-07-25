import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PyQt6.QtWidgets import QApplication
from ventana_reportes_caja import Ventana_Reportes_Caja
from BaseDatos.MySqlManager import MySqlManager

class SimuladorNavegar:
    def ir_a_ventana(self, nombre):
        print(f"Navegando a: {nombre}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 🔧 Pasamos los datos de configuración que requiere la clase
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'plagg',       # Pon tu contraseña de MySQL si usas una
        'database': 'sihmed',
        'port': 3306
    }
    
    # Instanciamos pasando el diccionario config
    db = MySqlManager(config)
    
    ventana = Ventana_Reportes_Caja(db=db, navegar=SimuladorNavegar())
    ventana.show()
    
    sys.exit(app.exec())