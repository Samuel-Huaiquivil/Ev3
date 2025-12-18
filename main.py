# Menu de inicio donde inicia todo el programa

from Interfaz_Usuario.menu_inicio import menu
from Datos.create_table import crear_tablas
from Datos.conexion import verificar_conexion

if __name__ == "__main__":
    # Verifica la conexión a la base de datos 
    if not verificar_conexion():
        print("No se pudo conectar a la base de datos. Saliendo del programa.")
        exit(1)
    # Crear las tablas en la base de datos al iniciar el programa
    crear_tablas()
    menu()