@echo off
:menu
cls
echo ===============================================
echo         AVATAR PROJECT MANAGER
echo ===============================================
echo.
echo   1. Full Setup (Create new environment)
echo   2. Start Server
echo   3. Fix Pydantic Issues
echo   4. Test Imports
echo   5. Install from requirements_windows.txt
echo   6. Exit
echo.
echo ===============================================
echo.

set /p choice="Enter your choice (1-6): "

if "%choice%"=="1" goto setup
if "%choice%"=="2" goto start
if "%choice%"=="3" goto fix_pydantic
if "%choice%"=="4" goto test
if "%choice%"=="5" goto install_requirements
if "%choice%"=="6" goto end

echo Invalid choice! Please try again.
pause
goto menu

:setup
cls
call WINDOWS_SETUP.bat
pause
goto menu

:start
cls
call START_SERVER.bat
pause
goto menu

:fix_pydantic
cls
call FIX_PYDANTIC.bat
pause
goto menu

:test
cls
cd /d D:\My_Projects\Avatar-v1
if exist venv_new (
    venv_new\Scripts\python.exe TEST_IMPORTS.py
) else if exist venv (
    venv\Scripts\python.exe TEST_IMPORTS.py
) else (
    python TEST_IMPORTS.py
)
pause
goto menu

:install_requirements
cls
cd /d D:\My_Projects\Avatar-v1
if exist venv_new (
    call venv_new\Scripts\activate.bat
) else if exist venv (
    call venv\Scripts\activate.bat
)
echo Installing from requirements_windows.txt...
pip install -r requirements_windows.txt
pause
goto menu

:end
exit