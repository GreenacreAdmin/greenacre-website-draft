#!/usr/bin/env python3
"""Copy the shared header and footer from partials/ into every page, and write
the "Learning › Early Years" trail in each page banner from the menu.

Edit partials/header.html or partials/footer.html, then run this script.
{{ROOT}} becomes the relative path back to the site root ("", "../", "../../"),
and {{HOME}} the link to the homepage ("./" on the homepage itself).
--check reports pages that are out of date without changing them.
"""
from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parents[1]
BLOCKS = {
    'header': re.compile(r'<header class="site-header".*?</header>', re.S),
    'footer': re.compile(r'<footer aria-label="Greenacre International School footer" class="site-footer">.*?</footer>', re.S),
}

# Pages reached from another page rather than the menu: page -> the menu page it sits under.
TRAIL_PARENTS = {
    'documents/calendar': 'parent-information/calendar-term-dates/',
    'documents/fees': 'admissions/fees/',
    'documents/lunch-menu': 'parent-information/services/',
    'eca': 'learning/clubs-ecas/',
}
# Unlisted pages keep their original label so the trail does not expose them.
TRAIL_SKIP = {'academics/secondary-information', 'academics/secondary-start-of-year'}
HERO_LABEL = re.compile(r'(<section class="(?:page-hero|subhero)[^"]*"[^>]*>\s*<div class="wrap">\s*)'
                        r'(?:<div class="eyebrow">.*?</div>|<nav aria-label="Breadcrumb" class="eyebrow page-trail">.*?</nav>)', re.S)

def menu():
    """data-path -> (menu group, link label), read from the header partial."""
    items = {}
    for group in re.finditer(r'<div class="nav-drop">\s*<button[^>]*>(.*?)</button>(.*?)</div>\s*</div>', partial('header'), re.S):
        for path, label in re.findall(r'<a data-path="([^"]+)"[^>]*>(.*?)</a>', group.group(2)):
            items[path] = (group.group(1), label)
    return items

def trail(rel, prefix, text):
    """The 'Group › Page' trail shown in the page banner, built from the menu."""
    items = menu()
    sep = '<span class="page-trail__sep" aria-hidden="true">›</span>'
    key = rel + '/'
    if key in items:
        group, label = items[key]
        parts = [group, f'<span aria-current="page">{label}</span>']
    elif rel in TRAIL_PARENTS:
        parent = TRAIL_PARENTS[rel]
        group, label = items[parent]
        title = re.search(r'<h1[^>]*>(.*?)</h1>', text, re.S).group(1).strip()
        parts = [group, f'<a href="{prefix}{parent}">{label}</a>', f'<span aria-current="page">{title}</span>']
    else:
        return None
    return f'<nav aria-label="Breadcrumb" class="eyebrow page-trail">{f" {sep} ".join(parts)}</nav>'

def partial(name):
    text = (ROOT / 'partials' / f'{name}.html').read_text()
    return re.sub(r'^<!--.*?-->\n', '', text, flags=re.S).rstrip('\n')

def targets():
    aliases = json.loads((ROOT / 'scripts/legacy-routes.json').read_text())
    for page in sorted(ROOT.rglob('index.html')):
        if '.git' in page.parts: continue
        rel = page.parent.relative_to(ROOT).as_posix()
        rel = '' if rel == '.' else rel
        if rel in aliases: continue
        prefix = '../' * len(rel.split('/')) if rel else ''
        yield page, prefix, prefix or './', rel
    # The 404 page is generated from this template with an absolute base URL.
    yield ROOT / 'scripts/404-template.html', '@@BASE@@', '@@BASE@@', None

def build(check=False):
    stale = []
    for page, prefix, home, rel in targets():
        text = page.read_text()
        new = text
        for name, pattern in BLOCKS.items():
            block = partial(name).replace('{{ROOT}}', prefix).replace('{{HOME}}', home)
            if len(pattern.findall(new)) != 1:
                raise SystemExit(f'{page.relative_to(ROOT)}: expected one {name}')
            new = pattern.sub(lambda m: block, new)
        label = rel is not None and rel not in TRAIL_SKIP and trail(rel, prefix, new)
        if label:
            new = HERO_LABEL.sub(lambda m: m.group(1) + label, new, count=1)
        if new != text:
            stale.append(page.relative_to(ROOT).as_posix())
            if not check: page.write_text(new)
    return stale

if __name__ == '__main__':
    check = '--check' in sys.argv
    stale = build(check)
    if check and stale:
        raise SystemExit('Shared header/footer out of date (run scripts/build-shared.py): ' + ', '.join(stale))
    print('Shared header and footer verified.' if check else f'Updated {len(stale)} files.')
