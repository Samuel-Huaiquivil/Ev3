# Menú del ingreso de usuario

from Datos import insertar_datos
import Modelos
from Negocio.obtener_datos import obtener_y_almacenar_todos_los_datos


def menu2():
    print("=== Menú del Sistema ===")
    print("1. Obtener datos desde JSON Placeholder")
    print("2. Insertar datos Nuevos")
    print("3. Ver datos almacenados")
    print("4. Actualizar datos existentes")
    print("5. Eliminar datos")
    print("6. Cerrar sesión")
    print("7. Salir del programa")

def opcion_mostrar_datos():
    print("=== Opciones para mostrar datos ===")
    print("1. Mostrar datos de Compañías")
    print("2. Mostrar datos de Direcciones")
    print("3. Mostrar datos de Usuarios")
    print("4. Mostrar datos de Tareas")
    print("5. Volver al menú principal")

def menu_mostrar_datos():
    while True:
        opcion_mostrar_datos()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            from Negocio.mostrar_datos import mostrar_datos_compania
            mostrar_datos_compania()
        elif opcion == '2':
            from Negocio.mostrar_datos import mostrar_datos_direccion
            mostrar_datos_direccion()
        elif opcion == '3':
            from Negocio.mostrar_datos import mostrar_datos_usuario
            mostrar_datos_usuario()
        elif opcion == '4':
            from Negocio.mostrar_datos import mostrar_datos_tarea
            mostrar_datos_tarea()
        elif opcion == '5':
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

def menu_de_sistema():
    while True:
        menu2()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            print("Obteniendo datos desde JSON Placeholder...")
            obtener_y_almacenar_todos_los_datos()
        elif opcion == '2':
            print("Insertando datos nuevos...")
            insertar_datos(Modelos) # Llama a la función para insertar datos
        elif opcion == '3':
            print("Mostrando datos almacenados...")
            menu_mostrar_datos()
        elif opcion == '4':
            print("Actualizando datos existentes...")
            # Lógica para actualizar datos existentes
        elif opcion == '5':
            print("Eliminando datos...")
            # Lógica para eliminar datos
        elif opcion == '6':
            print("Cerrando sesión...")
            break
        elif opcion == '7':
            print("Saliendo del programa...")
            exit(0)
        else:
            print("Opción no válida, por favor intente de nuevo.")