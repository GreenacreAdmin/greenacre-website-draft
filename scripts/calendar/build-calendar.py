#!/usr/bin/env python3
"""Build the school calendar PDF from a dates file.

Usage: python3 scripts/calendar/build-calendar.py scripts/calendar/calendar-2026-27.json

Writes an HTML page next to the dates file, then prints it to the PDF named in
the dates file with Google Chrome (set CHROME=/path/to/chrome if it is not found).
After building, update the PDF's sha256 and bytes in assets/documents/originals.json.
"""
from pathlib import Path
from datetime import date, timedelta
import calendar, html, json, os, shutil, subprocess, sys

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
KEY = [  # (class, label) in the order shown in the key
    ('public-holiday', 'Public holiday'),
    ('school-holiday', 'School holiday'),
    ('teacher-training', 'Teacher training'),
    ('first-day', 'First day back at school'),
]


def expand(entries):
    """'2026-08-03' or '2026-08-03/2026-08-07' -> the dates, skipping weekends inside ranges."""
    days = set()
    for entry in entries:
        start, _, end = entry.partition('/')
        d, last = date.fromisoformat(start), date.fromisoformat(end or start)
        while d <= last:
            if not end or d.weekday() < 5:
                days.add(d)
            d += timedelta(days=1)
    return days


def month_table(year, month, term, kinds):
    weeks = calendar.Calendar(firstweekday=6).monthdayscalendar(year, month)
    rows = []
    for i in range(6):
        week = weeks[i] if i < len(weeks) else None
        cells = []
        for col in range(7):
            cls = ['weekend'] if col in (0, 6) else []
            day = week[col] if week else 0
            if day:
                for kind, days in kinds.items():
                    if date(year, month, day) in days:
                        cls.append(kind)
            cells.append(f'<td class="{" ".join(cls)}">{day or ""}</td>')
        rows.append(f'<tr{"" if week else " class=spare"}>{"".join(cells)}</tr>')
    head = ''.join(f'<th{" class=weekend" if i in (0, 6) else ""}>{d}</th>'
                   for i, d in enumerate(['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']))
    name = f'{calendar.month_name[month]} {year}'
    return (f'<table><caption><strong>{name}</strong> <span>{html.escape(term)}</span></caption>'
            f'<thead><tr>{head}</tr></thead><tbody>{"".join(rows)}</tbody></table>')


def build(data_file):
    data = json.loads(Path(data_file).read_text())
    kinds = {kind: expand(data['days'].get(kind, [])) for kind, _ in KEY}
    months = ''.join(month_table(*map(int, m['month'].split('-')), m['term'], kinds) for m in data['months'])
    key = ''.join(f'<li><i class="{kind}"></i>{label}</li>' for kind, label in KEY)
    page = HERE / 'calendar.html'
    page.write_text(TEMPLATE.replace('{{TITLE}}', html.escape(data['title']))
                    .replace('{{MONTHS}}', months).replace('{{KEY}}', key))
    chrome = os.environ.get('CHROME') or next((c for c in [
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        shutil.which('google-chrome'), shutil.which('chromium'), shutil.which('chrome')] if c and Path(c).exists()), None)
    if not chrome:
        sys.exit(f'Wrote {page}. Chrome not found: set CHROME=/path/to/chrome and run again.')
    out = ROOT / data['output']
    root_only = ['--no-sandbox'] if hasattr(os, 'geteuid') and os.geteuid() == 0 else []
    subprocess.run([chrome, '--headless', '--disable-gpu', '--no-pdf-header-footer', *root_only,
                    f'--print-to-pdf={out}', page.as_uri()], check=True, capture_output=True)
    print(f'Built {out.relative_to(ROOT)}. Now update its sha256 and bytes in assets/documents/originals.json.')


TEMPLATE = '''<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>{{TITLE}} | Greenacre International School</title>
<style>
@font-face{font-family:Comfortaa;font-weight:400;src:url(fonts/comfortaa-latin-400-normal.woff2)}
@font-face{font-family:Comfortaa;font-weight:700;src:url(fonts/comfortaa-latin-700-normal.woff2)}
@page{size:A4;margin:0}
*{box-sizing:border-box}
body{margin:0;width:210mm;height:297mm;padding:48px 0 44px 32px;font-family:Comfortaa,sans-serif;color:#1f2a22;display:flex;flex-direction:column}
header{height:168px;width:730px;text-align:center}
header img{height:84px;display:block;margin:0 auto}
header p{margin:.5mm 0 0;line-height:1.2;font-size:10pt;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#2f6b2a}
h1{margin:14px 0 0;font-size:21pt;line-height:1.2}
/* Grid sizes are even whole CSS pixels so every 1px line sits on the same grid and shows at one even weight. */
main{display:grid;grid-template-columns:repeat(3,225px);column-gap:27px;row-gap:19px;margin-top:16px;align-content:start}
table{border-collapse:separate;border-spacing:0;table-layout:fixed;font-size:9pt;text-align:center}
caption{height:26px;line-height:20px;padding:0;font-size:10.5pt;white-space:nowrap}
caption span{margin-left:1.5mm;font-size:8pt;font-weight:700;color:#2f6b2a}
th,td{width:32px;height:22px;padding:0;border:0 solid #7d827d;border-width:0 1px 1px 0}
th{height:25px;border-top-width:1px}
th:first-child,td:first-child{width:33px;border-left-width:1px}
th{font-size:7.5pt;font-weight:700;background:#ededed}
.weekend{background:#fde6cf}
th.weekend{background:#f9cfa5}
.school-holiday{background:#4a86e8;color:#fff;font-weight:700}
.public-holiday{background:#00a651;color:#fff;font-weight:700}
.teacher-training{background:#b6d7a8;font-weight:700}
.first-day{background:#ffe14a;font-weight:700}
tr.spare td{border:0;background:none}
footer{margin-top:auto;width:730px}
footer ul{display:flex;justify-content:center;gap:9mm;margin:0;padding:0;list-style:none;font-size:9pt}
footer li{display:flex;align-items:center;gap:2mm}
footer i{width:18px;height:18px;border:1px solid #7d827d}
</style></head><body>
<header><img src="../../assets/images/greenacre-logo.png" alt="Greenacre International School crest">
<p>Greenacre International School</p><h1>{{TITLE}}</h1></header>
<main>{{MONTHS}}</main>
<footer><ul>{{KEY}}</ul></footer>
</body></html>
'''

if __name__ == '__main__':
    build(sys.argv[1] if len(sys.argv) > 1 else HERE / 'calendar-2026-27.json')
