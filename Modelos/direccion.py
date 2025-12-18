from Datos.base import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

class Direccion(Base):
    __tablename__ = 'direcciones'

    id = Column(Integer, primary_key=True, autoincrement=True)
    calle = Column(String(255))
    departamento = Column(String(100))
    ciudad = Column(String(100))
    codigo_postal = Column(String(50))
    lat = Column(String(50))
    lng = Column(String(50))

    #Fk
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    usuario = relationship("Usuario", back_populates="direcciones")

    def __repr__(self):
        return f"<Direccion(id={self.id}, calle='{self.calle}', ciudad='{self.ciudad}')>"
    def actualizar(self, calle=None, departamento=None, ciudad=None, codigo_postal=None, lat=None, lng=None):
        if calle is not None:
            self.calle = calle
        if departamento is not None:
            self.departamento = departamento
        if ciudad is not None:
            self.ciudad = ciudad
        if codigo_postal is not None:
            self.codigo_postal = codigo_postal
        if lat is not None:
            self.lat = lat
        if lng is not None:
            self.lng = lng