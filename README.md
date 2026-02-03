# ✂️ Acortador de URLs con FastAPI & SQLite

Una aplicación Full Stack robusta para acortar enlaces, construida con **Python** y **FastAPI**. Diseñada con arquitectura escalable, persistencia de datos real y una interfaz de usuario amigable.

## 🚀 Características Principales

* **Backend de Alto Rendimiento:** API REST construida con FastAPI (uno de los frameworks más rápidos de Python).
* **Persistencia de Datos:** Uso de **SQLite** y **SQLAlchemy** (ORM) para almacenar enlaces de forma permanente. No se pierden al reiniciar el servidor.
* **Frontend Integrado:** Interfaz web limpia (HTML/CSS/JS) servida directamente desde el backend.
* **Redirección Inteligente:** Sistema de validación y redirección HTTP 307.
* **Arquitectura Limpia:** Separación de responsabilidades en Modelos (`models.py`), Esquemas y Lógica (`main.py`) y Configuración (`database.py`).

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+
* **Framework API:** FastAPI
* **Servidor:** Uvicorn (ASGI)
* **ORM:** SQLAlchemy
* **Base de Datos:** SQLite (Archivo local)
* **Frontend:** HTML5, JavaScript (Fetch API), CSS3

## 📦 Instalación y Despliegue Local

Sigue estos pasos para correr el proyecto en tu máquina:

### 1. Clonar el repositorio
```bash
git clone [https://github.com/RicardoGit38/fastapi-url-shortener.git](https://github.com/RicardoGit38/fastapi-url-shortener.git)
cd fastapi-url-shortener

### 2. Crear entorno virtual
python -m venv venv
# En Windows:
.\venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate

### 3. Instalar dependencias
pip install fastapi uvicorn sqlalchemy aiofiles

### 4. Ejecutar el servidor
uvicorn main:app --reload

El servidor iniciará en http://127.0.0.1:8000