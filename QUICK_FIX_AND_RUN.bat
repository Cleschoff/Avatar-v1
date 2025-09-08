@echo off
echo =============================================
echo     AVATAR - QUICK FIX AND RUN
echo =============================================
echo.

cd /d D:\My_Projects\Avatar-v1

:: Check if we have any venv
if exist venv (
    echo Using existing venv...
    call venv\Scripts\activate.bat
) else (
    echo Creating new venv...
    python -m venv venv
    call venv\Scripts\activate.bat
)

echo.
echo Installing/Updating packages...
pip uninstall pydantic pydantic-core -y >nul 2>&1
pip install fastapi==0.109.0 pydantic==2.5.3 uvicorn[standard] openai python-multipart websockets aiohttp pydub python-dotenv requests

echo.
echo =============================================
echo Starting server on http://127.0.0.1:8000
echo Press Ctrl+C to stop
echo =============================================
echo.

python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

pause