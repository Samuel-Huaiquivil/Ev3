# Obtener los datos desde JSON PlaceHolder y almacenarlos en la base de datos mostrando los resultados

import requests
from Datos.conexion import get_session
from Modelos.usuario import Usuario
from Modelos.compania import Compania
from Modelos.direccion import Direccion
from Modelos.tarea import Tarea

# Urls para la conexión

URL_USUARIOS = "https://jsonplaceholder.typicode.com/users"
URL_TAREAS = "https://jsonplaceholder.typicode.com/todos"

def obtener_datos_almacenar_compania():
    try:
        response = requests.get(URL_USUARIOS)
        response.raise_for_status()
        usuarios_data = response.json()

        with get_session() as session:
            for usuario in usuarios_data:
                compania_data = usuario.get("company", {})
                compania = Compania(
                    nombre=compania_data.get("name"),
                    eslogan=compania_data.get("catchPhrase"),
                    servicio=compania_data.get("bs")
                )
                session.add(compania)
            session.commit()
        print("Compañías almacenadas correctamente.")
    except Exception as e:
        print(f"Error al obtener o almacenar compañías: {e}")

def obtener_datos_almacenar_usuarios():
    try:
        response = requests.get(URL_USUARIOS)
        response.raise_for_status()
        usuarios_data = response.json()

        with get_session() as session:
            for usuario in usuarios_data:
                direccion_data = usuario.get("address", {})
                direccion = Direccion(
                    calle=direccion_data.get("street"),
                    departamento=direccion_data.get("suite"),
                    ciudad=direccion_data.get("city"),
                    codigo_postal=direccion_data.get("zipcode")
                )
                session.add(direccion)
                session.flush()  # Obtener el ID de la dirección recién creada

                usuario_model = Usuario(
                    nombre=usuario.get("name"),
                    nombre_usuario=usuario.get("username"),
                    correo=usuario.get("email"),
                    telefono=usuario.get("phone"),
                    web=usuario.get("website"),
                    direccion_id=direccion.id
                )
                session.add(usuario_model)
            session.commit()
        print("Usuarios almacenados correctamente.")
    except Exception as e:
        print(f"Error al obtener o almacenar usuarios: {e}")

def obtener_datos_almacenar_tareas():
    try:
        response = requests.get(URL_TAREAS)
        response.raise_for_status()
        tareas_data = response.json()

        with get_session() as session:
            for tarea in tareas_data:
                tarea_model = Tarea(
                    titulo=tarea.get("title"),
                    completado=tarea.get("completed"),
                    usuario_id=tarea.get("userId")
                )
                session.add(tarea_model)
            session.commit()
        print("Tareas almacenadas correctamente.")
    except Exception as e:
        print(f"Error al obtener o almacenar tareas: {e}")

def obtener_y_almacenar_todos_los_datos():
    print("Iniciando la obtención y almacenamiento de datos...")
    print("Obteniendo y almacenando compañías...")
    obtener_datos_almacenar_compania()
    print("Obteniendo y almacenando usuarios...")
    obtener_datos_almacenar_usuarios()
    print("Obteniendo y almacenando tareas...")
    obtener_datos_almacenar_tareas()
    print("Proceso completado.")