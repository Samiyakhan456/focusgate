#!/bin/bash
# ============================================================
# setup.command — FocusGate First-Time Setup
# ============================================================
# Run this ONCE after downloading or cloning the repo.
# It will:
#   1. Generate the extension icons
#   2. Make start.command double-clickable
#   3. Open Chrome's extension page for you
#   4. Print clear next steps
# ============================================================

cd "$(dirname "$0")"

echo ""
echo "╔══════════════════════════════════════════╗"
echo "║     FocusGate — First Time Setup         ║"
echo "╚══════════════════════════════════════════╝"
echo ""

# Step 1 — Generate icons
echo "⏳ Step 1/3 — Generating extension icons..."
python3 make_icons.py
echo ""

# Step 2 — Make start.command executable so it can be double-clicked
echo "⏳ Step 2/3 — Making start.command double-clickable..."
chmod +x start.command
echo "✅ Done."
echo ""

# Step 3 — Open Chrome extension page automatically
echo "⏳ Step 3/3 — Opening Chrome extension page..."
open "chrome://extensions"
echo ""

# Print final instructions
echo "╔══════════════════════════════════════════════════════╗"
echo "║  Setup complete! One manual step left:               ║"
echo "║                                                      ║"
echo "║  In the Chrome window that just opened:              ║"
echo "║  1. Toggle ON 'Developer mode' (top right)           ║"
echo "║  2. Click 'Load unpacked'                            ║"
echo "║  3. Select the 'extension' folder inside focusgate   ║"
echo "║                                                      ║"
echo "║  Then every morning just double-click start.command  ║"
echo "╚══════════════════════════════════════════════════════╝"
echo ""
read -p "Press Enter to close this window..."
