# Actualizar datos del usuario en la base de datos

from Datos.conexion import get_session
from Modelos.usuario import Usuario

def actualizar_datos_usuario(user_id, nuevo_nombre=None, nuevo_email=None, nuevo_telefono=None, nuevo_sitio_web=None):
    try:
        with get_session() as session:
            usuario = session.query(Usuario).filter_by(id=user_id).first()
            if not usuario:
                print(f"No se encontró un usuario con ID {user_id}.")
                return
            
            if nuevo_nombre:
                usuario.nombre = nuevo_nombre
            if nuevo_email:
                usuario.email = nuevo_email
            if nuevo_telefono:
                usuario.telefono = nuevo_telefono
            if nuevo_sitio_web:
                usuario.sitio_web = nuevo_sitio_web
            
            session.commit()
            print("Datos del usuario actualizados correctamente.")
    except Exception as e:
        print(f"Error al actualizar datos del usuario: {e}")