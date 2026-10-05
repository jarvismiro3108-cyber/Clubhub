# Club Hub — notes for Claude Code

Football fan site: history, records, 2026/27 squads, a squad picker and match predictions for all
114 clubs in the Premier League, La Liga, Serie A, Bundesliga, Ligue 1 and Süper Lig.
Owner: Mir Ozel. Live at https://clubhub.jarvismiro3108.workers.dev (password-protected for now).

## How it fits together
- `src/template.html` — the whole front end (HTML + CSS + JS in one file). Fenerbahçe and Konyaspor
  have hand-written data inside it (`const CLUBS={...}`); every other club is injected at build time
  where the template says `/*EXTRA_DATA*/`.
- `data/clubs/<id>.json` — one file per club (schema in `data/CLUB_FILE_SPEC.md`). `<id>` is the slug of
  the club name as written in the `LEAGUES` list in the template (e.g. `1fckoln`, `parissaintgermain`).
- `data/computed_tables.json` — final tables rebuilt from match results (up to 2021–22);
  `data/raw/<league>_<season>.txt` — official tables `pos|team|P|W|D|L|GF|GA|Pts` for later seasons,
  plus `NOTE|team|text` (deductions etc.) and `SEASONNOTE|text` lines. `data/coaches.json` — current coaches.
- `build.py` — turns all of the above into `public/index.html`. **Always run `python3 build.py` after
  changing anything in `src/` or `data/`, and commit `public/index.html` too.** Never hand-edit
  `public/index.html`.
- `worker.js` + `wrangler.jsonc` — Cloudflare Worker named `clubhub`. It serves `public/` and the AI
  endpoint `POST /api/analyze`. Cloudflare builds and deploys automatically on every push to `main`
  (check status with the "Workers Builds: clubhub" check on the commit).
  The check shows no log. Once (5 Oct 2026) a production build failed for unknown reasons while the same code built fine
  locally (`npx wrangler deploy --dry-run`) and as a branch preview; the next push to `main` deployed normally.

## The AI part (worker.js)
- Gemini API (free tier) with Google Search grounding. The key is a Cloudflare secret; the worker
  accepts any env var whose name contains "gemini" (it is currently saved as `GEMINI-API-KEY-`).
  Never put keys or passwords in this repo — it is public.
- The browser sends structured match data; the server builds the prompt itself (`buildPrompt`), so the
  endpoint can't be used as a general chatbot. Keep it that way.
- Origin check, per-IP rate limit (Workers rate-limit binding `LIMITER` + in-memory fallback).
- Free tier may not be offered in the EEA/Switzerland/UK → those countries get HTTP 451 and the page
  falls back to its own simulation. Google requires showing the Search Suggestions (`suggest`) with
  grounded results — the page renders them in a sandboxed iframe.
- `GET /api/test` → `{"ok":true}` when the key works.

## Live data (worker.js + "This Season" tab)
- `GET /api/live/table?league=eng|esp|ita|ger|fra|tur` → current table (+ last-5 form) and
  `GET /api/live/club?league=..&id=<ESPN team id>` → this season's results (with goalscorers), next match and player stats
  (apps/goals/assists; saves/conceded/clean sheets for keepers). The worker fetches ESPN's public JSON
  (`site.api.espn.com`, no key), trims it and keeps it in memory for 10–30 min. If ESPN has no player stats it falls back
  to counting goals from the league match reports.
- The page matches our club names to ESPN's (`matchTeams()` in the template: exact tokens first, then fuzzy, each club once;
  add odd spellings to `TEAM_ALIAS`). Home page has a Clubs/Table switch; club pages have a "This Season" tab.

## Europe, Fantasy and Bracket pages (in the template, routes `#europe`, `#fantasy`, `#bracket`)
- `GET /api/live/cup?comp=ucl|uel` → league-phase table, knockout ties grouped by ESPN `season.slug` (aggregate + winner),
  recent results and next fixtures. Before the knockout draw the page shows a projected bracket from the table.
  ESPN teams are matched to our clubs with `matchAny()` (exact tokens, then fuzzy ≥ .7).
- Fantasy: Süper Lig draft league modelled on FPL Draft (snake draft, 2/5/5/3 squads, FPL points, H2H gameweeks).
  Matches are simulated with `fxMatch()` (same team ratings as the prediction model); projections come from two
  seeded simulated seasons. State lives in localStorage (`clubhub-fantasy-tur`).
- Dream Bracket: pick any of our clubs, two-legged ties + extra time + penalties, stored in `clubhub-mybracket`.

## Prediction model (in the template)
`teamRating()` (goal difference per game over the last 3 seasons + league level), `xiPenalty()`,
Poisson scorelines in `modelPredict()`, one sampled result per press (`simulate()`), goalscorers by
position weights (`GOAL_W`). The AI is told to stay within one goal of the simulated score.

## Private site
Every request goes through a Basic-Auth check in `worker.js` (`PW_HASH` = SHA-256 of `clubhub:<password>`;
`run_worker_first` is on so static files are protected too). Setting the Cloudflare text variable
`PUBLIC_SITE=yes` opens the site to everyone. The password itself is not stored anywhere in the repo.

## Legal / store readiness already done
`public/legal.html` (privacy policy, terms, data sources), "independent fan project / not betting advice"
footer, no club crests or logos, self-hosted fonts (`public/fonts`, OFL). Before an App Store release the app
needs real app features beyond the website (Apple guideline 4.2), a support email, and adult-owned
Apple Developer + Gemini accounts.

## Testing
Playwright + Chromium are handy: open `public/index.html` via `file://` and mock `**/api/analyze` with
`page.route`. For the worker, import `worker.js` in Node and call `default.fetch(new Request(...), env)`
with a fake `ASSETS` and a mocked global `fetch`.
