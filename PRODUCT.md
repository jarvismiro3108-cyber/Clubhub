# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Football fans in general: people who follow Europe's top five leagues or the Süper Lig and want one place for
history, records, current form and football games. They mostly visit on their phones, often around matchdays,
to check a table or result, explore a club, or play a quick game (simulate a match, a knockout, a draft league).

## Product Purpose

Club Hub brings each of the 114 clubs in the Premier League, La Liga, Serie A, Bundesliga, Ligue 1 and Süper Lig
into one fan site: club history and records, 2026/27 squads, live tables, results and player stats, and playful
tools built on that data. Success is a fan coming back on matchday because it is quicker and more fun than
juggling several apps and sites.

## Positioning

An independent fan project that joins deep club history with live 2026/27 data and simulations in one place,
with equal care for the Süper Lig and the big five leagues.

## Operating Context

- Live data (tables, results, goalscorers, player stats, Champions League and Europa League) comes from ESPN's
  public feed through the site's Cloudflare Worker, refreshed every few minutes; it can be briefly unavailable.
- Games: a squad picker, a match analysis that simulates a match (optionally with Gemini AI and Google Search), a
  16-club knockout bracket simulator, and a Süper Lig fantasy draft league against bot managers.
- The site is currently password-protected and shared privately; it may open to the public later.

## Capabilities and Constraints

- One-file vanilla front end (`src/template.html`, built to `public/index.html` by `build.py`); no framework,
  no build-time CSS tooling. Hosted as a Cloudflare Worker on the free tier.
- Gemini free tier is not offered in the EEA, Switzerland or the UK; those visitors get the built-in simulation.
- Undecided: a possible App Store release later, which would need app-only features (Apple guideline 4.2), a
  support email, and adult-owned Apple Developer and Gemini accounts.

## Brand Commitments

- Name: Club Hub. Presented as an independent fan project, not affiliated with any club, league or player.
- No club crests or official logos anywhere; clubs are shown by name, short code and their colours only.
- Simulations and predictions are "for fun", never betting advice, and must say so.

## Evidence on Hand

- Club data: `data/clubs/*.json` (112 clubs) plus Fenerbahçe and Konyaspor in the template; season tables in
  `data/raw/` and `data/computed_tables.json`; coaches in `data/coaches.json`.
- Live 2026/27 data via `/api/live/*`. No testimonials, user numbers or press exist; do not invent any.

## Product Principles

1. Real data first: show live or sourced facts, label simulations clearly, and never present a guess as fact.
2. Matchday on a phone: every feature must work well one-handed on a small screen.
3. Every club gets the same care, from Real Madrid to the newest promoted Süper Lig side.
4. Fun on top of facts: games and simulations should feel exciting, but tables and stats stay easy to read.

## Accessibility & Inclusion

Works in light and dark mode, respects reduced-motion settings, and never relies on colour alone for meaning
(results use W/D/L letters as well as colour).
