from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Semaforo(Base):
    __tablename__ = 'semaforo'

    id = Column(Integer, primary_key=True)
    ubicacion = Column(String(100))
    estado = Column(String(100))
    tipo = Column(String(100))
    id_mina = Column(Integer, ForeignKey('mina.id'))
    mina = relationship("Mina", backref="semaforos")