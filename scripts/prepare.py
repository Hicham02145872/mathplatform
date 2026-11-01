from pathlib import Path
import json,re,shutil
import pypdfium2 as pdfium

root=Path(__file__).resolve().parents[1]
source=root.parent/'maths-1bac-lettres'
items=json.loads((source/'manifest.json').read_text(encoding='utf-8'))
chapters=[('المنطق','logique','Notions de logique','P ∧ Q'),('الحساب العددي','calcul','Calcul numérique','a² + b²'),('الدوال العددية','fonctions','Fonctions numériques','f(x)'),('المتتاليات','suites','Suites numériques','uₙ'),('التعداد','denombrement','Dénombrement','Cⁿₚ'),('نهاية','limites','Limites de fonctions','lim'),('الاشتقاق','derivation','Dérivation',"f′(x)"),('دراسة','etude','Étude de fonctions','↗')]
region=[('الرباط سلا زمور زعير','Rabat–Salé–Zemmour–Zaër'),('الرباط سلا القنيطرة','Rabat–Salé–Kénitra'),('الشاوية ورديغة','Chaouia–Ouardigha'),('فاس مكناس','Fès–Meknès'),('طنجة تطوان الحسيمة','Tanger–Tétouan–Al Hoceïma'),('كلميم واد نون','Guelmim–Oued Noun'),('العيون الساقية الحمراء','Laâyoune–Sakia El Hamra')]
results=[]
for i in items:
 if i['statut']!='Téléchargé':continue
 title=i['titre'];path=source/i['fichier'];ident=path.stem
 chapter=next(((key,fr,symbol) for ar,key,fr,symbol in chapters if ar in title),('general','Programme & synthèses','Σ'))
 if i['langue']=='français':chapter=('logique','Notions de logique','P ∧ Q') if 'Logique' in title else ('calcul','Calcul numérique','a² + b²')
 kind='cours';subtitle='Cours complet';term=1
 if chapter[0] in ['denombrement','limites','derivation','etude']:term=2
 if 'ملخص' in title:subtitle='Fiche de synthèse'
 if 'تمارين' in title:kind='exercices';subtitle='Exercices corrigés' if 'محلولة' in title and 'غير' not in title else 'Série d’exercices'
 correction='التصحيح' in title
 if i['dossier']=='03-Controles':
  kind='controles';term=2 if 'الثانية' in title else 1
  ns=re.search('الفرض (\d+) نموذج (\d+)',title);a,b=ns.groups() if ns else ('1','1')
  chapter=('logique','Logique & calcul numérique','P ∧ Q') if term==1 and a=='1' else ('general','Mathématiques','Σ')
  display=f'Contrôle {a} · Modèle {b}';subtitle='Corrigé' if correction else 'Sujet';display+=f' — Semestre {term}'
 elif i['dossier']=='04-Examens-regionaux':
  kind='examens';term=0;chapter=('regional','Examen régional','∫')
  area=next((fr for ar,fr in region if ar in title),'Examen régional');year=re.search(r'20\d\d',title)
  display=area+' · '+(year.group() if year else '')
  subtitle=('Corrigé' if correction else 'Sujet')+(' · Rattrapage' if 'الإستدراكية' in title else ' · Session normale')
 else:
  display=chapter[1]
  if chapter[0]=='general':display='Programme pédagogique' if 'البرنامج' in title else 'Synthèse de mathématiques'
  number=re.search(r'(\d+)\s*$',title)
  if number:subtitle+=' · '+number.group()
 dest=root/'public'/'documents'/f'{ident}.pdf';shutil.copyfile(path,dest)
 cover=root/'public'/'covers'/f'{ident}.webp'
 if not cover.exists():
  doc=pdfium.PdfDocument(path);image=doc[0].render(scale=.65).to_pil();image.thumbnail((420,560));image.save(cover,'WEBP',quality=78)
 results.append(dict(id=ident,title=display,originalTitle=title,subtitle=subtitle,kind=kind,chapter=chapter[0],chapterTitle=chapter[1],symbol=chapter[2],term=term,correction=correction,language='fr' if i['langue']=='français' else 'ar',pages=i['pages'],size=i['octets'],url=f'/documents/{ident}.pdf',cover=f'/covers/{ident}.webp',source=i['page']))
custom=root/'src/custom-documents.json'
if custom.exists():
 results=json.loads(custom.read_text(encoding='utf-8'))+results
(root/'src'/'documents.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
shutil.copyfile(root.parent/'Maths-1bac-Lettres-PDF.zip',root/'public'/'Maths-1bac-Lettres-PDF.zip')
print('Prepared',len(results),'documents and thumbnails.')

# Page-level text extraction; scanned/image-only pages need a separate OCR pass.
import runpy
runpy.run_path(str(root/"scripts/index-text.py"))["index_documents"](root)
