@echo off
echo =============================================
echo   COPYING AVATAR SETUP FILES
echo =============================================
echo.
echo This script will copy all setup files to your Avatar project
echo.

set SOURCE=%~dp0
set DEST=D:\My_Projects\Avatar-v1\

echo Source: %SOURCE%
echo Destination: %DEST%
echo.

if not exist "%DEST%" (
    echo ERROR: Destination folder not found!
    echo Please make sure D:\My_Projects\Avatar-v1\ exists
    pause
    exit /b 1
)

echo Copying files...
echo.

copy "%SOURCE%AVATAR_MANAGER.bat" "%DEST%" /Y
echo Copied: AVATAR_MANAGER.bat

copy "%SOURCE%QUICK_START.bat" "%DEST%" /Y
echo Copied: QUICK_START.bat

copy "%SOURCE%WINDOWS_SETUP.bat" "%DEST%" /Y
echo Copied: WINDOWS_SETUP.bat

copy "%SOURCE%START_SERVER.bat" "%DEST%" /Y
echo Copied: START_SERVER.bat

copy "%SOURCE%FIX_PYDANTIC.bat" "%DEST%" /Y
echo Copied: FIX_PYDANTIC.bat

copy "%SOURCE%TEST_IMPORTS.py" "%DEST%" /Y
echo Copied: TEST_IMPORTS.py

copy "%SOURCE%run_server.py" "%DEST%" /Y
echo Copied: run_server.py

copy "%SOURCE%launcher.py" "%DEST%" /Y
echo Copied: launcher.py

copy "%SOURCE%requirements_windows.txt" "%DEST%" /Y
echo Copied: requirements_windows.txt

copy "%SOURCE%WINDOWS_INSTRUCTIONS.md" "%DEST%" /Y
echo Copied: WINDOWS_INSTRUCTIONS.md

echo.
echo =============================================
echo   ALL FILES COPIED SUCCESSFULLY!
echo =============================================
echo.
echo Next steps:
echo 1. Go to D:\My_Projects\Avatar-v1\
echo 2. Run AVATAR_MANAGER.bat
echo 3. Choose option 1 for setup
echo.
pause