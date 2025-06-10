from pydantic import BaseModel
from typing import Optional

class ClienteBase(BaseModel):
    Nombre: str
    Contacto: Optional[str] = None

class ClienteCreate(ClienteBase):
    pass

class ClienteOut(ClienteBase):
    ID_Cliente: int

    class Config:
        orm_mode = True

