import os
import sys

# Mantener tu configuración de rutas (opcional pero funcional)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import APIRouter

# Instanciamos la aplicación de FastAPI
router = APIRouter()

# Endpoint 1: Mensaje de bienvenida
@router.get("/api/ejemplo/")
def mensaje_bienvenida():
    return {"mensaje": "Este es un mensaje de bienvenida"}

# Endpoint 2: Saludar usuario
@router.get("/api/saludar/{nombre_usuario}")
def saludar_usuario(nombre_usuario: str):
    return {"mensaje": f"Bienvenido {nombre_usuario}"}
@router.post("/api/suma/")
def suma(a:int, b:int):
    sum = a + b 
    return {"mensaje": f"{sum}"}
