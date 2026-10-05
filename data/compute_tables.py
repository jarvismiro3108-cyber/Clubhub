"""Compute final league tables from FBref match results (worldfootballR_data) for complete seasons."""
import sys, json
sys.path.insert(0, '..')
from rds import read_rds
import pandas as pd

D = '../worldfootballR_data/data/match_results/'
LEAGUES = {'eng': ('ENG', ['Premier League']), 'esp': ('ESP', ['La Liga']), 'ita': ('ITA', ['Serie A']),
           'ger': ('GER', ['Fußball-Bundesliga', 'FuÃŸball-Bundesliga']), 'fra': ('FRA', ['Ligue 1']),
           'tur': ('TUR', ['Süper Lig', 'SÃ¼per Lig'])}
out = {}
for lid, (c, names) in LEAGUES.items():
    m = read_rds(D + f'{c}_match_results.rds')
    m = m[m.Competition_Name.isin(names) & (m.Gender == 'M')]
    m = m[m.Round.isna() | m.Round.astype(str).str.contains('Regular')]
    m = m[m.HomeGoals.notna() & m.AwayGoals.notna()]
    out[lid] = {}
    for y, s in m.groupby('Season_End_Year'):
        teams = sorted(set(s.Home) | set(s.Away))
        n = len(teams)
        expected = n * (n - 1)
        if len(s) < expected * 0.97:   # incomplete season
            continue
        first3 = {'eng': 1982, 'esp': 1996, 'ita': 1995, 'ger': 1996, 'fra': 1995, 'tur': 1988}[lid]
        win_pts = 3 if y >= first3 else 2
        rows = []
        for t in teams:
            h = s[s.Home == t]; a = s[s.Away == t]
            gf = int(h.HomeGoals.sum() + a.AwayGoals.sum()); ga = int(h.AwayGoals.sum() + a.HomeGoals.sum())
            w = int((h.HomeGoals > h.AwayGoals).sum() + (a.AwayGoals > a.HomeGoals).sum())
            d = int((h.HomeGoals == h.AwayGoals).sum() + (a.AwayGoals == a.HomeGoals).sum())
            g = len(h) + len(a)
            rows.append({'team': t, 'g': g, 'w': w, 'd': d, 'l': g - w - d, 'gf': gf, 'ga': ga, 'pts': win_pts * w + d})
        rows.sort(key=lambda r: (-r['pts'], -(r['gf'] - r['ga']), -r['gf']))
        for i, r in enumerate(rows): r['p'] = i + 1
        out[lid][f'{y-1}-{str(y)[2:]}'] = rows
    print(lid, list(out[lid])[:1], '...', list(out[lid])[-1], len(out[lid]))
json.dump(out, open('computed_tables.json', 'w'), ensure_ascii=False)
