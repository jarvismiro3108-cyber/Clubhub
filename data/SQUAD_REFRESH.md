# Squad refresh task

Today is 4 October 2026 (season 2026–27). Club files live in
`/tmp/claude-0/-home-claude/31ea80f1-8148-579d-b337-3dd7b8e3fba3/scratchpad/hub/clubs/<id>.json`.
Read `SPEC.md` in the same folder for the schema. These clubs' squads were taken from older Wikipedia lists
and have no ages; some are missing summer-2026 signings or still list players who left.

For each club id you are given, ONLY refresh `squad` and `starters` (leave every other field as is):
1. WebFetch `https://www.vavel.com/en-us/data/<slug>/squad` (prompt: "List every player: shirt number, name, position, nationality, age").
   Slug guesses: lowercase hyphenated club name, e.g. `ac-milan`, `aston-villa`, `atletico-madrid`, `manchester-united`,
   `newcastle-united`, `athletic-bilbao`, `real-sociedad`, `deportivo-la-coruna`, `eintracht-frankfurt`, `bayer-leverkusen`,
   `borussia-dortmund`, `fc-augsburg`, `hamburger-sv`, `tottenham-hotspur`, `crystal-palace`, `leeds-united`, `ipswich-town`,
   `coventry-city`, `afc-bournemouth`/`bournemouth`, `brighton-hove-albion`/`brighton`, `brentford`, `celta-vigo`, `rayo-vallecano`,
   `real-betis`, `racing-santander`, `deportivo-alaves`/`alaves`, `cagliari`, `fiorentina`, `bologna`, `como`, `genoa`, `lazio`, `roma`/`as-roma`, …
   If it 404s/410s try one or two variants, then fall back to the club's English Wikipedia "Current squad" (check its date)
   and a WebSearch for clear summer-2026 departures.
2. Build the new squad: `[shirtNo, "Name", "GK|DEF|MID|FWD", "NAT3", [roles], age]`. Keep the roles from the old entry
   when the player was already there; choose 1–3 sensible roles (`GK CB RB LB RWB LWB DM CM AM RW LW ST`) for new players.
   Prefer the accented spelling the old file used for players who were already there (so names stay consistent).
   Vavel's "Position unlisted" → work out the group yourself. Drop players vavel lists as "Other" only if they are clearly coaches.
3. Rewrite `starters`: 11 names from the new squad, GK first, realistic first XI.
4. Save with `json.dump(d, open(p,'w'), ensure_ascii=False)` and re-load to validate.

Keep it efficient (one or two fetches per club). Do not invent players.
Report back in a few lines: per club, old size → new size and the source used; anything that failed.
