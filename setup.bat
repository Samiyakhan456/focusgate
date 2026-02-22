@echo off
:: ============================================================
:: setup.bat — FocusGate First-Time Setup (Windows)
:: ============================================================
:: Run this ONCE after downloading or cloning the repo.
:: ============================================================

cd /d "%~dp0"

echo.
echo  ╔══════════════════════════════════════════╗
echo  ║     FocusGate - First Time Setup         ║
echo  ╚══════════════════════════════════════════╝
echo.

:: Step 1 - Generate icons
echo  Step 1/2 - Generating extension icons...
python make_icons.py
echo.

:: Step 2 - Open Chrome extension page
echo  Step 2/2 - Opening Chrome extension page...
start "" "chrome://extensions"
echo.

echo  ╔══════════════════════════════════════════════════════╗
echo  ║  Setup complete! One manual step left:               ║
echo  ║                                                      ║
echo  ║  In the Chrome window that just opened:              ║
echo  ║  1. Toggle ON Developer mode (top right)             ║
echo  ║  2. Click Load unpacked                              ║
echo  ║  3. Select the extension folder inside focusgate     ║
echo  ║                                                      ║
echo  ║  Then every morning just double-click start.bat      ║
echo  ╚══════════════════════════════════════════════════════╝
echo.
pause
