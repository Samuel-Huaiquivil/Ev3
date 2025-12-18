from Datos.base import Base
from sqlalchemy import Column, Integer, String

class Compania(Base):
    __tablename__ = 'companias'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    eslogan = Column(String(255))
    servicio = Column(String(255))