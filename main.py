from fastapi.responses import FileResponse
from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session
import uuid

# Importamos nuestros archivos nuevos
import models
from database import SessionLocal, engine

# --- CONFIGURACIÓN INICIAL ---
# 1. Esto crea las tablas en el archivo 'sql_app.db' si no existen
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# --- DEPENDENCIA (Dependency Injection) ---
# Esta función se encarga de abrir y cerrar la conexión a la DB en cada petición.
# Es el equivalente al EntityManager de Java.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- DTO (Pydantic) ---
# Esto es lo que el usuario ENVÍA (JSON)
class URLSolicitud(BaseModel):
    url: str


# --- RUTAS ---

# Nueva función para la ruta raíz
@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.post("/acortar")
def crear_url_corta(solicitud: URLSolicitud, db: Session = Depends(get_db)):
    # 1. Generamos clave
    clave_generada = str(uuid.uuid4())[:5]
    
    # 2. Creamos el Objeto Database (Entity)
    # Fíjate que usamos la clase de models.py
    nuevo_item = models.URLItem(clave=clave_generada, url_target=solicitud.url)
    
    # 3. Guardamos en DB (Transacción)
    db.add(nuevo_item)   # Insert
    db.commit()          # Confirmar cambios
    db.refresh(nuevo_item) # Recargar datos
    
    return {
        "mensaje": "URL guardada en BD",
        "clave": clave_generada,
        "short_url": f"http://127.0.0.1:8000/{clave_generada}"
    }

@app.get("/{clave}")
def redireccionar(clave: str, db: Session = Depends(get_db)):
    # 1. Buscamos en la DB (SELECT * FROM urls WHERE clave = ...)
    url_item = db.query(models.URLItem).filter(models.URLItem.clave == clave).first()
    
    # 2. Verificamos si existe
    if url_item:
        return RedirectResponse(url=url_item.url_target)
    else:
        raise HTTPException(status_code=404, detail="URL no encontrada en la base de datos")