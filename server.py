#!/usr/bin/env python3
"""
JT/CALL — Local server
Run this file. It will start a server at http://localhost:2727
and open your browser automatically.
"""

import http.server
import json
import os
import urllib.request
import urllib.error
import threading
import webbrowser
import time
import sys
import socketserver

PORT = 2727
DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_FILE = os.path.join(DIR, 'config.json')

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as f:
            return json.load(f)
    return {}

def save_config(data):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(data, f)

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def log_message(self, format, *args):
        pass  # suppress server logs

    def do_POST(self):
        if self.path == '/api/generate':
            length = int(self.headers.get('Content-Length', 0))
            body = json.loads(self.rfile.read(length))

            config = load_config()
            api_key = config.get('api_key', '')

            if not api_key:
                self.send_json(400, {'error': 'No API key set. Click Settings in the app.'})
                return

            try:
                payload = json.dumps({
                    'model': 'claude-sonnet-4-6',
                    'max_tokens': 4000,
                    'messages': body.get('messages', [])
                }).encode()

                req = urllib.request.Request(
                    'https://api.anthropic.com/v1/messages',
                    data=payload,
                    headers={
                        'Content-Type': 'application/json',
                        'x-api-key': api_key,
                        'anthropic-version': '2023-06-01'
                    },
                    method='POST'
                )
                with urllib.request.urlopen(req, timeout=60) as resp:
                    data = json.loads(resp.read())
                self.send_json(200, data)

            except urllib.error.HTTPError as e:
                err = json.loads(e.read())
                self.send_json(e.code, {'error': err.get('error', {}).get('message', str(e))})
            except Exception as e:
                self.send_json(500, {'error': str(e)})

        elif self.path == '/api/config':
            length = int(self.headers.get('Content-Length', 0))
            body = json.loads(self.rfile.read(length))
            save_config(body)
            self.send_json(200, {'ok': True})

        else:
            self.send_error(404)

    def do_GET(self):
        if self.path == '/api/config':
            config = load_config()
            # Don't send full key back, just whether it's set
            self.send_json(200, {'has_key': bool(config.get('api_key')), 'api_key': config.get('api_key','')})
        else:
            super().do_GET()

    def send_json(self, code, data):
        body = json.dumps(data).encode()
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', len(body))
        self.end_headers()
        self.wfile.write(body)

def open_browser():
    time.sleep(0.8)
    webbrowser.open(f'http://localhost:{PORT}')

if __name__ == '__main__':
    # Allow port reuse so relaunching doesn't fail
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(('', PORT), Handler) as httpd:
            threading.Thread(target=open_browser, daemon=True).start()
            print(f'JT/CALL running at http://localhost:{PORT}')
            httpd.serve_forever()
    except OSError:
        # Port already in use — just open browser
        webbrowser.open(f'http://localhost:{PORT}')
