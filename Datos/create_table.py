# Código para ccrear las tablas en la base de datos con los modelos ya establecidos
from Datos.conexion import motor_db
from Datos.base import Base

def crear_tablas():
    '''
    Crea las tablas en la base de datos según los modelos definidos.
    '''
    print("Creando las tablas en la base de datos local")
    Base.metadata.create_all(motor_db)
    print("Tablas creadas exitosamente.")