from sqlalchemy import Column, Integer, DateTime, ForeignKey
from app.database import Base

class Cita(Base):
    __tablename__ = "citas"

    id = Column(Integer, primary_key=True, index=True)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    servicio_id = Column(Integer, ForeignKey("servicios.id"))
    fecha = Column(DateTime)
    