from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#1. Definimos el nombre de la base de datos

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

#2. Creamos el motor de la base de datos (engine)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. Creamos la sesion (es lo que nos permite guardar/borrar datos)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Creamos la clase base para nuestros modelos (de aquí heredarán nuestros modelos)
Base = declarative_base()

