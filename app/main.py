# D:
# cd \Avatar
# python -m venv venv
# venv\Scripts\activate
# pip install -r requirements.txt
# uvicorn app.main:app --reload
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/docs

# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.routers.chat import router as chat_router
from app.routers.avatar import router as avatar_router
from app.routers.transcribe import router as transcribe_router

app = FastAPI(title="Avatar Chat + HeyGen Streaming")

# === Настройка CORS для фронтэнда ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # можно заменить на список ваших доменов
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Подключение API-роутеров - отдельных частей приложения (термин из ФастАпи) ===
app.include_router(chat_router)
app.include_router(avatar_router)
app.include_router(transcribe_router)

# === Подключение статики (фронтенд) ===
# Монтируем папку public/ как корневую статику, html=True отдает index.html
app.mount(
    "/",
    StaticFiles(directory="public", html=True),
    name="static"
)
