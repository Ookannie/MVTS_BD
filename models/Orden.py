from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Orden(Base):
    __tablename__ = 'orden'

    id = Column(Integer, primary_key=True)
    fecha_hora = Column(DateTime)
    cantidad = Column(Numeric)
    estado = Column(String(100))
    id_vehiculo = Column(Integer, ForeignKey('vehiculo.id'))
    vehiculo = relationship("Vehiculo", backref="ordenes")