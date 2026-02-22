# FocusGate 🔒
### Block Instagram until your tasks are done.

Add your daily tasks. Instagram stays locked until every single one is checked off. Built with Python and a Chrome extension — no accounts, no subscriptions, no cloud.

---

## How to install

### Step 1 — Download the project
Click the green **Code** button on this page → **Download ZIP** → unzip it on your Desktop.

### Step 2 — Run the setup script (once only)
Open the `focusgate_v2` folder and double-click **`setup.command`**.

> If Mac says *"cannot be opened because it is from an unidentified developer"*:
> Right-click `setup.command` → **Open** → **Open** again.

This will automatically generate the icons and open Chrome's extension page.

### Step 3 — Install the Chrome extension (once only)
The setup script opens Chrome's extension page for you. Then:

1. Toggle **Developer mode** ON (switch in the top-right corner)
2. Click **Load unpacked**
3. Select the **`extension`** folder inside `focusgate_v2`
4. FocusGate appears in your Chrome toolbar ✅

### Step 4 — Every morning
Double-click **`start.command`** — it starts the server and opens your task manager automatically.

That's it. Add your tasks and get to work. 🎯

---

## How it works

```
You visit instagram.com
        ↓
Chrome extension checks http://localhost:8000/status
        ↓
Server reads tasks.json on your computer
        ↓
Tasks incomplete → redirected to task manager
Tasks complete   → Instagram loads normally 🎉
```

---

## Files
```
focusgate_v2/
├── start.command      ← double-click every morning
├── setup.command      ← double-click once to install
├── server.py          ← local Python server
├── index.html         ← task manager webpage
├── make_icons.py      ← generates extension icons
└── extension/
    ├── manifest.json
    ├── background.js
    ├── popup.html
    └── icons/
```

---

## Requirements
- Mac (the `.command` scripts are Mac only)
- Python 3 (pre-installed on most Macs — check with `python3 --version`)
- Google Chrome

---

*Built with vanilla Python, HTML, CSS, and JavaScript. No frameworks, no dependencies.*
