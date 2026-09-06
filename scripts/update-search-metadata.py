#!/usr/bin/env python3
"""Regenerate search metadata. --launch prepares the custom-domain cutover; no network or git writes."""
from pathlib import Path
from urllib.parse import urlsplit
import argparse, html, json, re

ROOT=Path(__file__).resolve().parents[1]
DRAFT='https://greenacreadmin.github.io/greenacre-website-draft/'
LIVE='https://www.greenacre.ac.th/'

def outputs(base, launch=False):
    if not base.endswith('/'):
        raise ValueError('Base URL must end in /')
    aliases=json.loads((ROOT/'scripts/legacy-routes.json').read_text())
    urls=[]; result={}
    for page in sorted(ROOT.rglob('index.html')):
        if '.git' in page.parts: continue
        path=page.parent.relative_to(ROOT).as_posix()
        path='' if path=='.' else path
        source=page.read_text()
        hidden=path=='parent-information/secondary-parent-information'
        target=aliases.get(path,path+'/') if path else ''
        canonical=base+target.split('#')[0]
        source=re.sub(r'<link\b(?=[^>]*rel=[\"\']canonical[\"\'])[^>]*>\s*','',source,flags=re.I)
        if not hidden:
            source=source.replace('</head>',f'<link rel="canonical" href="{html.escape(canonical)}">\n</head>')
        if not hidden and path not in aliases:
            urls.append(canonical)
        result[page]=source
    result[ROOT/'sitemap.xml']='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'  <url><loc>{html.escape(url)}</loc></url>\n' for url in sorted(set(urls)))+'</urlset>\n'
    # Do not disallow the URL-only page: crawlers must read its noindex directive.
    result[ROOT/'robots.txt']='User-agent: *\nAllow: /\n\nSitemap: '+base+'sitemap.xml\n'
    result[ROOT/'404.html']=(ROOT/'scripts/404-template.html').read_text().replace('@@BASE@@',base)
    if launch:result[ROOT/'CNAME']=urlsplit(base).hostname+'\n'
    return result

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--launch',action='store_true',help='Use www.greenacre.ac.th and create CNAME only for the planned cutover')
    parser.add_argument('--check',action='store_true',help='Read-only comparison against generated files')
    args=parser.parse_args()
    launched=(ROOT/'CNAME').exists()
    expected=outputs(LIVE if args.launch or launched else DRAFT,args.launch or launched)
    changed=[]
    for p,text in expected.items():
        if not p.exists() or p.read_text()!=text:
            changed.append(str(p.relative_to(ROOT)))
            if not args.check:p.write_text(text)
    if args.check and changed:
        print('Metadata needs updating: '+', '.join(changed));raise SystemExit(1)
    print('Search metadata verified.' if args.check else 'Updated: '+', '.join(changed))
