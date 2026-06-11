import os
import sys

# Mantener tu configuración de rutas (opcional pero funcional)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import FastAPI

# Instanciamos la aplicación de FastAPI
app = FastAPI()

# Endpoint 1: Mensaje de bienvenida
@app.get("/api/")
def mensaje_bienvenida():
    return {"mensaje": "Este es un mensaje de bienvenida"}

# Endpoint 2: Saludar usuario
@app.get("/api/saludar/{nombre_usuario}")
def saludar_usuario(nombre_usuario: str):
    return {"mensaje": f"Bienvenido {nombre_usuario}"}
@app.post("/api/suma/")
def suma(a:int, b:int):
    sum = a + b 
    return {"mensaje": f"{sum}"}
