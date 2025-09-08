@echo off
echo =============================================
echo      STARTING AVATAR SERVER
echo =============================================
echo.

cd /d D:\My_Projects\Avatar-v1

if not exist venv_new (
    echo ERROR: Virtual environment not found!
    echo Please run WINDOWS_SETUP.bat first
    pause
    exit /b 1
)

echo Activating virtual environment...
call venv_new\Scripts\activate.bat

echo.
echo Starting server on http://127.0.0.1:8000
echo.
echo Press Ctrl+C to stop the server
echo =============================================
echo.

python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

pause