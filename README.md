# FocusGate 🔒
### Block Instagram until your tasks are done.

Add your daily tasks. Instagram stays locked until every single one is checked off. Built with Python and a Chrome extension — no accounts, no subscriptions, no cloud.

![FocusGate Demo](https://github.com/Samiyakhan456/focusgate/raw/main/screenshots/demo.gif)

---

## The problem it solves

Opening Instagram before finishing work is effortless. Blocking it shouldn't require willpower — it should be automatic. FocusGate locks Instagram at the browser level and only unlocks it once every task on your list is checked off.

---

## How it works

```
You visit instagram.com
        ↓
Chrome extension intercepts the navigation
        ↓
Calls http://localhost:8000/status on your local server
        ↓
Server reads tasks.json on your computer
        ↓
Tasks incomplete → redirected to task manager
Tasks complete   → Instagram loads normally 🎉
```

---

## How to install

### Step 1 — Download the project
Click the green **Code** button → **Download ZIP** → unzip it on your Desktop.

### Step 2 — Run the setup script (once only)

**Mac:** Double-click **`setup.command`**

> If Mac says *"cannot be opened because it is from an unidentified developer"*:
> Right-click → **Open** → **Open** again.

**Windows:** Double-click **`setup.bat`**

This generates the extension icons and opens Chrome's extension page automatically.

### Step 3 — Install the Chrome extension (once only)
1. Toggle **Developer mode** ON (top-right corner of the extensions page)
2. Click **Load unpacked**
3. Select the **`extension`** folder inside the project
4. FocusGate appears in your Chrome toolbar ✅

### Step 4 — Every morning

**Mac:** Double-click `start.command`  
**Windows:** Double-click `start.bat`

This starts the server and opens your task manager automatically. Add your tasks and get to work. 🎯

---

## Screenshots

> Task manager — add and track your daily tasks

![Task Manager](screenshots/taskmanager.png)

> Instagram blocked — redirected when tasks are incomplete

![Blocked](screenshots/blocked.png)

---

## Files

```
focusgate/
├── start.command      ← Mac: double-click every morning
├── start.bat          ← Windows: double-click every morning
├── setup.command      ← Mac: double-click once to install
├── setup.bat          ← Windows: double-click once to install
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

- Python 3 — [python.org](https://python.org)
- Google Chrome
- Mac or Windows

---

## What I learned

This project taught me more about browser security than I expected. My original design passed task data through three layers — `localStorage` → `content.js` → `chrome.storage` → `background.js` — and Chrome's security model blocked it at every step. Content scripts don't run on `http://` pages by default, `chrome.storage` isn't accessible from web pages, and `file://` URLs can't be redirected to by extensions.

After three failed architectures I landed on a much simpler approach: skip the sync entirely and have the extension call a local Python server directly. One HTTP request to `/status`, one JSON response. The simplest solution turned out to be the most reliable.

I also learned that debugging Chrome extensions is non-obvious — the service worker has its own console completely separate from the page console, and finding it took longer than the actual fix. Knowing where to look is half the battle.

---

*Built with vanilla Python, HTML, CSS, and JavaScript. No frameworks, no dependencies.*
