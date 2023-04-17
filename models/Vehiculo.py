from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Vehiculo(Base):
    __tablename__ = 'vehiculo'

    id = Column(Integer, primary_key=True)
    modelo = Column(String(100))
    placa = Column(String(20))
    ubicacion = Column(String(100))
    estado = Column(String(100))
    id_mina = Column(Integer, ForeignKey('mina.id'))
    conductor_id = Column(Integer, ForeignKey('conductor.id'))
    
    conductor = relationship("Conductor", back_populates="vehiculos")
    mina = relationship("Mina", back_populates="vehiculos")
