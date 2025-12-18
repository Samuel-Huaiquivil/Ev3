# Funcion para insertar datos


from Datos.session import get_session

def insertar_datos(modelo):
    with get_session() as session:
        session.add(modelo)
        session.commit()