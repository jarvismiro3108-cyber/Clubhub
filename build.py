"""Club Hub build script. Run from the repo root:  python3 build.py

Reads data/ (club files, league tables, coaches) and src/template.html, and writes public/index.html.
Build per-club data for Club Hub from clubs/*.json + league tables. Output: clubs_data.json"""
import hashlib
import json, glob, re, collections, unicodedata, os
ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = lambda *p: os.path.join(ROOT, 'data', *p)

LEAGUE_NAME = {'eng': 'Premier League', 'esp': 'La Liga', 'ita': 'Serie A', 'ger': 'Bundesliga', 'fra': 'Ligue 1', 'tur': 'Süper Lig'}
THREE_FROM = {'eng': 1981, 'esp': 1995, 'ita': 1994, 'ger': 1995, 'fra': 1994, 'tur': 1987}
SKIP = {'fenerbahce', 'konyaspor'}

def slug(n):
    n = unicodedata.normalize('NFD', n.replace('ı', 'i'))
    n = ''.join(c for c in n if unicodedata.category(c) != 'Mn').lower()
    return re.sub(r'[^a-z0-9]+', '', n)

# table name -> club id (only when it differs from the slug)
ALIAS = {
    'manchesterutd': 'manchesterunited', 'newcastleutd': 'newcastleunited', 'nothamforest': 'nottinghamforest',
    'tottenham': 'tottenhamhotspur', 'brightonhovealbion': 'brighton',
    'athleticclub': 'athleticbilbao', 'betis': 'realbetis', 'lacoruna': 'deportivolacoruna', 'racingsant': 'racingsantander',
    'inter': 'intermilan', 'internazionale': 'intermilan', 'milan': 'acmilan',
    'koln': '1fckoln', '1fckoln': '1fckoln', 'mgladbach': 'borussiamonchengladbach', 'eintfrankfurt': 'eintrachtfrankfurt',
    'leverkusen': 'bayerleverkusen', 'dortmund': 'borussiadortmund', 'freiburg': 'scfreiburg', 'tsghoffenheim': 'hoffenheim',
    'stuttgart': 'vfbstuttgart', 'fcaugsburg': 'augsburg', 'paderborn07': 'scpaderborn', 'mainz05': 'mainz05',
    'parissg': 'parissaintgermain',
    'istanbulbasaksehir': 'basaksehir', 'istanbulbb': 'basaksehir', 'bberzurumspor': 'erzurumspor', 'erzurumbb': 'erzurumspor',
    'gaziantepfk': 'gaziantep', 'caykurrizespor': 'rizespor',
}
EXCLUDE = {'cdmalaga', 'gaziantepspor'}  # different, older clubs

def team_id(name):
    name = re.sub(r'\s*\((C|R)\)$', '', name)
    s = slug(name)
    if s in EXCLUDE: return None
    return ALIAS.get(s, s)

# ---------- league tables: league -> season -> list of rows
tables = collections.defaultdict(dict)
notes = collections.defaultdict(list)   # (league, season) -> [(teamid, text)]
ct = json.load(open(DATA('computed_tables.json'), encoding='utf-8'))
for lg, ss in ct.items():
    for s, rows in ss.items():
        tables[lg][s] = [dict(id=team_id(r['team']), p=r['p'], g=r['g'], w=r['w'], d=r['d'], l=r['l'], gf=r['gf'], ga=r['ga'], pts=r['pts'], src='c') for r in rows]
for f in sorted(glob.glob(DATA('raw', '*.txt'))):
    lg, s = f.split('/')[-1][:-4].split('_')
    rows = []
    for line in open(f, encoding='utf-8'):
        line = line.strip()
        if not line: continue
        parts = line.split('|')
        if parts[0] == 'NOTE': notes[(lg, s)].append((team_id(parts[1]), parts[2])); continue
        if parts[0] == 'SEASONNOTE': notes[(lg, s)].append((None, parts[1])); continue
        p, t, g, w, d, l, gf, ga, pts = parts[:9]
        rows.append(dict(id=team_id(t), p=int(p), g=int(g), w=int(w), d=int(d), l=int(l), gf=int(gf), ga=int(ga), pts=int(pts), src='r'))
    tables[lg][s] = rows

def nxt(s):
    y = int(s[:4]) + 1
    return f'{y}-{str(y + 1)[2:]}'

# ---------- colours
def hx(c): c = c.lstrip('#'); return [int(c[i:i + 2], 16) / 255 for i in (0, 2, 4)]
def tohex(rgb): return '#' + ''.join(f'{max(0, min(255, round(v * 255))):02x}' for v in rgb)
def lum(c):
    def ch(v): return v / 12.92 if v <= .03928 else ((v + .055) / 1.055) ** 2.4
    r, g, b = hx(c); return .2126 * ch(r) + .7152 * ch(g) + .0722 * ch(b)
