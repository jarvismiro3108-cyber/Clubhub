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

## Europe, Bracket Simulator, Fantasy Draft (hash routes #europe, #bracket, #fantasy; `XPAGES` / `showX()`)
- Europe: `/api/live/table?league=ucl|uel` (league phase, zones set client-side: 1–8 R16, 9–24 play-offs) and
  `/api/live/cup?league=ucl|uel` (knockout legs Jan–Jun 2027 grouped into ties by round; round from ESPN notes or the
  UEFA date windows). No real ties yet → projected bracket from the table. European team names are matched against all
  114 clubs with `matchGlobal()` (confident matches only; foreign clubs stay unlinked).
- Brackets (`bracketTree()`): mirrored tree (R16 both sides → final + SVG trophy in the middle), connector lines are CSS
  borders on `.bpair`; below 760px it turns into a round-by-round list. Europe shows play-off ties in `tieGrid()` above it.
- Bracket Simulator: clubs are picked straight on the bracket (localStorage `clubhub-bracket`), `simTie()` plays two-legged
  ties + a one-match final (Poisson on `teamRating()`, extra time, penalties), rounds reveal with an animation.
- Fantasy Draft (Süper Lig): snake draft vs bots onto a pitch: 15 players = 2 GK, 5 DEF, 4 MID, 4 FWD (`FZ_Q`), i.e. a 4-3-3
  XI + one sub per position (`FZ_SLOTS`); each player owned once. After the draft the user swaps starters/subs, then a
  double round-robin league of simulated matches (`fzMatch()`: score, scorers, assists, cards, subs). No fantasy points:
  league table + leaders (goals, assists, clean sheets, yellow, red) and end-of-season awards. State: localStorage
  `clubhub-fantasy-tur` (v2). Real 2026/27 goals/assists from `/api/live/players?league=tur` are shown while drafting.
- Club "This Season" player stats: spotlight cards, goal-contributions chart (goals `--s-g` / assists `--s-a`, validated
  palette pair), player cards with a position filter, full sortable table folded in a `<details>`.


`teamRating()` (goal difference per game over the last 3 seasons + league level), `xiPenalty()`,
Poisson scorelines in `modelPredict()`, one sampled result per press (`simulate()`), goalscorers by
position weights (`GOAL_W`). The AI is told to stay within one goal of the simulated score.

## Design skills and docs
- `PRODUCT.md` (who the site is for, constraints) and `DESIGN.md` ("Floodlit Matchday": colours, type, components,
  do's and don'ts) are the design source of truth. Read them before UI work and keep `DESIGN.md` in sync when the
  look changes.
- Skills in `.claude/skills/`: `impeccable` (Apache-2.0; design commands such as audit, critique, polish, layout,
  typeset; its helper binary downloads from GitHub on first run; run
  `.claude/skills/impeccable/scripts/impeccable detect --json src/template.html` after UI changes),
  `make-interfaces-feel-better` (MIT; small polish details) and `web-design-guidelines` (our wrapper that fetches
  Vercel's MIT-licensed Web Interface Guidelines and audits `src/template.html`).
- Also installed: `ui-ux-pro-max` and its companions `design`, `design-system`, `brand`, `ui-styling`, `slides`,
  `banner-design` (MIT, via `npx ui-ux-pro-max-cli init --ai claude`; search with
  `python3 .claude/skills/ui-ux-pro-max/scripts/search.py "<query>"`), `frontend-design` (Anthropic, Apache-2.0) and
  `tailwindcss`, `react-three-fiber`, `motion-framer` (pasted by the owner; their bundled reference files are not
  included).
- **Precedence:** `DESIGN.md` and `PRODUCT.md` win over any skill's generic defaults (suggested palettes, fonts, "no
  uppercase labels" rules, etc.). Club Hub is one vanilla HTML/CSS/JS file: the Tailwind, shadcn/ui, React Three Fiber
  and Motion (Framer) skills only apply if the owner decides to move to that stack. Never add Tailwind, React or a
  framework just to follow a skill.

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
