@echo off
echo =============================================
echo     AVATAR PROJECT - AUTOMATIC SETUP
echo =============================================
echo.

cd /d D:\My_Projects\Avatar-v1

echo [1/5] Removing old environments...
rmdir /s /q venv_old 2>nul
if exist venv (
    rename venv venv_old
)
rmdir /s /q venv_new 2>nul

echo [2/5] Creating new virtual environment...
python -m venv venv_new

echo [3/5] Activating environment...
call venv_new\Scripts\activate.bat

echo [4/5] Upgrading pip...
python -m pip install --upgrade pip

echo [5/5] Installing packages...
echo Installing FastAPI framework...
pip install fastapi==0.109.0

echo Installing Pydantic (compatible version)...
pip install pydantic==2.5.3

echo Installing Uvicorn server...
pip install uvicorn[standard]

echo Installing OpenAI...
pip install openai

echo Installing other dependencies...
pip install python-multipart websockets aiohttp pydub python-dotenv requests

echo.
echo =============================================
echo     SETUP COMPLETE!
echo =============================================
echo.
echo Your project is ready to run!
echo.
echo To start the server, run:
echo     start_server.bat
echo.
echo Or manually:
echo     venv_new\Scripts\activate
echo     python -m uvicorn app.main:app --reload
echo.
pause