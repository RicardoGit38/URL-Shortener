from sqlalchemy import Column, String
from database import Base

class URLItem(Base):
    # 1. Nombre de la tabla en la base de datos
    __tablename__ = "urls"

    # 2. Columnas
    # primary_key=True hace que esta sea la llave única
    # index=True ayuda a buscar más rápido
    clave = Column(String, primary_key=True, index=True)
    url_target = Column(String, index=True)