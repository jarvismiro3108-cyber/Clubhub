# Club Hub

Football club website: history, records, squad picker and match predictions for every club in the top 5 leagues and the Süper Lig.

- `public/index.html` — the whole website
- `worker.js` — Cloudflare Worker: serves the site and the AI endpoint `/api/analyze` (Gemini, with Google Search for current form)
- `wrangler.jsonc` — Cloudflare settings

The Gemini key is stored in Cloudflare as the secret `GEMINI_API_KEY` (never in this repo).
