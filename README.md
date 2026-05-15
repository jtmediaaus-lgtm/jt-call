# JT Invoice

Lightweight in-browser invoice generator and catalog for **JT Media Aus** (Jack Templeman). Two-page static app, zero build step.

**Live:** [jt-call.vercel.app](https://jt-call.vercel.app)

## What it does

- **Catalog** (`/`) — searchable archive of past invoices with totals, clients, and a one-click print-ready view.
- **Generator** (`/new`) — build new invoices, save per-client "regular order" templates, manage saved services, and print/PDF.

Everything is client-side — your data lives in your browser's `localStorage`.

## URLs

| Path | What |
|------|------|
| `/` or `/catalog` | Past-invoice catalog |
| `/new` or `/generator` | Invoice generator |
| `/call.html` | Legacy JT/CALL flowchart app (unfinished, hidden) |

## Local development

Everything is plain HTML/CSS/JS — no build step. Open the files directly or serve them with anything.

```bash
git clone https://github.com/jtmediaaus-lgtm/jt-call.git
cd jt-call
python3 -m http.server 8000
# then visit http://localhost:8000/invoice-generator/catalog.html
```

## File map

```
index.html                       # redirects → /invoice-generator/catalog.html
invoice-generator/
  catalog.html                   # past-invoice catalog (read-only)
  index.html                     # invoice generator
call.html                        # legacy flowchart app, preserved but unlinked
vercel.json                      # routing for /catalog, /new, etc.
```

## Deployment

Auto-deployed to Vercel from `main`. No build command — Vercel serves the static files directly.
