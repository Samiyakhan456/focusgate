# FocusGate 🔒

Blocks Instagram until you finish your daily tasks.

## How it works
- Add tasks at `http://localhost:8000`
- Instagram stays blocked until every task is checked off
- Built with Python + Chrome Extension (Manifest V3)

## Setup
1. `cd focusgate_v2`
2. `python3 server.py`
3. Load the `extension/` folder in Chrome via `chrome://extensions` → Developer Mode → Load Unpacked
4. Open `http://localhost:8000` and add your tasks

## Stack
- Python (built-in HTTP server)
- Vanilla HTML/CSS/JavaScript
- Chrome Extension (Manifest V3)