def contrast(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True); return (la + .05) / (lb + .05)
def mix(c, t, k): a, b = hx(c), hx(t); return tohex([x + (y - x) * k for x, y in zip(a, b)])
def darken_to(c, bg, target):
    k = 0
    while contrast(c, bg) < target and k < 1: k += .05; c2 = mix(c, '#000000', k); c = c2 if contrast(c2, bg) >= contrast(c, bg) else c
    return c
def lighten_to(c, bg, target):
    k = 0; base = c
    while contrast(c, bg) < target and k < 1: k += .05; c = mix(base, '#ffffff', k)
    return c

def colours(P, S, D):
    vivid = [c for c in (P, S) if .02 < lum(c) < .80]
    hi = vivid[0] if vivid else '#c9a227'
    hiInk = '#111111' if contrast(hi, '#111111') >= contrast(hi, '#ffffff') else '#ffffff'
    deep = D if lum(D) < .06 else mix(D, '#000000', .55)
    if lum(deep) > .06: deep = mix(deep, '#000000', .5)
    strong = darken_to(hi, '#ffffff', 4.5)
    strongDk = lighten_to(hi, '#16181d', 4.5)
    acc = hi if contrast(hi, deep) >= 3 else '#ffffff'
    s1, s2 = P, S
    if lum(P) > .85 and lum(S) > .85: s2 = '#111111'
    return dict(deep=deep, acc=acc, hi=hi, hiInk=hiInk, strong=strong, strongDk=strongDk, s1=s1, s2=s2, bar=strong, barDk=strongDk)

def ordinal(n): return f"{n}{'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')}"
def fmtS(s): return s.replace('-', '–')

TITLE_RE = re.compile(r"(league titles?|liga titles?|serie a titles?|bundesliga titles?|ligue 1 titles?|süper lig titles?|german (champions|titles?)|italian (titles|champions)|league title|bundesliga title|serie a title|la liga title|turkish football championship|spanish champions|french champions|english champions)", re.I)
NOT_TITLE = re.compile(r"(2\.|second|ligue 2|serie b|segunda|championship title|first league|best|runners|promotion|division 2|division title|u-1|amateur|youth|women)", re.I)

