# Local Setup — JT/CALL

Run JT/CALL locally on your machine.

## Mac (Fastest)

1. **Get the files:**
   ```bash
   git clone https://github.com/yourusername/jt-call.git
   cd jt-call
   ```

2. **Run the server:**
   ```bash
   python3 server.py
   ```
   
   You should see:
   ```
   JT/CALL running at http://localhost:2727
   ```
   
   Browser opens automatically.

3. **Paste API key** in Settings
4. **Done!** Build flowcharts offline

## Mac (One-Click Launch)

Double-click `launch.command` instead of using terminal.

To make it permanent in your Applications:
1. Open Finder → Applications → Utilities
2. Open Automator
3. File → New → Application
4. Search for "Run Shell Script"
5. Paste this:
   ```bash
   cd /path/to/jt-call && python3 server.py
   ```
6. Save as "JT Call" to Applications
7. Drag it to your dock

Now you can launch from the dock like any app.

## Linux

```bash
git clone https://github.com/yourusername/jt-call.git
cd jt-call
python3 server.py
```

## Windows

1. Install Python 3.8+ from python.org
2. Open PowerShell, navigate to the folder:
   ```bash
   git clone https://github.com/yourusername/jt-call.git
   cd jt-call
   python server.py
   ```
3. Open browser → `http://localhost:2727`

## API Key Storage

**Local mode:** Your API key is stored in `config.json` on your machine. Never committed to GitHub (see `.gitignore`).

## Offline Usage

Works completely offline once loaded. Everything runs locally except the Anthropic API calls.

## Troubleshooting

**Port 2727 already in use?**
```bash
# Kill the process
lsof -i :2727
kill -9 <PID>
```

**Python not found?**
- Make sure Python 3.8+ is installed
- Use `python3` not `python`

**Permission denied on launch.command?**
```bash
chmod +x launch.command
./launch.command
```
