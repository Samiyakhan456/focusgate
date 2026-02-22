#!/usr/bin/env python3
# ============================================================
# server.py — FocusGate Local Server
# ============================================================
# This replaces "python3 -m http.server".
# Run it with:  python3 server.py
#
# It does two things:
#   1. Serves index.html at http://localhost:8000
#   2. Handles /tasks API so the extension can read task status
#      without any content script or storage sync needed.
# ============================================================

import json
import os
from http.server import HTTPServer, BaseHTTPRequestHandler

TASKS_FILE = os.path.join(os.path.dirname(__file__), 'tasks.json')

# Make sure tasks.json exists on first run
if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'w') as f:
        json.dump([], f)


class Handler(BaseHTTPRequestHandler):

    # ── GET requests ──────────────────────────────────────
    def do_GET(self):

        # Serve the task manager page
        if self.path == '/' or self.path == '/index.html':
            self.serve_file('index.html', 'text/html')

        # ★ THE KEY ENDPOINT ★
        # background.js calls this to check if Instagram is unlocked
        # Returns: {"status": "locked"} or {"status": "unlocked"}
        elif self.path == '/status':
            self.serve_status()

        # The extension also needs the raw task list
        elif self.path == '/tasks':
            self.serve_tasks()

        # Serve static files (CSS, JS, etc.)
        else:
            filename = self.path.lstrip('/')
            if os.path.exists(filename):
                ext = filename.split('.')[-1]
                types = {
                    'css': 'text/css',
                    'js':  'application/javascript',
                    'png': 'image/png',
                    'ico': 'image/x-icon'
                }
                self.serve_file(filename, types.get(ext, 'text/plain'))
            else:
                self.send_error(404, 'Not found')

    # ── POST requests ─────────────────────────────────────
    def do_POST(self):

        # Save tasks sent from index.html
        if self.path == '/tasks':
            length = int(self.headers.get('Content-Length', 0))
            body   = self.rfile.read(length)

            try:
                tasks = json.loads(body)
                with open(TASKS_FILE, 'w') as f:
                    json.dump(tasks, f)

                self.send_json({'ok': True})
                print(f'[FocusGate] Tasks saved: {len(tasks)} tasks')
            except Exception as e:
                self.send_error(400, str(e))
        else:
            self.send_error(404, 'Not found')

    # ── HELPERS ───────────────────────────────────────────

    def serve_status(self):
        """Read tasks.json and return locked/unlocked status."""
        try:
            with open(TASKS_FILE) as f:
                tasks = json.load(f)

            total = len(tasks)
            done  = sum(1 for t in tasks if t.get('done'))

            if total > 0 and done == total:
                status = 'unlocked'
            else:
                status = 'locked'

            self.send_json({
                'status':    status,
                'total':     total,
                'done':      done,
                'remaining': total - done
            })
            print(f'[FocusGate] Status check: {done}/{total} → {status}')

        except Exception as e:
            self.send_json({'status': 'locked', 'error': str(e)})

    def serve_tasks(self):
        """Return raw tasks list."""
        try:
            with open(TASKS_FILE) as f:
                data = f.read()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(data.encode())
        except:
            self.send_json([])

    def serve_file(self, filename, content_type):
        """Serve a file from disk."""
        try:
            mode = 'rb' if content_type.startswith('image') else 'r'
            with open(filename, mode) as f:
                content = f.read()

            self.send_response(200)
            self.send_header('Content-Type', content_type)
            self.send_cors_headers()
            self.end_headers()

            if isinstance(content, str):
                self.wfile.write(content.encode())
            else:
                self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, f'{filename} not found')

    def send_json(self, data):
        """Send a JSON response."""
        body = json.dumps(data).encode()
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_cors_headers()
        self.end_headers()
        self.wfile.write(body)

    def send_cors_headers(self):
        """
        Allow the Chrome extension to call our server.
        Without these headers, Chrome blocks cross-origin requests.
        """
        self.send_header('Access-Control-Allow-Origin',  '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def do_OPTIONS(self):
        """Handle CORS preflight requests."""
        self.send_response(200)
        self.send_cors_headers()
        self.end_headers()

    # Suppress the default request log spam
    def log_message(self, format, *args):
        pass


if __name__ == '__main__':
    port   = 8000
    server = HTTPServer(('localhost', port), Handler)
    print(f'╔══════════════════════════════════════╗')
    print(f'║  FocusGate server running!           ║')
    print(f'║  Task Manager → http://localhost:{port} ║')
    print(f'║  Press Ctrl+C to stop                ║')
    print(f'╚══════════════════════════════════════╝')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print('\nServer stopped.')
