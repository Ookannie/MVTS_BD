from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Mina(Base):
    __tablename__ = 'mina'

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    ubicacion = Column(String(100))
