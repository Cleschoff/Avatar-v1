@echo off
echo =============================================
echo     FIXING PYDANTIC COMPATIBILITY
echo =============================================
echo.

cd /d D:\My_Projects\Avatar-v1

if exist venv_new (
    call venv_new\Scripts\activate.bat
) else if exist venv (
    call venv\Scripts\activate.bat
) else (
    echo ERROR: No virtual environment found!
    pause
    exit /b 1
)

echo Removing old pydantic versions...
pip uninstall pydantic pydantic-core pydantic-settings -y

echo.
echo Installing compatible versions...
pip install pydantic==2.5.3 --no-deps
pip install pydantic-core==2.14.6
pip install typing-extensions==4.9.0 annotated-types==0.6.0
pip install pydantic-settings==2.1.0

echo.
echo Testing import...
python -c "import pydantic; print(f'Pydantic {pydantic.__version__} installed successfully!')"

echo.
echo =============================================
echo Fix complete! Try running START_SERVER.bat
echo =============================================
echo.
pause