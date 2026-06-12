
from pydantic import BaseModel


class LoginDTO(BaseModel):
    usuario: str
    password: str

