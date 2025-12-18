from Datos.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    nombre_usuario = Column(String(100), nullable=False)
    correo = Column(String(255), nullable=False)
    telefono = Column(String(100))
    web = Column(String(255))
    
    #Fk
    compania_id = Column(Integer, ForeignKey('companias.id'))
    compania = relationship("Compania")
    tareas = relationship("Tarea", back_populates="usuario")
    direcciones = relationship("Direccion", back_populates="usuario")
    