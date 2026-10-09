---
name: Club Hub
description: Floodlit-matchday fan site for 114 clubs — live tables, history and football games
colors:
  floodlight-navy: "#111a36"
  night-stand: "#0c1640"
  night-deep: "#050a1e"
  trophy-gold: "#ffd200"
  paper: "#f3f4f8"
  surface: "#ffffff"
  surface-sunk: "#e9ecf4"
  ink: "#0e1530"
  ink-soft: "#4a5272"
  muted: "#5f6787"
  line: "#d9ddea"
  night-paper: "#080d1c"
  night-surface: "#10172e"
  night-surface-sunk: "#182141"
  night-ink: "#eef0f8"
  night-line: "#253055"
  result-win: "#1f9d55"
  result-draw: "#c98a00"
  result-loss: "#d0423a"
  badge-win: "#17803f"
  badge-draw: "#a16207"
  badge-loss: "#c0352c"
  pitch-light: "#2f7d47"
  pitch-dark: "#2a7240"
  chart-goals: "#2a78d6"
  chart-assists: "#eb6834"
typography:
  display:
    fontFamily: "Big Shoulders Display, Arial Narrow, sans-serif"
    fontSize: "clamp(100px, 15vw, 224px)"
    fontWeight: 900
    lineHeight: 0.84
    letterSpacing: "0"
  headline:
    fontFamily: "Big Shoulders Display, Arial Narrow, sans-serif"
    fontSize: "clamp(26px, fit to width, 150px)"
    fontWeight: 900
    lineHeight: 0.88
  title:
    fontFamily: "Big Shoulders Display, Arial Narrow, sans-serif"
    fontSize: "clamp(27px, 3.2vw, 34px)"
    fontWeight: 900
    lineHeight: 1
  stat:
    fontFamily: "Big Shoulders Display, Arial Narrow, sans-serif"
    fontSize: "clamp(48px, 5.6vw, 66px)"
    fontWeight: 900
    lineHeight: 1
  body:
    fontFamily: "Libre Franklin, system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Big Shoulders Display, Arial Narrow, sans-serif"
    fontSize: "16px"
    fontWeight: 800
    letterSpacing: "0.04em"
rounded:
  sm: "6px"
  md: "8px"
  lg: "10px"
  xl: "14px"
  pill: "999px"
spacing:
  xs: "6px"
  sm: "10px"
  md: "16px"
  lg: "22px"
  page-gutter: "16px"
components:
  button-primary:
    backgroundColor: "{colors.floodlight-navy}"
    textColor: "{colors.surface}"
    typography: "{typography.title}"
    rounded: "{rounded.md}"
    padding: "10px 20px"
  button-secondary:
    backgroundColor: "{colors.surface-sunk}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    padding: "9px 14px"
  card:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: "18px"
  chip:
    backgroundColor: "{colors.surface-sunk}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "3px 10px"
  segmented-control:
    backgroundColor: "{colors.surface-sunk}"
    textColor: "{colors.ink-soft}"
    rounded: "{rounded.pill}"
    padding: "3px"
  scoreboard:
    backgroundColor: "{colors.floodlight-navy}"
    textColor: "{colors.surface}"
    rounded: "{rounded.lg}"
    padding: "16px 14px"
  night-panel:
    backgroundColor: "{colors.night-stand}"
    textColor: "{colors.surface}"
    rounded: "{rounded.xl}"
    padding: "18px 16px"
---

# Design System: Club Hub

## Overview

**Creative North Star: "Floodlit Matchday"**

Club Hub should feel like walking into a stadium for a night game: deep navy stands, the pitch lit up, gold reserved
for the moment someone wins. Every club page takes on that club's own colours, so the site is one stadium that
changes its home team. Big condensed uppercase type does the shouting, the way a scoreboard or a TV graphic would.

