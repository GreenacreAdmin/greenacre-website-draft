#!/usr/bin/env python3
"""Copy the shared header and footer from partials/ into every page.

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
        yield page, prefix, prefix or './'
    # The 404 page is generated from this template with an absolute base URL.
    yield ROOT / 'scripts/404-template.html', '@@BASE@@', '@@BASE@@'

def build(check=False):
    stale = []
    for page, prefix, home in targets():
        text = page.read_text()
        new = text
        for name, pattern in BLOCKS.items():
            block = partial(name).replace('{{ROOT}}', prefix).replace('{{HOME}}', home)
            if len(pattern.findall(new)) != 1:
                raise SystemExit(f'{page.relative_to(ROOT)}: expected one {name}')
            new = pattern.sub(lambda m: block, new)
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
