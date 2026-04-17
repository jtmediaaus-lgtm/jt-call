#!/bin/bash
# JT/CALL Launcher
# Double-click this file to start the app

DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$DIR"

# Kill any existing instance on port 2727
lsof -ti:2727 | xargs kill -9 2>/dev/null

# Start server
python3 server.py
