from fastapi import APIRouter
from .DTOs.LoginDTO import LoginDTO
from .Functions.LoginFunction import LoginFunction
from .Functions.Encrypt import Encrypt
router = APIRouter()
lf = LoginFunction()
@router.post("/api/login/")

def login(ldto: LoginDTO):
   lf.obtener_datos(ldto.usuario, ldto.password)
   valor = Encrypt(ldto.password)
   hash_bd = "consulta_bd"
   valor.parssword_hash(hash_bd)
