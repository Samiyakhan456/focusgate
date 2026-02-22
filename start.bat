@echo off
:: ============================================================
:: start.bat — FocusGate Launcher (Windows)
:: ============================================================
:: Double-click this file every morning to start FocusGate.
:: It will:
::   1. Start the Python server
::   2. Open the task manager in Chrome automatically
:: ============================================================

:: Change to the folder where this script lives
cd /d "%~dp0"

echo.
echo  ╔══════════════════════════════════════╗
echo  ║       FocusGate is starting...       ║
echo  ╚══════════════════════════════════════╝
echo.

:: Check Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo  ERROR: Python not found.
    echo  Please install it from https://python.org
    pause
    exit /b 1
)

:: Check server.py exists
if not exist "server.py" (
    echo  ERROR: server.py not found.
    echo  Make sure you're running this from the focusgate folder.
    pause
    exit /b 1
)

:: Open the task manager in Chrome after a short delay
timeout /t 2 /nobreak >nul
start "" "http://localhost:8000"

:: Start the server
echo  Server starting at http://localhost:8000
echo  Opening task manager in Chrome...
echo.
echo  Keep this window open while you work.
echo  Close it when you are done for the day.
echo.
python server.py

pause
