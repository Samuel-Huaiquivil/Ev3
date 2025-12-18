# Creación de usuarios

def registrar_usuario(nombre, nombre_usuario, contrasena, telefono=None):
    '''
    Registra un nuevo usuario en la base de datos.
    
    Parámetros:
    nombre (str): Nombre completo del usuario.
    nombre_usuario (str): Nombre de usuario único.
    contrasena (str): Contraseña del usuario.
    telefono (str, opcional): Número de teléfono del usuario.
    
    Retorna:
    bool: True si el registro fue exitoso, False en caso contrario.
    '''
    from Datos.conexion import sesion_db
    from Modelos.registro import Registro
    import bcrypt

    # Hashear la contraseña antes de almacenarla
    contrasena_hashed = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt())

    nuevo_usuario = Registro(
        nombre_usuario=nombre_usuario,
        contrasena=contrasena_hashed.decode('utf-8'),
        telefono=telefono
    )

    try:
        sesion_db.add(nuevo_usuario)
        sesion_db.commit()
        print("Usuario registrado exitosamente.")
        return True
    except Exception as e:
        sesion_db.rollback()
        print(f"Error al registrar el usuario: {e}")
        return False