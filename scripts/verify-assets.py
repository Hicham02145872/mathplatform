from pathlib import Path
import json, urllib.request
root=Path(__file__).resolve().parents[1]
docs=json.loads((root/'src/documents.json').read_text(encoding='utf-8'))
assert len(docs)>=120
assert len({d['id'] for d in docs})==len(docs)
pages=0
for d in docs:
 assert (root/'public'/d['url'].lstrip('/')).read_bytes().startswith(b'%PDF-')
 assert (root/'public'/d['cover'].lstrip('/')).is_file()
 for n in range(1,d['pages']+1):
  path=root/'public/pages'/d['id']/f'{n}.webp'
  assert path.is_file() and path.stat().st_size>500,(d['id'],n)
  pages+=1
assert pages==sum(d['pages'] for d in docs)
for path in ['/',docs[0]['url'],docs[0]['cover'],f"/pages/{docs[0]['id']}/1.webp",'/Maths-1bac-Lettres-PDF.zip']:
 with urllib.request.urlopen('http://127.0.0.1:5180'+path) as r:
  assert r.status==200
print('OK:',len(docs),'PDFs and covers,',pages,'pages, 5 HTTP responses.')