out = {}
for f in sorted(glob.glob(DATA('clubs', '*.json'))):
    cid = os.path.basename(f)[:-5]
    if cid in SKIP: continue
    c = json.load(open(f, encoding='utf-8'))
    lg = c['league']; LN = LEAGUE_NAME[lg]
    # seasons
    seasons = []
    for s in sorted(tables[lg]):
        row = next((r for r in tables[lg][s] if r['id'] == cid), None)
        if row: seasons.append((s, row))
    all_s = sorted(tables[lg])
    start = all_s[0]
    relegated = [s for s, r in seasons if nxt(s) in tables[lg] and not any(x['id'] == cid for x in tables[lg][nxt(s)])]
    lines = [f"{s}|{r['p']}|{r['g']}|{r['w']}|{r['d']}|{r['l']}|{r['gf']}|{r['ga']}|{r['pts']}" for s, r in seasons]
    club_notes = [f"{fmtS(s)}: {t}" for (l2, s), lst in notes.items() if l2 == lg for (tid, t) in lst if tid == cid]
    # honours
    hon = c.get('honours', [])
    title = next((h for h in hon if TITLE_RE.search(h[0]) and not NOT_TITLE.search(h[0])), None)
    trophies = [[h[1], h[0] + (f" ({h[2]})" if h[2] and len(h[2]) <= 40 else '')] for h in hon[:5]]
    if seasons: trophies.append([len(seasons), f"{LN} seasons since {fmtS(start)[:4]}"])
    first = cid not in [] and not seasons
    if title:
        titlesHead = f"{LN} Titles" if LN.lower() in title[0].lower() else 'League Titles'
        yrs = [y.strip() for y in re.split(r',\s*', title[2] or '') if y.strip() and not y.strip().startswith('incl')]
        chips = yrs if yrs else [fmtS(s) for s, r in seasons if r['p'] == 1]
        titlesText = f"{c['name']} have been champions {title[1]} time{'s' if title[1] != 1 else ''}." + (' The chips below are the title-winning seasons.' if chips else '')
    else:
        titlesHead = 'Big Moments'
        best = sorted(seasons, key=lambda x: (x[1]['p'], -x[1]['pts']))[:4]
        chips = [f"{ordinal(r['p'])} · {fmtS(s)}" for s, r in best]
        if seasons:
            b = best[0]
            titlesText = f"{c['name']} have not won the {LN} title. Their best finish in our tables (since {fmtS(start)}) is {ordinal(b[1]['p'])}, in {fmtS(b[0])}. The chips below are their best seasons."
        else:
            titlesText = f"2026/27 is {c['name']}'s first {LN} season in our tables (since {fmtS(start)}). The trophy cabinet above shows how they got here."
            chips = [h[0] for h in hon[:3]]
    cups = [f"{h[0]}: {h[2]}" for h in hon if h is not title and h[2]]
    # chart text
    if seasons:
        gaps = len(seasons) < len(all_s) - all_s.index(seasons[0][0])
        chartLede = (f"Every {LN} season for {c['name']} since {fmtS(start)}, when our tables begin." +
                     (' Gaps are seasons spent outside the top flight.' if gaps else '') +
                     (' Red bars are relegation seasons.' if relegated else '') + ' Hover a bar for details.')
    else:
        chartLede = ''
    tf = THREE_FROM[lg]
    sn = []
    if seasons and int(seasons[0][0][:4]) < tf: sn.append(f"Seasons before {tf}/{str(tf + 1)[2:]} gave 2 points for a win.")
    if any(r['src'] == 'c' for s, r in seasons): sn.append('Tables up to 2021–22 are rebuilt from every match result, so rare points deductions from those years are not included.')
    sn += club_notes
    # best seasons / snapshot
    def ppg(r): return (3 * r['w'] + r['d']) / max(r['g'], 1)
    if len(seasons) >= 3:
        bs = sorted(seasons, key=lambda x: -ppg(x[1]))[:10]
        apps = {'head': 'Best Seasons', 'sub': f'Top {LN} seasons since {fmtS(start)[:4]}, ranked by points per game (a win counted as 3 points in every era).',
                'rows': [[fmtS(s), f"{ordinal(r['p'])} · {r['w']}W {r['d']}D {r['l']}L · goals {r['gf']}–{r['ga']}", r['pts']] for s, r in bs]}
    else:
        sq = c['squad']; ages = [p[5] for p in sq if len(p) > 5 and p[5]]
        nat = collections.Counter(p[3] for p in sq)
        home = {'eng': 'ENG', 'esp': 'ESP', 'ita': 'ITA', 'ger': 'GER', 'fra': 'FRA', 'tur': 'TUR'}[lg]
        rows = [['Squad size', '2026/27 first team', len(sq)]]
        if ages: rows.append(['Average age', f'Youngest {min(ages)}, oldest {max(ages)}', round(sum(ages) / len(ages), 1)])
        rows.append(['Home-grown nationality', f'Players from {home}', nat.get(home, 0)])
        rows.append(['Foreign players', f'{len([n for n in nat if n != home])} countries', len(sq) - nat.get(home, 0)])
        top = [(n, k) for n, k in nat.most_common() if n != home][:1]
        if top and top[0][1] > 1: rows.append(['Top foreign nationality', top[0][0], top[0][1]])
        apps = {'head': 'Squad Snapshot', 'sub': 'Quick facts about the 2026/27 squad.', 'rows': rows}
    legends = {'head': 'Club Legends', 'sub': 'Record holders and icons.', 'rows': [list(x) for x in c.get('legends', [])][:10]}
    # records
    recs = [list(r) for r in c.get('records', [])]
    full = [(s, r) for s, r in seasons if r['g'] >= 30]
    if full:
        mp = max(full, key=lambda x: x[1]['pts']); mg = max(full, key=lambda x: x[1]['gf']); fc = min(full, key=lambda x: x[1]['ga'] / x[1]['g'])
        recs += [[f"{mp[1]['pts']} points", f"Most in a league season in our tables ({fmtS(mp[0])})"],
                 [f"{mg[1]['gf']} goals", f"Most league goals in a season ({fmtS(mg[0])})"],
                 [f"{fc[1]['ga']} conceded", f"Fewest league goals allowed in a season ({fmtS(fc[0])})"]]
    if c.get('cap') and not any(c['cap'] in r[0] for r in recs): recs.append([c['cap'], f"Capacity of {c['stadium']}"])
    # squad + pref
    sq = c['squad']
    names = {p[1] for p in sq}
    starters = [n for n in c.get('starters', []) if n in names]
    roles = {p[1]: p[4] for p in sq}
    pref = {}
    for role in ['GK', 'CB', 'RB', 'LB', 'RWB', 'LWB', 'DM', 'CM', 'AM', 'RW', 'LW', 'ST']:
        lst = [n for n in starters if role in roles[n]]
        lst += [n for n in starters if role not in roles[n] and n not in lst and roles[n] and roles[n][0] == role]
        pref[role] = lst
    meta = ' · '.join(x for x in [f"Founded {c['founded']}" if c.get('founded') else '', c.get('city', ''),
                                   f"“{c['nick']}”" if c.get('nick') else '',
                                   f"{c['stadium']} ({c['cap']})" if c.get('cap') else c.get('stadium', '')] if x)
    P, S, D = c['colors']
    out[cid] = dict(name=c['name'], short=c['short'][:4], league=lg, meta=meta, coach=c['coach'], stadium=c['stadium'],
                    colors=colours(P, S, D), trophies=trophies, titlesHead=titlesHead, titlesText=titlesText, titleChips=chips,
                    cupsNote='  ·  '.join(cups), chartLede=chartLede, seasonNote=' '.join(sn), relegated=relegated,
                    seasons='\n'.join(lines), threeFrom=tf, scorers=legends, apps=apps, records=recs[:9],
                    squad=[[p[0], p[1], p[2], p[5] if len(p) > 5 else None, p[3], p[4]] for p in sq],
                    pref=pref, starters=starters, squadNote='2026/27 squad')

