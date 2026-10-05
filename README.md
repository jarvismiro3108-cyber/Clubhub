# Club Hub

Independent football fan site: history, records, squads and match predictions for every club in the top 5 European leagues and the Süper Lig.

- `src/template.html` — the front end
- `data/` — club files, league tables, coaches
- `build.py` — builds `public/index.html` (run `python3 build.py`)
- `public/` — the website that gets deployed
- `worker.js`, `wrangler.jsonc` — Cloudflare Worker (site + AI endpoint)

See `CLAUDE.md` for how everything works.
