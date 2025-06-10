from app.database import Base, engine
from app.models.cliente import Cliente

# Si tienes más modelos (Producto, Venta, etc.), impórtalos aquí también.

# Crear todas las tablas definidas en los modelos importados
Base.metadata.create_all(bind=engine)

print("✅ Tablas creadas exitosamente.")
