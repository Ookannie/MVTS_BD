from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Gerente(Base):
    __tablename__ = 'gerente'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    email = Column(String(100))
    fecha_nacimiento = Column(DateTime)
    telefono = Column(String(20))