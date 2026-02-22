#!/bin/bash
# ============================================================
# start.command — FocusGate Launcher
# ============================================================
# Double-click this file every morning to start FocusGate.
# It will:
#   1. Start the Python server
#   2. Open the task manager in Chrome automatically
# ============================================================

# Change to the folder where this script lives
cd "$(dirname "$0")"

echo "╔══════════════════════════════════════╗"
echo "║       FocusGate is starting...       ║"
echo "╚══════════════════════════════════════╝"
echo ""

# Check Python is installed
if ! command -v python3 &> /dev/null; then
  echo "❌ Python3 not found. Please install it from python.org"
  read -p "Press Enter to close..."
  exit 1
fi

# Check server.py exists
if [ ! -f "server.py" ]; then
  echo "❌ server.py not found."
  echo "Make sure you're running this from the focusgate_v2 folder."
  read -p "Press Enter to close..."
  exit 1
fi

# Open the task manager in Chrome after a short delay
# (gives the server time to start first)
sleep 1.5 && open "http://localhost:8000" &

# Start the server (this stays running until you close the window)
echo "✅ Server starting at http://localhost:8000"
echo "✅ Opening task manager in Chrome..."
echo ""
echo "Keep this window open while you work."
echo "Close it when you're done for the day."
echo ""
python3 server.py
