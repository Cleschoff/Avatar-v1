@echo off
echo === Исправление проблем с pydantic в Windows ===
echo.

cd /d D:\My_Projects\Avatar-v1

echo Деактивация старого окружения...
call venv\Scripts\deactivate.bat 2>nul

echo Удаление старого venv...
rmdir /s /q venv

echo Создание нового виртуального окружения...
python -m venv venv

echo Активация нового окружения...
call venv\Scripts\activate.bat

echo Обновление pip...
python -m pip install --upgrade pip

echo Установка зависимостей с правильными версиями...
pip install fastapi==0.109.0
pip install "pydantic>=2.5.0,<2.6.0"
pip install uvicorn[standard]
pip install openai
pip install python-multipart
pip install websockets
pip install aiohttp
pip install pydub
pip install python-dotenv
pip install requests

echo.
echo === Установка завершена! ===
echo Попробуйте запустить сервер:
echo python -m uvicorn app.main:app --reload
echo.
pause