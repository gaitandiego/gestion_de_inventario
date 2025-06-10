from sqlalchemy import Column, Integer, String
from app.database import Base

class Cliente(Base):
    __tablename__ = "cliente"

    ID_Cliente = Column(Integer, primary_key=True, index=True)
    Nombre = Column(String(100), nullable=False)
    Contacto = Column(String(100), nullable=True)