The energy is **balanced**. The exciting moments (match results, the knockout bracket, the trophy, the fantasy
draft's "on the clock" banner, season awards) get the full floodlit treatment: dark panels, gold, motion. The
everyday reading surfaces (league tables, results lists, stats tables, club history) stay calm, light and easy to
scan. The design is used mostly on phones, around matchdays.

**Key Characteristics:**
- Navy night panels and gold accents for big moments; calm light cards for reading.
- Club colours (two stripes) stand in for crests, which are never used.
- Big Shoulders Display (stadium signage) in capitals for headings, labels, numbers and scores; Libre Franklin (the
  sports-newspaper grotesque) for everything you read.
- Results always pair colour with a letter (W/D/L), never colour alone.
- Full light and dark themes; motion respects reduced-motion settings.

## Colors

A navy-and-gold matchday palette with neutral reading surfaces and a reserved set of result colours.

### Primary
- **Floodlight Navy** (#111a36): the default "home" colour for headers, the scoreboard and primary buttons. On a
  club page it is replaced by that club's deep colour (`--c-deep`, `--c-hi`).
- **Night Stand** (#0c1640) into **Night Deep** (#050a1e): the vertical gradient behind night panels (bracket,
  "on the clock" banner, fantasy hero, award cards).

### Secondary
- **Trophy Gold** (#ffd200): winners, champions, trophies, the selected pitch spot, eyebrow labels on dark panels,
  the "Hub" in the logo.

### Tertiary
- **Club colours**: each club's two kit colours (`colors.s1`, `colors.s2` in its data) shown as stripes on shirts,
  mini badges, bracket rows and card tints. They identify clubs; they never carry meaning like win or loss.

### Neutral
- **Paper** (#f3f4f8) / **Night Paper** (#080d1c): page background, light / dark.
- **Surface** (#ffffff) / **Night Surface** (#10172e): cards and sheets.
- **Surface Sunk** (#e9ecf4) / **Night Surface Sunk** (#182141): table headers, chips, inactive buttons, list rows.
- **Ink** (#0e1530), **Ink Soft** (#4a5272), **Muted** (#5f6787; dark mode #8e96b6): text by importance, all at least
  4.5:1 on their backgrounds; **Line** (#d9ddea) borders.

### Result and data colours
- **Win** (#1f9d55), **Draw** (#c98a00), **Loss** (#d0423a): match outcomes and form guides only (dark-mode steps
  are brighter: #34c172, #e2a72a, #ef6a60). League-table zone edges reuse them (European places / relegation).
  Badges with white W/D/L letters use the deeper **badge** steps (#17803f, #a16207, #c0352c) in both themes so the
  letters stay readable.
- **Pitch** (#2f7d47 / #2a7240): the striped grass behind lineups.
- **Chart goals** (#2a78d6) and **chart assists** (#eb6834): the validated pair for goal-contribution bars
  (dark: #3987e5 / #d95926). On club pages the bars are white (goals) and half-white (assists) so they read on
  any club colour.
- **Club-page result colours:** on club pages win/draw/loss text is lightened per club (`posterPalette()` returns
  `win`, `draw`, `loss`) until it reads at 4.6:1 on the lightest club card; the probability bar then uses dark text.

### Named Rules
**The Gold Means Winning Rule.** Trophy Gold marks winners, champions, trophies and the current selection. Never use
it for decoration, warnings or ordinary buttons.

**The Results Are Reserved Rule.** Green, amber and red mean win, draw and loss. Never use them as general accents or
as a club's colour, and always pair them with W/D/L text.

## Typography

**Display Font:** Big Shoulders Display (variable 100–900, with Arial Narrow, sans-serif), self-hosted, OFL.
**Body Font:** Libre Franklin (variable 100–900, with system-ui, sans-serif), self-hosted, OFL.

**Character:** stadium signage and the sports pages. Tall, tight Big Shoulders capitals for anything you glance at
(titles, labels, scores, shirt lettering, tabs, buttons); Libre Franklin, a Franklin Gothic revival, for anything you
read. Two families only; the old Barlow Condensed, Figtree and Archivo were dropped because they read as generic.

**Named Rules.** *No tiny spaced-out capitals*: a label is either a short Big Shoulders cap line at 15px or more with
light tracking (0.03–0.05em), or plain sentence case in Libre Franklin. *No middle-dot meta strings*: join facts
with words, commas or line breaks (the club details line in the header is a wrapped row of separate facts).
*Headlines track at 0*, never negative; condensed caps need room, not squeezing.

### Hierarchy
- **Display** (900, clamp(100px, 15vw, 224px), 0.84): the home poster headline.
- **Headline** (900, fitted to width up to 150px, 0.88): club and page names in the poster headers.
- **Title** (900, 27–34px): card headings and section headings, capitals.
- **Stat** (900, 48–88px): stat tiles, spotlight numbers, scoreboards; tabular figures.
- **Label** (800, 15–18px, 0.03–0.05em, capitals): kickers, table headers, tabs, buttons, small tile headings.
- **Body** (400, 15px, 1.5): paragraphs and lists, max about 65ch; metadata and helper text in sentence case.

### Named Rules
**The Numbers Line Up Rule.** Every score, table and stat uses tabular numerals (`.num` / `font-variant-numeric`).

## Layout

Single column of cards inside a centred 1120px container with a 16px side gutter; cards stack with a 22px gap.
Two-up grids (`.two`, auto-fit, min 360px) collapse to one column on phones. Wide content (league tables, the
bracket) scrolls inside its own panel, never the page: no horizontal page scroll at 390px. The knockout bracket
is a mirrored tree on desktop and becomes a round-by-round list below 760px. Pickers open as a bottom sheet on
phones (under 600px) and a centred dialog on larger screens.

## Elevation & Depth

Mostly flat, with tonal layering: surfaces are separated by background steps and 1px lines rather than shadows.
Shadows appear only where something floats or is the star: sheets, hovered club cards, bracket ties, the final.

### Shadow Vocabulary
- **Lift** (`box-shadow: 0 8px 20px rgba(10,20,50,.12)`): club cards on hover.
- **Tie** (`box-shadow: 0 6px 18px rgba(0,0,0,.35)`): bracket tie cards on night panels.
- **Gold glow** (`box-shadow: 0 10px 34px rgba(255,190,0,.22)` / trophy drop-shadow): the final and the trophy only.
- **Sheet** (`box-shadow: 0 20px 50px rgba(0,0,0,.35)`): picker sheets and dialogs.

### Named Rules
**The Flat Until It Matters Rule.** Reading surfaces stay flat; only floating layers and winning moments get depth.

## Shapes

Soft rectangles: 10px cards, 8px buttons and inputs, 14px for large hero panels and sheets, full pills for chips,
league switches and segmented controls. Circles are reserved for shirts and club badges. Night panels may carry a
faint diagonal or vertical stripe texture, like a mown pitch or stadium stands.

## Components

### Buttons
- **Primary:** club colour (Floodlight Navy by default), uppercase Big Shoulders Display, 8px radius. One per area.
- **Secondary:** Surface Sunk with Ink text, Libre Franklin 600; `.sm` for compact rows; disabled at half opacity.
- **On dark panels:** keep primary/secondary, but the primary becomes the navy button on a green or gold panel.

### Chips and segmented controls
- **Chips:** Surface Sunk pills, 12.5px semibold; the gold variant marks titles won.
- **Segmented control:** a pill track with the active option as a raised white pill (Clubs/Table, positions,
  competitions).

### Cards / Containers
- **Card:** Surface, 1px Line border, 10px radius, 18px padding, uppercase title.
- **Night panel:** the page's darkest shade (`--p-page`) with a soft glow of the poster colour at the top and a faint
  gold glow at the bottom, white text, gold accents, 20px radius (the knockout bracket).
- **Poster tile:** the poster colour with the darker curve, white Big Shoulders label and a giant Big Shoulders headline
  (bracket champion card, fantasy hero, draft clock, fantasy awards with the number in the poster accent colour).
  "Your turn" on the draft clock is a solid tile in the page accent colour; season champions get a deep gold tile
  (#3d2c05 to #86650b) so white text stays readable.
- **Spotlight card:** a mini poster in the club's poster colour with the darker curve, the player's own shirt tucked
  in the corner, white label and name, and the big stat in the poster accent colour.

### Tables
League tables use Big Shoulders uppercase column headers, tabular figures, 1px row separators with a subtle hover tint,
a coloured left edge for zones, a big Big Shoulders Pts column, W/D/L form squares, and hide secondary columns
on phones (`.hs` under 640px, `.hxs` under 420px). The user's own club or team row is tinted with the club colour and
carries a white left accent bar (also highlighted in the home league table, not only on club pages).

### Navigation
Club pages and the Europe, Bracket and Fantasy pages use Big Shoulders pill tabs: outlined white on the poster colour, the active one solid white
with poster-colour text and a 4px bottom edge. Site
sections (Europe, Bracket Simulator, Fantasy Draft) are the feature tiles in the home hero; the league switcher is one
swipeable row of pills on phones. Club tabs scroll sideways on phones with a fade at the edge.

### Signature components
- **Club shirt badge:** each club is a small shirt drawn in its colours (body = first colour, sleeves and collar =
  second), with a thin outline so white or navy shirts never vanish. Used on club cards (the club header shows the big poster shirt); it
  replaces crests entirely.
- **Home poster:** the home header is a sports poster coloured from the featured club's shirt (`posterPalette()`,
  OKLCH): a deeper or brighter shade of the shirt colour; for yellow or white shirts the club's second colour (e.g.
  Fenerbahçe yellow on navy); for black-and-white kits a dark slate. The first candidate where the shirt clearly
  stands out (contrast at least 1.6 against the background) wins, and every background keeps white text at 4.6:1 or
  more. A darker shade draws the big background curve and the button's 3D edge; "2026/27" uses the club's other
  colour when it reads, else a light tint. A giant shirt seen from the back is the figure (club name and 26, printed
  in the second colour or in white/black when that would not show); the wide heavy CLUB HUB headline overlaps it;
  vertical rails run down both edges; the round SWAP CLUB sticker steps through the league's clubs in alphabetical
  order (wrapping round) and each league remembers its last shirt; a chunky white "Open <club>" pill button has a
  solid 6px bottom edge. The poster lettering is Big Shoulders Display 900 at a very large size. Poster accents follow the club, so the Gold
  Means Winning rule applies outside it.
- **Home page colour world:** below the poster the whole home page (feature tiles, league heading, club cards,
  Clubs/Table switch, live table, footer) uses the poster's darker shade as its background, with tinted panels and
  white text; it recolours with the poster on every swap. The league heading uses the poster's Big Shoulders.
- **Europe, Bracket Simulator, Fantasy Draft:** the same poster header (giant page title, figure on the right, pill
  tabs) and the same tinted colour world as club pages (`body.on-x`), each with its own palette (`XPAL`, run through
  `posterPalette()`): Champions League royal blue and Europa League burnt orange (the page recolours when you switch
  competition; the figure is a glowing gold trophy); the Bracket Simulator night violet with a white "CHAMPION ?"
  mystery shirt until you simulate, then the whole page takes the champion's colours and the figure becomes the
  champion's shirt (number 1) with the trophy; Fantasy Draft in the user's own team colours (ten two-colour kits in
  `FZ_KITS`, Red & Gold by default, picked on the setup screen and changeable later) with a shirt printed with the
  team name (live while typing) and 11. Kits use `posterPalette(c,{accFirst:true})`, which darkens the background until
  the kit's second colour reads as the accent. "Your pick" highlights (draft clock, open spots on the pitch, selected
  player, stat badges) use the page accent (`--p-acc`, with `--p-accink` for text on it; `--p-ring` falls back to white
  when the accent would vanish on the grass), never a fixed yellow.
- **Club pages:** every club page (Club & Records, This Season, Squad Picker, Match Analysis) uses the same colour
  world, built from that club's `posterPalette()`. The header is a poster: the poster colour with the darker curve, the
  club name in giant Big Shoulders capitals (sized from the longest word with container units so words never break), and the big
  club shirt on the right (beside the club details on phones). Below it the page background is `page`, a shade of
  the club colour dark enough that muted text (72% white) reads on the lightest card (15% white); cards are tinted
  panels with white text and 16px corners. Trophy cabinet and This Season stat tiles are small posters (poster colour,
  curve, big number in the poster accent colour). Primary buttons and segmented controls are white pills with a solid
  bottom edge. The points chart reads its colours from the page: champions white, top three light, the rest faint,
  relegation in the lightened loss colour. The browser's theme colour follows the club.
- **Player cards (sticker album):** each player in "The Squad" gets a card with his own shirt (surname and number, in
  the club's colours) on a poster-colour panel, a coloured position dot (GK amber, DEF blue, MID green, FWD coral), the
  name in Big Shoulders capitals and a three-number stats row split by thin lines (zeros muted). Players without an
  appearance have a greyed shirt panel; four or more goal contributions earn a tilted yellow "On fire" sticker.
- **First-visit welcome:** a full-screen night panel (navy-to-deep gradient) shown only on a first visit with no
  favourite club: gold "Welcome to" kicker, giant Big Shoulders "CLUB HUB", one line of what the site is, a gold primary
  button ("Choose my club", 3D bottom edge) and a ghost "Just having a look", then three feature rows (live scores,
  Squad Picker & Predict, History & records) each with a gold line-icon. Dismissed either way it never shows again.
- **My club card (home):** a wide poster tile in the favourite club's colours (shirt on the left, giant name, "Change"
  and "Share" links) with three dark inset tiles: Table, Last match (W/D/L badge + score) and Next match; links open the
  season tab or the match centre. A full-width **storyline chip** (gold pennant icon) sits under the tiles with one
  sentence a fan would say, read from the data — a winning/unbeaten/winless run, top of the league, a European place, a
  relegation scrap, or the last result. "Share" draws a poster share card. Without a favourite it is a dashed "Choose
  your club" button. Club pages have a small star pill in the header (white when it is your club).
- **Storyline chip:** a small inset row (spark/pennant icon in the accent colour, one sentence) that turns numbers into
  context. Used under the My club card and on the match preview's prediction card (recent head-to-head record, or the
  table gap between the sides). Only shown when the data says something worth saying.
- **Matchday list (home):** a round refresh button (kept clear of the fixed menu button on phones) sits by the heading;
  day pills (Yesterday to five days ahead, same style as the league pills). Each competition is a labelled section — a
  header button (accent tick, Big Shoulders name, red live dot, match count, chevron; folded unless live, your league or
  one of the first two) — above its matches, which are **framed fixture cards** rather than table rows: a bordered,
  rounded panel with a soft top-light gradient and a lift on hover. Each card stacks a small centred status strip
  (KICK-OFF / FULL TIME / live minute) over a scoreboard row — home badge+name at the far left, away name+badge at the far
  right, a Big Shoulders score chip centred between them (kick-off time in the chip's place before the match). Live cards
  gain a red frame and red score chip; a score that changes on refresh bumps up and flashes gold.
- **Pitch shirts (Squad Picker, Predict, Fantasy):** round numbered shirts split in the club's first colour and a
  slightly darker half, ringed in the second colour, number in black or white for contrast (same family as the match
  centre's line-up chips). On Predict the opponent pitch is centred on its own (no repeated list of picked names
  beside it, just a one-line status under it), and the home team is shown as a compact "formation · XI set · bench"
  summary rather than a list of all eleven names.
- **Menu:** a round 46px button fixed top right in the poster colour with a white ring and a 4px bottom edge (three bars
  that turn into a cross); it opens a right-hand drawer in the page's dark shade: Club Hub wordmark, search bar, a my-club
  tile in its colours, big Big Shoulders links (Home, Matchday, Europe, Bracket Simulator, Fantasy Draft), league pills,
  recently viewed clubs and small legal links.
- **Confirm dialog:** destructive actions (e.g. Fantasy "New draft") use an on-brand centred dialog over a blurred
  scrim — Big Shoulders title, a plain-language warning, a secondary "keep it" button and a white primary pill — never
  the browser's native `confirm()`. Keyboard-accessible (Escape closes, focus trapped) and themed from the current page.
- **Player page (detailed):** poster header and a "This Season" poster panel with big accent-coloured numbers (apps,
  minutes, goals, assists, xG, xA) and a row of per-90 rates shown by default; everything else (percentile bars, the
  shot map, match-by-match, season-by-season, the details list and teammates) is folded behind a full-width
  "Full stats & profile" toggle so the page opens clean. Percentile bars rank against league players in the same
  position (blue 80+, green 60+, orange 40+, red below, number in a matching badge); the half-pitch shot map has goals
  filled in the accent colour, saved blue, missed white outline, blocked dashed, size = xG; season-by-season rows carry
  goals vs xG bars.
- **Match shot map (interactive):** both teams on one pitch in their colours (home shoots right); shots are small
  tappable circles (size = xG, goals filled). Tapping one rings it gold and opens a detail panel below the pitch —
  player, team, minute, result, xG and where the shot came from (inside / edge / outside the box), plus the assist —
  with prev/next arrows that step through every shot in the match minute by minute. Below it, the list of players with
  the most xG + xA.
- **Search:** a round magnifier button fixed at the top of the home page, sitting left of the menu button and matching
  it (poster-filled circle, white ring), plus a round magnifier button in every poster header; results open in the bottom
  sheet, which takes the page colours (home included): clubs first, then players with a numbered shirt circle in their
  club colours and a Club/Player tag.
- **Player page:** the club page's poster header with the player's name as the giant title and his own shirt (surname
  and number); stat tiles (apps, goals, assists or saves/clean sheets), goals match by match, a profile list and
  teammates as chips.
- **Share card (1080×1350 image):** poster colour with the darker curve, CLUB HUB and the date top left/right, the shirt(s)
  as the figure, a giant Big Shoulders title, a sentence line, up to three dark stat boxes and a small footer. Always
  says "just for fun, not betting advice" for simulations.
- **Match preview:** prediction bar (home colour / grey draw / away colour) with the likeliest score, two form-and-table
  tiles, head-to-head totals and the list of meetings.
- **Kit wall (home club list):** every club is a tall tile in its own poster colour (`posterPalette()`) with the darker
  curve, its big shirt hanging at the top and its name in Big Shoulders capitals with the coach underneath; two columns
  on phones. Replaces the old identical grey list cards.
- **Match centre:** a poster scoreboard (both shirts, giant score, goalscorers, venue) in the page colours of the club
  you came from, then pill tabs: Facts (player of the match tile, then a two-sided timeline with minutes down the
  middle), Line-ups (both teams on one tall pitch, round number shirts in team colours, rating badges: 8+ blue
  #1a64d8, 7+ green #17803f, 6+ orange #a8560f, under 6 red #c0352c, player of the match ringed in gold; benches
  below) and Stats (possession split bar, then FotMob-style rows: values in pills, the better side's pill filled with
  its team colour, a two-colour bar underneath). xG and ratings are always labelled as Club Hub estimates.
- **Feature tiles:** Europe, Bracket Simulator and Fantasy Draft are tiles directly under the poster, each with its own small
  drawn picture (trophy, bracket, pitch); three across on desktop, a stacked list on phones. They sit in the home colour
  world but each carries a per-competition accent (Champions blue, Bracket violet, Fantasy green) on its corner glow,
  border and icon panel, so the three read as distinct; the icon lifts and tilts on hover.
- **Skeleton loaders:** while live data loads, surfaces show a shimmer skeleton in the shape of what's coming (My Club
  tiles, Matchday league cards, club/season/match/player cards, the live table) instead of a spinner or blank — tinted
  from the current text colour so it works in every colour world; the shimmer stops under `prefers-reduced-motion`.
- **Reveal on scroll:** home sections (My Club, Matchday, the feature tiles, the league heading and the club grid),
  and the club-page tab panels, match centre and player page,
  ease up and fade in the first time they come near the viewport, once per load. A scroll/resize check guarantees nothing
  is ever left hidden, and `prefers-reduced-motion` shows everything immediately.
- **Scoreboard:** navy block (the poster colour on club pages), team names either side, a dark inset score box, used for every match result.
- **Knockout tie card:** glassy card on the night panel, club-colour stripe per row, winner row tinted gold with a gold score.
- **Pitch and shirts:** striped grass with circular two-colour shirts, name tags and a dugout bar for subs.
- **On-the-clock banner:** poster tile with a live dot, big name and a progress bar (solid gold when it is your pick).

## Do's and Don'ts

### Do:
- **Do** take each club's identity from its two colours and short code.
- **Do** keep tables, results and stats on calm cards (light/dark themes, or the club's tinted panels on club pages);
  save night panels for big moments.
- **Do** use tabular numbers and Big Shoulders Display for scores and stats.
- **Do** pair every win/draw/loss colour with a W/D/L letter.
- **Do** check every screen at 390px and 1280px, in light and dark, with no horizontal page scroll.
- **Do** give animations a `prefers-reduced-motion` fallback.
- **Do** theme browser surfaces: gold text selection, club-colour caret and focus (gold on dark panels), styled
  dropdown arrows, quiet scrollbars.

### Don't:
- **Don't** use club crests, league logos or official marks, or anything that imitates them.
- **Don't** show build status to visitors (no "ready", "open" or "soon" tags).
- **Don't** use Trophy Gold for anything but winners, trophies and the current selection.
- **Don't** use the win/draw/loss colours as decoration or as a club colour.
- **Don't** make whole pages loud: a page gets at most one or two night panels.
- **Don't** introduce a second styling system or framework; the site is one vanilla HTML/CSS/JS file.
