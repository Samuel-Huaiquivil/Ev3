# Inteerfaz para el registrode usuario

def registrar_usuario():
    nombre = input("Ingrese su nombre completo: ")
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    telefono = input("Ingrese su número de teléfono (opcional): ")
    contrasena = input("Ingrese su contraseña: ")
    confirmar_contrasena = input("Confirme su contraseña: ")

    if contrasena != confirmar_contrasena:
        print("Las contraseñas no coinciden. Por favor, intente de nuevo.")
        return None
    print("Registro exitoso.")
    return nombre, nombre_usuario, contrasena, telefono