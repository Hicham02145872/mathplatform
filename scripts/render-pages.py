from pathlib import Path
import json
import pypdfium2 as pdfium
root=Path(__file__).resolve().parents[1]
items=json.loads((root/'src/documents.json').read_text(encoding='utf-8'))
count=0
for item in items:
 dest=root/'public/pages'/item['id'];dest.mkdir(parents=True,exist_ok=True)
 doc=pdfium.PdfDocument(root/'public'/item['url'].lstrip('/'))
 for n in range(len(doc)):
  path=dest/f'{n+1}.webp'
  if not path.exists():
   im=doc[n].render(scale=1.5).to_pil();im.save(path,'WEBP',quality=86)
  count+=1
 doc.close()
print('Rendered',count,'pages.')
