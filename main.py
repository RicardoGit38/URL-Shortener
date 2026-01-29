from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import uuid  # Librería para generar IDs únicos

app = FastAPI()

# --- BASE DE DATOS SIMULADA ---
# Aquí guardaremos las parejas: "clave_corta" -> "url_larga"
# Ej: {'a1b2': 'https://google.com'}
base_de_datos = {}

# --- MODELOS ---
class URLSolicitud(BaseModel):
    url: str

# --- RUTAS ---

@app.post("/acortar")
def crear_url_corta(solicitud: URLSolicitud):
    # 1. Generamos una clave única (cortamos el ID para que sea breve, 5 letras)
    clave = str(uuid.uuid4())[:5]
    
    # 2. GUARDAMOS en nuestra "Base de Datos"
    base_de_datos[clave] = solicitud.url
    
    # 3. Devolvemos la URL lista para usar
    return {
        "mensaje": "URL guardada",
        "clave": clave,
        "short_url": f"http://127.0.0.1:8000/{clave}"
    }

# La ruta de redirección
@app.get("/{clave}")
def redireccionar(clave: str):
    # 1. Buscamos si la clave existe en el diccionario
    if clave in base_de_datos:
        url_original = base_de_datos[clave]
        # 2. Redirigimos al usuario (Código 307)
        return RedirectResponse(url=url_original)
    else:
        # Si no existe, error 404
        raise HTTPException(status_code=404, detail="Esa URL corta no existe")