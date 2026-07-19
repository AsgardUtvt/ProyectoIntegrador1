from fastapi import APIRouter
from .DTOs.LoginDTO import LoginDTO
from .Functions.LoginFunction import LoginFunction
from .Functions.Encrypt import Encrypt
router = APIRouter()
lf = LoginFunction()
en = Encrypt()
@router.post("/api/login/")

def login(ldto: LoginDTO):
    if not lf.validar_datos(ldto.usuario) and not lf.validar_datos(ldto.password):
        hash_bd = "$argon2id$v=19$m=65536,t=3,p=4$tnuaw4NCHGH4acRZ4ktIzA$tF7W/SSvnw8yqIGSNRQWhoWuiDPsO/zhXfG3oOOMLUg"
        if en.parssword_hash(hash_bd, ldto.password):
            return {"ok": "inicio de sesion exitoso"}
        else:
            return {"error": "Usuario no encontrado"}

    else:
        return {"error": "hubo un problema al iniciar sesion"}
