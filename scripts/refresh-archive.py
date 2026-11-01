from pathlib import Path
import json,zipfile,html,time
root=Path(__file__).resolve().parents[1]
docs=json.loads((root/'src/documents.json').read_text(encoding='utf-8'))
target=root/'public/Maths-1bac-Lettres-PDF.zip'
temp=target.with_suffix('.building.zip')
rows=''.join('<li><a href="documents/'+html.escape(d['id'])+'.pdf">'+html.escape(d['title'])+' — '+html.escape(d['subtitle'])+'</a></li>' for d in docs)
index='<!doctype html><html lang="fr"><meta charset="utf-8"><title>Folio by Hicham</title><style>body{font:16px/1.8 system-ui;max-width:1000px;margin:40px auto;padding:20px;color:#172d49}li{margin:12px 0}a{color:#285cc9}</style><h1>Folio by Hicham</h1><p>'+str(len(docs))+' documents de mathématiques · 1ère bac Lettres et Sciences humaines.</p><ul>'+rows+'</ul></html>'
with zipfile.ZipFile(temp,'w',zipfile.ZIP_DEFLATED) as archive:
 for d in docs:archive.write(root/'public'/d['url'].lstrip('/'),'Folio-by-Hicham/documents/'+d['id']+'.pdf')
 archive.writestr('Folio-by-Hicham/index.html',index)
 archive.writestr('Folio-by-Hicham/catalogue.json',json.dumps(docs,ensure_ascii=False,indent=2))
for attempt in range(6):
 try:
  temp.replace(target)
  break
 except PermissionError:
  if attempt==5:raise
  time.sleep(1)
print('Archive refreshed:',len(docs),'PDFs')
