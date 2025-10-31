# Global Weather App

## Description

This project is a **Global Weather App** that allows users to get the current weather for any city in the world using **FastAPI** as the backend and a Bootstrap-based frontend. It uses the **OpenWeatherMap API** to fetch live weather data.

---

## Features

* Query the weather for any city in the world.
* Display temperature, weather description, humidity, and wind speed.
* Save search results in a table dynamically.
* Responsive UI using Bootstrap 5.
* FastAPI backend with CORS enabled to allow frontend requests.
* Environment variables support with `.env` for storing API keys securely.

---

## Technologies

* **Frontend:** HTML, CSS (Bootstrap 5), JavaScript
* **Backend:** Python 3.11+, FastAPI, httpx, python-dotenv
* **API:** [OpenWeatherMap API](https://openweathermap.org/api)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/global-weather-app.git
cd global-weather-app/backend
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows (PowerShell):**

```powershell
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

In the `backend` folder, create a `.env` file with your OpenWeatherMap API key:

```
OPENWEATHER_API_KEY=your_api_key_here
```

### 6. Run the backend

```bash
uvicorn main:app --reload --port 8080
```

The backend will be available at: `http://127.0.0.1:8080`.

### 7. Open the frontend

1. Go to the frontend folder (where `index.html` is located).
2. Open it using **VS Code Live Server** or any local server.
3. Access it via: `http://127.0.0.1:5500` (or your Live Server URL).

---
