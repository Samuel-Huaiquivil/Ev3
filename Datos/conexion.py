# Conexión a la base de datos

from contextlib import contextmanager
from urllib.parse import quote_plus
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Configuración de la conexión a la base de datos
# Ingreso de credenciales y parámetros de conexión
password = quote_plus("a")
usuario_root = "a"
base_nombre = "a"
URL_DATABASE = f"mysql+mysqlconnector://{usuario_root}:{password}@localhost:3306/{base_nombre}"

motor_db = create_engine(URL_DATABASE, echo=False, future=True, pool_pre_ping=True)
Session = sessionmaker(bind=motor_db)

def verificar_conexion() -> bool:
    '''
    Verifica la conexión a la base de datos y la existencia de la base de datos.
    :return: True si la conexión es exitosa, False en caso contrario.
    '''
    try:
        with motor_db.connect() as conexion:
            # Verifica la conexión y que la base de datos existe
            result = conexion.execute(text("SELECT DATABASE()"))
            db_name = result.scalar()
            print(f"Conectado a la base de datos: {db_name}")
            return True
    except Exception as e:
        print(f" Error al conectar a la base de datos: {e}")
        return False
    
@contextmanager
def get_session():
    session = Session()
    try:
        yield session
        session.commit()  # Commit automático si todo va bien
    except Exception:
        session.rollback()  # Rollback si hay error
        raise
    finally:
        session.close()