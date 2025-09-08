@echo off
echo AVATAR QUICK START
echo ==================
echo.

cd /d D:\My_Projects\Avatar-v1

:: Try to activate any existing environment
if exist venv_new\Scripts\activate.bat (
    call venv_new\Scripts\activate.bat
) else if exist venv\Scripts\activate.bat (
    call venv\Scripts\activate.bat
) else (
    echo No virtual environment found!
    echo Creating new one...
    python -m venv venv_quick
    call venv_quick\Scripts\activate.bat
    pip install fastapi==0.109.0 pydantic==2.5.3 uvicorn openai python-multipart websockets aiohttp pydub python-dotenv
)

echo.
echo Starting server...
echo.
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
pause