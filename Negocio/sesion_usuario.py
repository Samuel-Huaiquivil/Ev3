# Iniciar la sesión del usuario

from Datos.conexion import sesion_db
from Modelos.registro import Registro
import bcrypt

def iniciar_sesion(nombre_usuario, contrasena):
    # Lógica para iniciar sesión del usuario
    print(f"Iniciando sesión para el usuario: {nombre_usuario}")
    usuario = sesion_db.query(Registro).filter_by(nombre_usuario=nombre_usuario).first()
    if usuario is None:
        print("Usuario no encontrado.")
        return False
    if bcrypt.checkpw(contrasena.encode('utf-8'), usuario.contrasena.encode('utf-8')):
        print("Inicio de sesión exitoso.")
        return True
    else:
        print("Contraseña incorrecta.")
        return False