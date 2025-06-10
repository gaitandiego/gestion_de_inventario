from sqlalchemy.orm import Session
from app.models.cliente import Cliente
from app.schemas.cliente import ClienteCreate

class ClienteDAO:
    def __init__(self, db: Session):
        self.db = db

    def crear_cliente(self, cliente_data: ClienteCreate) -> Cliente:
        nuevo_cliente = Cliente(**cliente_data.dict())
        self.db.add(nuevo_cliente)
        self.db.commit()
        self.db.refresh(nuevo_cliente)
        return nuevo_cliente

    def listar_clientes(self):
        return self.db.query(Cliente).all()

    def actualizar_cliente(self, cliente_id: int, datos_actualizados: ClienteCreate):
        cliente = self.db.query(Cliente).filter(Cliente.ID_Cliente == cliente_id).first()
        if cliente:
            for campo, valor in datos_actualizados.dict().items():
                setattr(cliente, campo, valor)
            self.db.commit()
            self.db.refresh(cliente)
        return cliente
