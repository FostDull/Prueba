from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import httpx
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Global Weather API",
    description="Get the current weather of any city in the world using the OpenWeatherMap API.",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend origin for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# 🔹 FRONTEND CONFIGURATION
# ==============================
# Ruta base del frontend (ajusta si está en otro lugar)
frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")

# Montar archivos estáticos (CSS, JS, imágenes)
app.mount("/static", StaticFiles(directory=os.path.join(frontend_path, "static")), name="static")

# Servir index.html en la raíz
@app.get("/")
async def serve_index():
    index_file = os.path.join(frontend_path, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    else:
        return {"message": "Welcome to the Global Weather API 🌦️"}

# ==============================
# 🔹 API CONFIGURATION
# ==============================

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.get("/weather/")
async def get_weather(city: str, country: str = None):
    if not OPENWEATHER_API_KEY:
        raise HTTPException(status_code=500, detail="API key not configured")

    location = f"{city},{country}" if country else city

    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params={
            "q": location,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric",
            "lang": "en"
        })

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail=f"City '{city}' not found.")
    elif response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())

    data = response.json()

    if "name" not in data or not data["name"]:
        raise HTTPException(status_code=404, detail="Invalid location. Please enter a valid city name.")

    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": f"{data['main']['temp']} °C",
        "description": data["weather"][0]["description"],
        "humidity": f"{data['main']['humidity']}%",
        "wind": f"{data['wind']['speed']} m/s",
        "icon": f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
    }
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import httpx
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Global Weather API",
    description="Get the current weather of any city in the world using the OpenWeatherMap API.",
    version="1.0.0"
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend origin for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==============================
# 🔹 FRONTEND CONFIGURATION
# ==============================
# Ruta base del frontend (ajusta si está en otro lugar)
frontend_path = os.path.join(os.path.dirname(__file__), "../frontend")

# Montar archivos estáticos (CSS, JS, imágenes)
app.mount("/static", StaticFiles(directory=os.path.join(frontend_path, "static")), name="static")

# Servir index.html en la raíz
@app.get("/")
async def serve_index():
    index_file = os.path.join(frontend_path, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    else:
        return {"message": "Welcome to the Global Weather API 🌦️"}

# ==============================
# 🔹 API CONFIGURATION
# ==============================

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

@app.get("/weather/")
async def get_weather(city: str, country: str = None):
    if not OPENWEATHER_API_KEY:
        raise HTTPException(status_code=500, detail="API key not configured")

    location = f"{city},{country}" if country else city

    async with httpx.AsyncClient() as client:
        response = await client.get(BASE_URL, params={
            "q": location,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric",
            "lang": "en"
        })

    if response.status_code == 404:
        raise HTTPException(status_code=404, detail=f"City '{city}' not found.")
    elif response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.json())

    data = response.json()

    if "name" not in data or not data["name"]:
        raise HTTPException(status_code=404, detail="Invalid location. Please enter a valid city name.")

    return {
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": f"{data['main']['temp']} °C",
        "description": data["weather"][0]["description"],
        "humidity": f"{data['main']['humidity']}%",
        "wind": f"{data['wind']['speed']} m/s",
        "icon": f"https://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
    }
