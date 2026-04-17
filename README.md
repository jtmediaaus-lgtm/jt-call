# JT/CALL — Call Strategy Flowchart Builder

**Generate structured call scripts & strategy in seconds.** Built for fight promoters, sponsorship negotiators, and sales professionals who need to prep fast and execute smart.

## Features

- 🎯 **Smart flowcharts** — Claude AI builds your call strategy based on situation, numbers, and psychology
- 📱 **Multi-device** — Works on iPhone, Mac, Windows, iPad. Just open the link.
- 💾 **Session memory** — Automatically saves recent calls
- 📊 **Data dashboard** — Track ask/target/floor prices in real-time
- ↓ **Export HTML** — Download standalone flowchart (share, print, archive)
- 🎨 **Native macOS design** — Rounded corners, glassmorphism, zero clutter

## Quick Start

### Online (No Installation)
1. Go to **[jt-call.vercel.app](https://jt-call.vercel.app)** (coming soon)
2. Paste your Anthropic API key (free at console.anthropic.com)
3. Describe your call situation
4. Click "Build Flowchart" → AI generates your strategy in ~15 seconds

### Local (Mac/Linux)
```bash
git clone https://github.com/yourusername/jt-call.git
cd jt-call
python3 server.py
```
Browser opens automatically at `http://localhost:2727`

## How It Works

1. **You provide context:**
   - Who are you talking to? (client, contact name, call type)
   - What's the situation? (goals, objections, stakes)
   - What are your numbers? (ask, target, floor)

2. **Claude analyzes & generates:**
   - Opening script (set the vibe)
   - Listening phase (understand their position)
   - Objection handling (deflect/negotiate)
   - Close strategy (seal the deal)
   - Psychology & tactics for each phase

3. **You execute:**
   - Follow the flowchart step-by-step
   - Click through their responses
   - See the "why" behind each tactic
   - Export for reference during call

## Cost

**~$0.03 per call** (Anthropic API)
- 1000 tokens input @ $3/1M = $0.003
- 2000 tokens output @ $15/1M = $0.03
- Total: ~$0.033 per flowchart

## Files

- `index.html` — The app (redesigned macOS UI)
- `server.py` — Local Python server (handles API calls securely)
- `launch.command` — Double-click launcher for Mac
- `vercel.json` — Deployment config for serverless backend
- `api/generate.js` — Vercel serverless function (replaces server.py online)

## Deployment

### Option A: Local Only
```bash
python3 server.py
```
Runs at `http://localhost:2727`. Your API key stays on your machine.

### Option B: Online + Vercel (Recommended)
1. Push this repo to GitHub
2. Connect to Vercel → auto-deploys
3. Users visit your app → paste their own API key → works everywhere

See [DEPLOYMENT.md](./docs/deployment.md) for step-by-step.

## Tech Stack

- **Frontend:** Vanilla JS (no frameworks)
- **Backend:** Python (local) or Node.js/Vercel (online)
- **AI:** Anthropic Claude API
- **Hosting:** GitHub Pages (static) + Vercel (serverless backend)

## Security

- API keys are **never stored** or logged
- Each user pastes their own key (if using online version)
- Config saved locally in `config.json` (local mode only)
- No tracking, no analytics, no BS

## Roadmap

- [ ] Vercel deployment (online version)
- [ ] Mobile app (React Native)
- [ ] Voice transcription (record call, auto-log outcomes)
- [ ] Team collaboration (share flowcharts with sales team)
- [ ] Analytics (track call outcomes vs. strategy)

## Credits

Built by JT (age 18, Falcon WA) for fight promoters & sales pros.  
Inspired by Sev's multi-tool knowledge-hub pattern.

## License

MIT — Use it, fork it, build on it. Commercial use OK.

## Questions?

- Email: [your email]
- GitHub Issues: Post bugs/feature requests here
- Twitter: [@yourhandle]
