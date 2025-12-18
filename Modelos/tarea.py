from Datos.base import Base
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Tarea(Base):
    __tablename__ = 'tareas'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    completado = Column(Boolean, default=False) 

    #FK
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    usuario = relationship("Usuario", back_populates="tareas")

