from Login.LoginController import router as login_router
from Documentacion.EjemploApi import router as doc_router
from Usuario.UsuarioController import router as us_router
import sys
import os.path

if __package__ is None and not getattr(sys, 'frozen', False):
    # Obtiene la ruta absoluta de este main.py
    path = os.path.realpath(os.path.abspath(__file__))
    # Agrega la carpeta raíz actual (ProyectoIntegrador1) a sys.path
    sys.path.insert(0, os.path.dirname(path))
pp.include_router(login_router)
app.include_router(doc_router)
app.include_router(us_router)

if __name__ == '__main__':
