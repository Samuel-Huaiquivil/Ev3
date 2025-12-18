# El menú de inicio
from Interfaz_Usuario.login import login
from Interfaz_Usuario.registro import registrar_usuario
from Negocio.sesion_usuario import iniciar_sesion


def mostrar_menu_inicio():
    print("=== Menú de Inicio ===")
    print("1. Iniciar Sesión")
    print("2. Registrarse")
    print("3. Salir")

def menu():
    while True:
        mostrar_menu_inicio()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            print("Iniciando sesión...")
            nombre_usuario, contrasena = login()
            if iniciar_sesion(nombre_usuario, contrasena):
                print("Bienvenido al sistema.")
            else:
                print("Error al iniciar sesión.")
        elif opcion == '2':
            print("Registrándose...")
            registrar_usuario()
            continue
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")