coaches = json.load(open(DATA('coaches.json'), encoding='utf-8'))
for cid, d in out.items():
    if cid in coaches: d['coach'] = coaches[cid].replace(' (?)', '')
print(len(out), 'clubs')
for cid, d in out.items():
    if not d['seasons'] or len(d['starters']) < 11: print(' ', cid, 'seasons' if not d['seasons'] else '', len(d['starters']), 'starters')

tpl = open(os.path.join(ROOT, 'src', 'template.html'), encoding='utf-8').read()
assert '/*EXTRA_DATA*/' in tpl
# Speed: the page carries only what every club needs at once (name, colours, coach, the last three seasons for the
# strength model). The heavy parts (full history, records, squads) go into one file per league, loaded when needed.
LITE = ('name', 'short', 'league', 'meta', 'coach', 'stadium', 'colors', 'squadNote')
lite, heavy = {}, {}
for cid, d in out.items():
    lite[cid] = {k: d[k] for k in LITE if k in d}
    lite[cid]['seasons'] = '\n'.join(d['seasons'].split('\n')[-3:]) if d['seasons'] else ''
    heavy.setdefault(d['league'], {})[cid] = {k: v for k, v in d.items() if k not in LITE}
ddir = os.path.join(ROOT, 'public', 'data')
os.makedirs(ddir, exist_ok=True)
for f in os.listdir(ddir):
    if f.endswith('.json'): os.remove(os.path.join(ddir, f))
files = {}
for lg, clubs in sorted(heavy.items()):
    body = json.dumps(clubs, ensure_ascii=False, separators=(',', ':'))
    name = f"{lg}-{hashlib.sha1(body.encode()).hexdigest()[:10]}.json"  # content hash in the name, so browsers can keep it for good
    open(os.path.join(ddir, name), 'w', encoding='utf-8').write(body)
    files[lg] = 'data/' + name
data = json.dumps(lite, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
site = tpl.replace('/*EXTRA_DATA*/', 'const EXTRA=' + data + ';const LEAGUE_DATA=' + json.dumps(files) + ';')
# optional: a copy for the private Claude artifact version (uses Google Fonts, no doctype)
if os.environ.get('ARTIFACT_OUT'):
    open(os.environ['ARTIFACT_OUT'], 'w', encoding='utf-8').write(site)

# standalone copy for the public site (GitHub -> Cloudflare): needs its own doctype + charset
head = '<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n<meta name="theme-color" content="#0f1a3f">\n'
# self-hosted fonts on the public site (no requests to Google Fonts)
# Big Shoulders Display (stadium-signage headlines) and Libre Franklin (body), both variable weight, OFL
LAT = 'U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD'
LATX = 'U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1D00-1DBF,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF'
ff = ''
for fam, slug in [('Big Shoulders Display', 'big-shoulders-display'), ('Libre Franklin', 'libre-franklin')]:
    for sub, rng in [('latin', LAT), ('latin-ext', LATX)]:
        ff += (f"@font-face{{font-family:'{fam}';font-weight:100 900;font-style:normal;font-display:swap;"
               f"src:url(fonts/{slug}-{sub}.woff2) format('woff2');unicode-range:{rng}}}")
gl = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Big+Shoulders+Display:wght@100..900&family=Libre+Franklin:wght@100..900&display=swap">'
assert gl in site
site = site.replace(gl, ''.join(f'<link rel="preload" href="fonts/{f}-latin.woff2" as="font" type="font/woff2" crossorigin>\n' for f in ('big-shoulders-display', 'libre-franklin')) + '<style>' + ff + '</style>')
head += '<meta name="description" content="Independent fan site: history, records, squads and match predictions for every club in the top five European leagues and the Süper Lig.">\n'
open(os.path.join(ROOT, 'public', 'index.html'), 'w', encoding='utf-8').write(head + site + '\n</html>\n')
print('wrote public/index.html')
