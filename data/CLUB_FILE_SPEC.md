# Club file spec (Club Hub football site)

Today is 4 October 2026. The season is 2026–27. Write ONE JSON file per club to
`/tmp/claude-0/-home-claude/31ea80f1-8148-579d-b337-3dd7b8e3fba3/scratchpad/hub/clubs/<id>.json`
(UTF-8, real accents, no ASCII escaping needed). Validate each with `python3 -c "import json;json.load(open(path))"`.

## Schema
```json
{"name":"Club display name","short":"3-letter code","league":"ger|fra|tur",
 "founded":"date or year","city":"City","nick":"Nickname (English gloss in brackets if non-English)",
 "stadium":"Stadium","cap":"capacity e.g. 34,700","coach":"Head coach as of Oct 2026",
 "colors":["#primary","#secondary","#dark shade of primary for backgrounds"],
 "honours":[["Label (e.g. Süper Lig titles)", count, "years, comma separated"]],
 "legends":[["Player","what they are known for (all-time top scorer, most appearances…)","value e.g. 228 goals"]],
 "records":[["short big value","what it means"]],
 "squad":[[shirtNo,"Full Name","GK|DEF|MID|FWD","NAT3",["roles"],age]],
 "starters":["11 names from squad, GK first, then defence R→L, midfield, attack"]}
```
- honours: 2–7 rows, most important first (league titles, domestic cups, European trophies, super cups, second-tier titles). For small clubs use promotions / second-tier titles / best finish / cup finals. Count must be an integer.
- legends: 3–6 rows. Include the club's all-time top scorer and most-appearances record holder if findable, plus iconic players.
- records: 3–4 rows, e.g. best league finish, record win, record attendance, notable European run, where they finished in 2025–26.
- squad: the CURRENT 2026–27 first-team squad (summer 2026 transfers included), ~24–32 players. shirtNo = integer, use 0 if unknown. NAT3 = FIFA 3-letter code (GER, FRA, TUR, BRA, ENG, NED, ESP, POR, BEL, SUI, AUT, CIV, SEN, MAR, ALG, NGA, GHA, CMR, MLI, COD, USA, JPN, KOR, CRO, SRB, …). roles = 1–3 from exactly this set, best position first:
  `GK CB RB LB RWB LWB DM CM AM RW LW ST`. age = integer age now (include whenever the source gives it; omit the 6th element only if unknown).
- starters: 11 names that exist in squad, a realistic first XI (1 GK, ~4 defenders, etc.).

## Sources (web access works through WebFetch / WebSearch only; the shell cannot reach websites)
1. Squad with ages (preferred, most current): `https://www.vavel.com/en-us/data/<slug>/squad` — guess slugs like `rc-lens`, `olympique-lyon`, `galatasaray`, `schalke-04`; if a slug 404s try variants or WebSearch "vavel <club> squad". Get shirt numbers from Wikipedia's "Current squad" section if vavel lacks them.
2. English Wikipedia club page (e.g. `https://en.wikipedia.org/wiki/FC_Schalke_04`) for founded, stadium, capacity, nickname, honours, records, current squad numbers, head coach. Also "List of <club> records and statistics" pages for top scorer / appearances.
3. Coach: confirm with the league's 2026–27 season Wikipedia article (e.g. `https://en.wikipedia.org/wiki/2026–27_Süper_Lig`, "Personnel and kits" / "Managerial changes") — use whoever is in charge now.
If a player clearly left in summer 2026 (Wikipedia transfers section), leave him out.

Do not invent players. If unsure about a detail, prefer omitting it to guessing. Work efficiently: one or two fetches per club for squad, one for club info.
Report back briefly: which files were written, squad sizes, and anything uncertain (e.g. coach not confirmed). Do not paste the files.
