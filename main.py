import uvicorn
from fastapi import FastAPI
from Login.LoginController import router as login_router
from Documentacion.EjemploApi import router as doc_router
import sys
import os.path

if __package__ is None and not getattr(sys, 'frozen', False):
    # Obtiene la ruta absoluta de este main.py
    path = os.path.realpath(os.path.abspath(__file__))
    # Agrega la carpeta raíz actual (ProyectoIntegrador1) a sys.path
    sys.path.insert(0, os.path.dirname(path))
app = FastAPI()
app.include_router(login_router)
app.include_router(doc_router)

if __name__ == '__main__':
    HOST = "127.0.0.1"
    PORT = 8000
    RELOAD = True
    uvicorn.run("main:app", host=HOST, port=PORT, reload=RELOAD)
