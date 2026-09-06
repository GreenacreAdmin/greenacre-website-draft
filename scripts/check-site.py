#!/usr/bin/env python3
"""Validate local routes, original PDF hashes and search metadata without modifying files."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote, urljoin
import hashlib,json,subprocess,sys
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__();self.links=[];self.ids=[];self.h1=0;self.robots='';self.canonicals=[];self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='meta' and a.get('name')=='robots':self.robots=a.get('content','')
        if tag=='link' and a.get('rel')=='canonical':self.canonicals.append(a.get('href'))
        for k in ('href','src'):
            if a.get(k):self.links.append((tag,k,a[k]))
errors=[]
aliases=json.loads((ROOT/'scripts/legacy-routes.json').read_text())
pages={p:Page(p.read_text()) for p in ROOT.rglob('index.html')}
for p,s in pages.items():
    path=p.parent.relative_to(ROOT).as_posix();path='' if path=='.' else path
    if len(s.ids)!=len(set(s.ids)):errors.append(f'{path}: duplicate IDs')
    if path not in aliases and s.h1!=1:errors.append(f'{path}: expected one h1')
    if path=='parent-information/secondary-parent-information':
        if s.robots!='noindex, nofollow':errors.append('Secondary parent indexing changed')
    elif len(s.canonicals)!=1:errors.append(f'{path}: expected one canonical')
    for tag,attr,url in s.links:
        u=urlsplit(url)
        if u.scheme or u.netloc:continue
        target=(ROOT/u.path.lstrip('/') if u.path.startswith('/') else p.parent/unquote(u.path)) if u.path else p
        target=target.resolve()
        if target.is_dir():target=target/'index.html'
        if not target.exists():errors.append(f'{path}: missing {url}');continue
        if u.fragment and target.suffix=='.html' and unquote(u.fragment) not in Page(target.read_text()).ids:
            errors.append(f'{path}: missing fragment {url}')
        # Compare resolution under both deployment layouts.
        if u.path and not u.path.startswith('/'):
            for base in ['https://preview.test/','https://preview.test/greenacre-website-draft/']:
                resolved=urljoin(base+(path+'/' if path else ''),url)
                if not resolved.startswith(base):errors.append(f'{path}: escapes deployment base: {url}')
for entry in json.loads((ROOT/'assets/documents/originals.json').read_text()):
    data=(ROOT/entry['file']).read_bytes()
    if hashlib.sha256(data).hexdigest()!=entry['sha256'] or len(data)!=entry['bytes'] or not data.startswith(b'%PDF-'):
        errors.append('Original PDF changed: '+entry['file'])
if errors:
    print('\n'.join(errors));sys.exit(1)
subprocess.run([sys.executable,str(ROOT/'scripts/update-search-metadata.py'),'--check'],check=True)
print(f'Checked {len(pages)} pages, all relative links and fragments at root/project paths, and 3 original PDF checksums.')
