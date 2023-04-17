from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Congestion(Base):
    __tablename__ = 'congestion'

    id = Column(Integer, primary_key=True)
    fecha_hora = Column(DateTime)
    duracion = Column(Integer)
    id_vehiculo = Column(Integer, ForeignKey('vehiculo.id'))
    id_semaforo = Column(Integer, ForeignKey('semaforo.id'))
    vehiculo = relationship("Vehiculo", backref="congestiones")
    semaforo = relationship("Semaforo", backref="congestiones")