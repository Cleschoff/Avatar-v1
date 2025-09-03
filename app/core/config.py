# core/config.py

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Ключ API для OpenAI
    OPENAI_API_KEY: str
    # Ключ API для HeyGen
    HEYGEN_API_KEY: str
    # URL сервера HeyGen (можно переопределить в .env)
    HEYGEN_SERVER_URL: str = "https://api.heygen.com"
    # ID аватара по умолчанию
    AVATAR_ID: str = "Amina_Chair_Sitting_public"
    # ID голоса по умолчанию
    VOICE_ID: str = "bc69c9589d6747028dc5ec4aec2b43c3"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Загружаем настройки из окружения
settings = Settings()
