"""Extract page text without changing the original PDFs. No OCR is implied."""
from pathlib import Path
import json
import pypdfium2 as pdfium

def index_documents(root):
    root=Path(root)
    docs=json.loads((root/'src/documents.json').read_text(encoding='utf-8'))
    result={}
    for doc in docs:
        pdf=pdfium.PdfDocument(root/'public'/doc['url'].lstrip('/'))
        pages=[]
        for n in range(len(pdf)):
            page=pdf[n]
            textpage=page.get_textpage()
            text=textpage.get_text_range()
            pages.append({'page':n+1,'text':text,'searchable':bool(text.strip())})
            textpage.close();page.close()
        pdf.close()
        result[doc['id']]=pages
    (root/'src/page-index.json').write_text(json.dumps(result,ensure_ascii=False),encoding='utf-8')
    print('Indexed',sum(len(p) for p in result.values()),'pages')

if __name__=='__main__':index_documents(Path(__file__).resolve().parents[1])
