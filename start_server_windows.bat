@echo off
echo === Запуск Avatar сервера ===
cd /d D:\Avatar
call venv\Scripts\activate
echo.
echo Сервер запускается...
echo После запуска откройте http://127.0.0.1:8000/
echo.
uvicorn app.main:app --reload
pause