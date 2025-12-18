# Modelo para registrar usuario con los datos ingresados y la contraseña hasheada
# Usando la librería bcrypt para hashear la contraseña

from sqlalchemy import Column, Integer, String
from Datos.base import Base

class Registro(Base):
    __tablename__ = 'usuarios_registrados'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_usuario = Column(String(100), unique=True, nullable=False)
    contrasena = Column(String(255), nullable=False)
    telefono = Column(String(20), nullable=True)

    def __init__(self, nombre_usuario, contrasena, telefono=None):
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.telefono = telefono

    def __repr__(self):
        return f"<Registro(nombre_usuario='{self.nombre_usuario}', telefono='{self.telefono}')>"

