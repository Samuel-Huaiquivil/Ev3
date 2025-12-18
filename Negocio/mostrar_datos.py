# Mostrar los datos almacenados en la base de datos usando PrettyTable

from Datos.conexion import get_session
from Modelos.usuario import Usuario
from Modelos.compania import Compania
from Modelos.direccion import Direccion
from Modelos.tarea import Tarea
from prettytable import PrettyTable


def mostrar_datos_compania():
    with get_session() as session:
        companias = session.query(Compania).all()
        tabla = PrettyTable()
        tabla.field_names = ["ID", "Nombre", "Slogan", "Servicio"]
        for compania in companias:
            tabla.add_row([compania.id, compania.nombre, compania.slogan, compania.servicio])
        print("=== Compañías ===")
        print(tabla)

def mostrar_datos_direccion():
    with get_session() as session:
        direcciones = session.query(Direccion).all()
        tabla = PrettyTable()
        tabla.field_names = ["ID", "Calle", "Departamento", "Ciudad", "Código Postal"]
        for direccion in direcciones:
            tabla.add_row([direccion.id, direccion.calle, direccion.departamento, direccion.ciudad, direccion.codigo_postal])
        print("=== Direcciones ===")
        print(tabla)

def mostrar_datos_usuario():
    with get_session() as session:
        usuarios = session.query(Usuario).all()
        tabla = PrettyTable()
        tabla.field_names = ["ID", "Nombre", "Nombre de Usuario", "Correo Electrónico", "Telefono", "Web", "Compañía ID"]
        for usuario in usuarios:
            tabla.add_row([usuario.id, usuario.nombre, usuario.nombre_usuario, usuario.correo, usuario.telefono, usuario.web, usuario.compania_id ])
        print("=== Usuarios ===")
        print(tabla)

def mostrar_datos_tarea():
    with get_session() as session:
        tareas = session.query(Tarea).all()
        tabla = PrettyTable()
        tabla.field_names = ["ID", "Título", "Completada", "Usuario ID"]
        for tarea in tareas:
            tabla.add_row([tarea.id, tarea.titulo, tarea.completado, tarea.usuario_id])
        print("=== Tareas ===")
        print(tabla)