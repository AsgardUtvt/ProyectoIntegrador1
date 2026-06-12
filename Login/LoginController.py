from fastapi import APIRouter
from pydantic import BaseModel
from .DTOs.LoginDTO import LoginDTO
from .Functions.LoginFunction import LoginFunction
router = APIRouter()
lf = LoginFunction()
@router.post("/api/login/")

def login(ldto: LoginDTO):
    if lf.validar_datos(ldto.usuario) or lf.validar_datos(ldto.password):
        return {"mensaje": "usuario o contraseña invalidos"}
    else:
        return {"mensaje": "inicio session exitosa"}
