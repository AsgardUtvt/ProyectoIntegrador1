import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from PyQt6.QtWidgets import QApplication
from ventana_crear_recetas import Ventana_Crear_Recetas

class SimuladorNavegar:
    def ir_a_ventana(self, nombre):
        print(f"Navegando a la ventana: {nombre}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Creamos la ventana pasándole None en la BD por ahora
    ventana = Ventana_Crear_Recetas(db=None, navegar=SimuladorNavegar())
    ventana.show()
    
    sys.exit(app.exec())