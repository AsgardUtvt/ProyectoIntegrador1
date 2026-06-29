from pydantic import BaseModel

class UsuarioDTO(BaseModel):
    nombre: str
    ap_paterno: str
    ap_materno: str
    password: str
