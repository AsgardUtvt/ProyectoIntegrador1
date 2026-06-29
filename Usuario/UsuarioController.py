from fastapi import APIRouter
from .DTOs.UsuarioDTO import UsuarioDTO
from Login.Functions.Encrypt import Encrypt
router = APIRouter()
en = Encrypt()

@router.post("/api/generar/usuario/")
def registrar_usuario(udto: UsuarioDTO)-> dict:
    pass_hash = en.generate_password_hash(udto.password)
    lenght = len(pass_hash)
    return {
        "hash": pass_hash,
        "tamaño": lenght
    }
