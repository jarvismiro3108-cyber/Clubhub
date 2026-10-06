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
    fontFamily: "Barlow Condensed, Arial Narrow, sans-serif"
    fontSize: "clamp(40px, 7vw, 72px)"
    fontWeight: 800
    lineHeight: 0.92
    letterSpacing: "0.01em"
  headline:
    fontFamily: "Barlow Condensed, Arial Narrow, sans-serif"
    fontSize: "34px"
    fontWeight: 800
    lineHeight: 1
  title:
    fontFamily: "Barlow Condensed, Arial Narrow, sans-serif"
    fontSize: "24px"
    fontWeight: 700
    lineHeight: 1.1
  stat:
    fontFamily: "Barlow Condensed, Arial Narrow, sans-serif"
    fontSize: "46px"
    fontWeight: 800
    lineHeight: 1
  body:
    fontFamily: "Figtree, system-ui, sans-serif"
    fontSize: "15px"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Figtree, system-ui, sans-serif"
    fontSize: "11.5px"
    fontWeight: 600
    letterSpacing: "0.14em"
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
- Barlow Condensed uppercase for headings, numbers and scores; Figtree for everything you read.
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
  (dark: #3987e5 / #d95926).

### Named Rules
**The Gold Means Winning Rule.** Trophy Gold marks winners, champions, trophies and the current selection. Never use
it for decoration, warnings or ordinary buttons.

**The Results Are Reserved Rule.** Green, amber and red mean win, draw and loss. Never use them as general accents or
as a club's colour, and always pair them with W/D/L text.

## Typography

**Display Font:** Barlow Condensed (with Arial Narrow, sans-serif), self-hosted.
**Poster Font:** Archivo at 125% width, weight 800–900, home poster only (self-hosted).
**Body Font:** Figtree (with system-ui, sans-serif), self-hosted.

**Character:** a stadium scoreboard paired with a friendly modern sans: condensed uppercase for anything you glance
at, a warm readable sans for anything you read.

### Hierarchy
- **Display** (800, clamp(40px, 7vw, 72px), 0.92): the home hero only.
- **Headline** (800, 34px, 1): club and page names in the header, uppercase.
- **Title** (700, 24px): card headings, uppercase; section headings outside cards use the same style.
- **Stat** (800, 46–60px, 1): big numbers on stat boards, spotlight cards and scoreboards.
- **Body** (400, 15px, 1.5): paragraphs and lists, max about 65ch.
- **Label** (600, 11.5px, 0.14em, uppercase): eyebrows above headings and small captions.

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
- **Primary:** club colour (Floodlight Navy by default), uppercase Barlow Condensed 19px, 8px radius. One per area.
- **Secondary:** Surface Sunk with Ink text, Figtree 600; `.sm` for compact rows; disabled at half opacity.
- **On dark panels:** keep primary/secondary, but the primary becomes the navy button on a green or gold panel.

### Chips and segmented controls
- **Chips:** Surface Sunk pills, 12.5px semibold; the gold variant marks titles won.
- **Segmented control:** a pill track with the active option as a raised white pill (Clubs/Table, positions,
  competitions).

### Cards / Containers
- **Card:** Surface, 1px Line border, 10px radius, 18px padding, uppercase title.
- **Night panel:** Night Stand to Night Deep gradient, white text, gold accents, 14px radius (bracket, banners,
  awards, fantasy hero).
- **Spotlight card:** club-colour gradient with a huge faded shirt number, gold label, big stat.

### Tables
League tables use a coloured left edge for zones, a bold Pts column, W/D/L form squares, and hide secondary columns
on phones (`.hs` under 640px, `.hxs` under 420px). The user's own club or team row is tinted with the club colour.

### Navigation
Header tabs are uppercase Barlow Condensed on the dark header with a 4px accent underline for the active tab. Site
sections (Europe, Bracket Simulator, Fantasy Draft) are the feature tiles in the home hero; the league switcher is one
swipeable row of pills on phones. Club tabs scroll sideways on phones with a fade at the edge.

### Signature components
- **Club shirt badge:** each club is a small shirt drawn in its colours (body = first colour, sleeves and collar =
  second), with a thin outline so white or navy shirts never vanish. Used on club cards and the club header; it
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
  solid 6px bottom edge. The poster lettering uses **Archivo** (self-hosted, OFL) at 125% width and weight 800–900;
  nowhere else uses Archivo. Poster accents follow the club, so the Gold Means Winning rule applies outside it.
- **Home page colour world:** below the poster the whole home page (feature tiles, league heading, club cards,
  Clubs/Table switch, live table, footer) uses the poster's darker shade as its background, with tinted panels and
  white text; it recolours with the poster on every swap. The league heading uses the poster's wide Archivo.
  Club pages, Europe, Bracket and Fantasy keep the standard light/dark themes.
- **Feature tiles:** Europe, Bracket Simulator and Fantasy Draft are tinted tiles directly under the poster, each with its own small
  drawn picture (trophy, bracket, pitch); three across on desktop, a stacked list on phones.
- **Scoreboard:** navy block, team names either side, a dark inset score box, used for every match result.
- **Knockout tie card:** glassy dark card, club-colour stripe per row, winner row tinted gold with a gold score.
- **Pitch and shirts:** striped grass with circular two-colour shirts, name tags and a dugout bar for subs.
- **On-the-clock banner:** broadcast-style night panel with a live dot, big name and a gold progress bar.

## Do's and Don'ts

### Do:
- **Do** take each club's identity from its two colours and short code.
- **Do** keep tables, results and stats on calm light (or dark-mode) cards; save night panels for big moments.
- **Do** use tabular numbers and Barlow Condensed for scores and stats.
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
