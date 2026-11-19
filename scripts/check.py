from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
import os
root=Path(__file__).resolve().parents[1]/'dist'
class Inspect(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=[];self.lang='';self.direction='';self.canonical=[];self.alternates=[]
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='html':self.lang=a.get('lang');self.direction=a.get('dir')
  if 'id' in a:self.ids.append(a['id'])
  if tag in ['a','script','link','img']:
   url=a.get('href',a.get('src',''))
   if url.startswith('/'):self.links.append(url)
  if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a['href'])
  if tag=='link' and a.get('rel')=='alternate':self.alternates.append(a.get('hreflang'))
count=0
for lang in ['en','ar']:
 for p in (root/lang).rglob('index.html'):
  doc=Inspect();doc.feed(p.read_text());assert doc.lang==lang;assert doc.direction==('rtl' if lang=='ar' else 'ltr')
  assert len(doc.ids)==len(set(doc.ids)),f'Duplicate IDs: {p}'
  for link in doc.links:
   u=urlparse(link);target=root/u.path.lstrip('/')
   assert target.exists(),f'Broken link {p}: {link}'
   if u.fragment:
    dest=target/'index.html' if target.is_dir() else target
    d=Inspect();d.feed(dest.read_text());assert u.fragment in d.ids,f'Missing anchor: {link}'
  if os.getenv('SITE_URL'):
   assert len(doc.canonical)==1 and {'en','ar'}.issubset(doc.alternates)
  count+=1
assert count==30
for lib in ['qrcode.js','pdf-lib.min.js']:assert (root/'assets'/lib).stat().st_size>10000
print(f'PASS: {count} localized pages; internal links, fragments, language, direction, unique IDs and bundled libraries.')
