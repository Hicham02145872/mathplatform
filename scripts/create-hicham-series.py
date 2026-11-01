from pathlib import Path
import json,hashlib,runpy,sys
sys.stdout.reconfigure(encoding='utf-8')
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph,Table,TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from pypdf import PdfReader
import pypdfium2 as pdfium

ROOT=Path(__file__).resolve().parents[1]
ID='hicham-serie-logique-calcul-01'
OUT=ROOT/'public/documents'/f'{ID}.pdf'
pdfmetrics.registerFont(TTFont('Cambria','C:/Windows/Fonts/cambria.ttc',subfontIndex=0))
pdfmetrics.registerFont(TTFont('CambriaBold','C:/Windows/Fonts/cambriab.ttf'))
pdfmetrics.registerFontFamily('Cambria',normal='Cambria',bold='CambriaBold',italic='Cambria',boldItalic='CambriaBold')
required='ℝℕℤℚ∃∀⇒⇔¬∅√∧∨≥≤'
assert all(ord(ch) in pdfmetrics.getFont('Cambria').face.charWidths for ch in required),'Missing mathematical glyphs'
NAVY=HexColor('#172d49');BLUE=HexColor('#285cc9');GRAY=HexColor('#637085');LINE=HexColor('#e4e8ef')
style=ParagraphStyle('body',fontName='Cambria',fontSize=11,leading=16,textColor=NAVY,spaceAfter=0)
small=ParagraphStyle('small',parent=style,fontSize=9,leading=13,textColor=GRAY)
c=canvas.Canvas(str(OUT),pagesize=(595.276,841.89))
c.setTitle('Folio by Hicham — Série 01 : Logique et calcul numérique')
c.setAuthor('Folio by Hicham')
y=0;page=0
def para(text,gap=7,sty=style):
 global y
 p=Paragraph(text,sty);w,h=p.wrap(499,800)
 assert y-h>47,(page,text,y,h)
 p.drawOn(c,48,y-h);y-=h+gap
def heading(n,title):
 global y
 y-=8;c.setFillColor(BLUE);c.roundRect(48,y-19,24,21,5,fill=1,stroke=0)
 c.setFillColor(HexColor('#ffffff'));c.setFont('Helvetica-Bold',9);c.drawCentredString(60,y-12,str(n))
 c.setFillColor(NAVY);c.setFont('CambriaBold',14);c.drawString(82,y-13,title);y-=31
def new(title,section,subtitle):
 global y,page
 if page:c.showPage()
 page+=1
 c.drawImage(ImageReader(str(ROOT/'public/brand/hicham-monogram.png')),43,785,38,38,mask='auto')
 c.setFillColor(NAVY);c.setFont('Helvetica-Bold',17);c.drawString(87,805,'folio.')
 c.setFont('Helvetica',6)
 c.drawString(88,794,'B Y   H I C H A M')
 c.setFillColor(GRAY);c.setFont('Helvetica',8);c.drawRightString(547,807,'1 BAC · LETTRES & SCIENCES HUMAINES')
 c.setStrokeColor(LINE);c.line(48,775,547,775)
 c.setFillColor(BLUE);c.setFont('Helvetica-Bold',8);c.drawString(48,750,section)
 c.setFillColor(NAVY);c.setFont('CambriaBold',25);c.drawString(48,717,title)
 y=697;para(subtitle,15,small)
 c.setStrokeColor(LINE);c.line(48,39,547,39);c.setFillColor(GRAY);c.setFont('Helvetica',7)
 c.drawString(48,25,'FOLIO BY HICHAM  /  SÉRIE 01  /  LOGIQUE & CALCUL')
 c.drawRightString(547,25,f'{page} / 6')
def table(rows,widths):
 global y
 cells=[[Paragraph(str(x),style) for x in row] for row in rows]
 t=Table(cells,colWidths=widths)
 t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),HexColor('#eaf0fc')),('GRID',(0,0),(-1,-1),.5,LINE),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('LEFTPADDING',(0,0),(-1,-1),8),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
 w,h=t.wrap(499,800);assert y-h>47;t.drawOn(c,48,y-h);y-=h+10

new('Logique : lire et raisonner','EXERCICES  /  01–03','Travaillez sans consulter les corrigés. Pour chaque réponse, donnez une justification ou un contre-exemple.')
para('<b>Notations.</b> ℕ contient 0 ; ℤ désigne les entiers, ℚ les rationnels et ℝ les réels. Le symbole ∃! signifie « il existe un unique ».',9,small)
heading(1,'Quantificateurs')
para('Résoudre x + 1 ≥ 0 dans ℝ, puis déterminer la valeur de vérité de chaque proposition.')
table([['Domaine','Pour tout x : x + 1 ≥ 0','Il existe x : x + 1 ≥ 0','Il existe un unique x : x + 1 ≥ 0'],['ℝ','A','B','C'],['ℤ','D','E','F'],['ℕ','G','—','—'],['ℚ','H','I','—']],[65,145,145,144])
heading(2,'Implications : vrai ou faux ?')
for s in ['a. (3 &lt; 0) ⇒ « 4 est un nombre impair ».','b. (−4 = 1) ⇒ ((−4)² = 1²).','c. (π &gt; 3) ⇒ ((1 − √2)² = 1 − √2).','d. ∀x ∈ ℝ, (x² = 4) ⇒ (x = 2).','e. (π &gt; 3) ⇒ (π² = 10).','f. ∀x ∈ ℝ, (x = 1) ⇒ (x² = 1).','g. ∀x ∈ ℝ, (|x| ≤ 1) ⇒ (−1 ≤ x ≤ 1).','h. Si ABCD est un parallélogramme, alors les vecteurs AB et DC sont égaux.']:para(s,3)
heading(3,'Propositions composées')
for s in ['a. « 0 divise 3 » ⇒ « 0 est pair ».','b. (6 = 2 × 3) ⇒ « 3 est un nombre premier ».','c. (4 × 3 = 20) ⇔ « 5 est pair ».','d. « 24,15 est un nombre décimal » ⇔ « 25 est un multiple de 5 ».']:para(s,3)

new('Logique : nier et démontrer','EXERCICES  /  04–05','Écrire une négation sans conserver un symbole ¬ devant la proposition entière.')
heading(4,'Négations')
for s in ['a. √(15/4) = √15 / √4.','b. 22/7 est un nombre décimal.','c. √2 &lt; 1.','d. (2 ∉ ℕ) ∧ (√5 &lt; 3).','e. Pour un réel x fixé : (|x| = x) ∨ (|x| = −x).','f. Pour un réel x fixé : (x = 2) ⇒ (x² = 4).','g. ∀x ∈ ]0 ; +∞[, x + 1/x ≥ 2.']:para(s,9)
para('Pour g, exprimer la négation en utilisant un réel strictement positif. Déterminer ensuite la valeur de vérité de la proposition initiale.')
heading(5,'Lois logiques')
para('Construire une table de vérité pour démontrer que les deux propositions suivantes sont des tautologies :')
para('a. (P ⇒ Q) ⇔ (¬P ∨ Q).',12)
para('b. (P ⇔ Q) ⇔ [(P ⇒ Q) ∧ (Q ⇒ P)].',12)
para('<b>Méthode.</b> Utiliser les quatre couples (P,Q) : (V,V), (V,F), (F,V), (F,F). Une tautologie est vraie pour chacun de ces couples.',15,small)
heading('→','Espace de travail')
for k in range(7):
 c.setStrokeColor(LINE);c.line(48,y-5,547,y-5);y-=23

new('Calcul numérique','EXERCICES  /  06–08','Préciser les conditions de définition et conserver les valeurs exactes.')
heading(6,'Équations : deux ensembles de solutions')
para('Résoudre chacune des équations dans ℝ, puis dans ℕ :')
for s in ['a. 2x − 3 = 0.','b. (x − 3)(2x + 1) = 0.','c. (2x + 1)/(x − 1) = 1.','d. x − 1 = x + 1.','e. x − 2 = x − 2.']:para(s,12)
heading(7,'Inéquations')
para('Résoudre dans ℝ et présenter le résultat sous forme d’intervalle.')
para('a. 4x + 1 ≤ x − 2.',15)
para('b. −3x + 1 &gt; x + 5.',15)
heading(8,'Signe de ax + b')
para('Soient a et b deux réels. Si a ≠ 0, déterminer le zéro de ax + b et construire son tableau de signes. Distinguer a &gt; 0 et a &lt; 0, puis expliquer le cas a = 0.')
para('<b>Vérification.</b> Appliquer le résultat à 3x + 3, puis à −4x − 4.',18)
para('<b>Note éditoriale.</b> Série structurée à partir des photos du cahier fournies par l’utilisateur. Notations harmonisées, calculs revérifiés et doublon photographique retiré. Un second énoncé quantifié de l’application 7, ambigu sur la photo, n’est pas reproduit. Le cas a = 0 et les deux applications de signe complètent la consigne générale du cahier.',0,small)

new('Corrigé : valeurs de vérité','CORRIGÉS  /  01–03','Comparer le raisonnement, et pas uniquement la réponse finale.')
heading(1,'Quantificateurs')
para('x + 1 ≥ 0 ⇔ x ≥ −1. Dans ℝ, l’ensemble des solutions est [−1 ; +∞[.')
table([['Domaine','Universelle','Existence','Unicité'],['ℝ','A : faux','B : vrai','C : faux'],['ℤ','D : faux','E : vrai','F : faux'],['ℕ','G : vrai','—','—'],['ℚ','H : faux','I : vrai','—']],[80,139,140,140])
para('Contre-exemple aux propositions A, D et H : x = −2. Pour B, E et I, choisir x = 0. Les valeurs x = 0 et x = 1 réfutent l’unicité C et F. Enfin, tout entier naturel x vérifie x ≥ 0, donc x + 1 ≥ 1 : G est vraie.')
heading(2,'Implications')
for s in ['a. <b>Vrai.</b> L’antécédent 3 &lt; 0 est faux.','b. <b>Vrai.</b> L’antécédent −4 = 1 est faux.','c. <b>Faux.</b> π &gt; 3, mais (1 − √2)² = 3 − 2√2 ≠ 1 − √2.','d. <b>Faux.</b> x = −2 vérifie x² = 4 sans vérifier x = 2.','e. <b>Faux.</b> π &gt; 3 et π² ≠ 10. En effet, 3 &lt; π &lt; 22/7 et (22/7)² = 484/49 &lt; 10.','f. <b>Vrai.</b> Le carré de 1 est 1.','g. <b>Vrai.</b> Par définition de la valeur absolue, |x| ≤ 1 ⇔ −1 ≤ x ≤ 1.','h. <b>Vrai.</b> Les côtés opposés AB et DC ont même direction, même sens et même longueur.']:para(s,7)
heading(3,'Propositions composées')
para('a. <b>Vrai</b> : 0 ne divise pas 3 ; l’antécédent est faux. b. <b>Vrai</b> : les deux affirmations sont vraies. c. <b>Vrai</b> : les deux affirmations sont fausses ; leur équivalence est vraie. d. <b>Vrai</b> : 24,15 est décimal et 25 = 5 × 5.')

new('Corrigé : négations et lois','CORRIGÉS  /  04–05','Les quantificateurs et les connecteurs changent lorsqu’on nie une proposition.')
heading(4,'Négations')
for s in ['a. √(15/4) ≠ √15 / √4.','b. 22/7 n’est pas un nombre décimal.','c. √2 ≥ 1.','d. (2 ∈ ℕ) ∨ (√5 ≥ 3).','e. (|x| ≠ x) ∧ (|x| ≠ −x).','f. (x = 2) ∧ (x² ≠ 4).','g. ∃x ∈ ]0 ; +∞[, x + 1/x &lt; 2.']:para(s,7)
para('La proposition g initiale est vraie : pour x &gt; 0, (x − 1)² ≥ 0 ; en divisant par x, on obtient x − 2 + 1/x ≥ 0, donc x + 1/x ≥ 2.')
heading(5,'Tables de vérité')
table([['P','Q','P ⇒ Q','¬P ∨ Q','Équivalence'],['V','V','V','V','V'],['V','F','F','F','V'],['F','V','V','V','V'],['F','F','V','V','V']],[55,55,125,125,139])
table([['P','Q','P ⇔ Q','(P ⇒ Q) ∧ (Q ⇒ P)','Équivalence'],['V','V','V','V','V'],['V','F','F','F','V'],['F','V','F','F','V'],['F','F','V','V','V']],[55,55,95,155,139])
para('Dans les deux tables, la dernière colonne est toujours V : ce sont bien deux lois logiques.')

new('Corrigé : calcul numérique','CORRIGÉS  /  06–08','Les solutions dans ℕ s’obtiennent en ne gardant que les solutions réelles qui sont naturelles.')
heading(6,'Équations')
for s in ['a. 2x − 3 = 0 ⇔ x = 3/2. Donc Sℝ = {3/2} et Sℕ = ∅.','b. Un produit est nul si au moins un facteur est nul. Ainsi x = 3 ou x = −1/2. Donc Sℝ = {−1/2 ; 3} et Sℕ = {3}.','c. Condition : x ≠ 1. Alors 2x + 1 = x − 1 ⇔ x = −2, valeur autorisée. Donc Sℝ = {−2} et Sℕ = ∅.','d. En retranchant x : −1 = 1, ce qui est impossible. Donc Sℝ = Sℕ = ∅.','e. L’égalité est vraie pour tout réel. Donc Sℝ = ℝ et Sℕ = ℕ.']:para(s,9)
heading(7,'Inéquations')
para('a. 4x + 1 ≤ x − 2 ⇔ 3x ≤ −3 ⇔ x ≤ −1. Ainsi S = ]−∞ ; −1].',10)
para('b. −3x + 1 &gt; x + 5 ⇔ −4x &gt; 4 ⇔ x &lt; −1. La division par −4 inverse le sens de l’inégalité. Ainsi S = ]−∞ ; −1[.',10)
heading(8,'Signe d’une expression affine')
para('Si a ≠ 0, poser r = −b/a. Alors ax + b = a(x − r).')
table([['Valeurs de x',']−∞ ; r[','r',']r ; +∞['],['a &gt; 0 : signe de ax + b','−','0','+'],['a &lt; 0 : signe de ax + b','+','0','−']],[235,88,88,88])
para('Si a = 0, l’expression est constante, égale à b : positive si b &gt; 0, nulle si b = 0 et négative si b &lt; 0.')
para('Pour 3x + 3 : zéro −1, signe − avant −1 et + après. Pour −4x − 4 : zéro −1, signe + avant −1 et − après.')
c.save()
reader=PdfReader(OUT);assert len(reader.pages)==6
doc=pdfium.PdfDocument(OUT)
dest=ROOT/'public/pages'/ID;dest.mkdir(parents=True,exist_ok=True)
qa=ROOT/'verification/serie-hicham';qa.mkdir(parents=True,exist_ok=True)
for n in range(len(doc)):
 im=doc[n].render(scale=1.5).to_pil()
 im.save(dest/f'{n+1}.webp','WEBP',quality=88)
 im.save(qa/f'page-{n+1}.png')
 if n==0:
  im.thumbnail((420,560));im.save(ROOT/'public/covers'/f'{ID}.webp','WEBP',quality=85)
doc.close()
item=dict(id=ID,title='Logique & calcul numérique — Série Hicham',originalTitle='Série 01 — exercices et corrigés à partir du cahier',subtitle='Exercices et corrigés · 8 exercices',kind='exercices',chapters=['logique','calcul'],chapter='logique',chapterTitle='Logique & calcul numérique',symbol='P ∧ Q',term=1,correction=False,language='fr',pages=6,size=OUT.stat().st_size,url=f'/documents/{ID}.pdf',cover=f'/covers/{ID}.webp',source=f'/documents/{ID}.pdf')
manifest=ROOT/'src/documents.json';items=json.loads(manifest.read_text(encoding='utf-8'));items=[i for i in items if i['id']!=ID];items.insert(0,item);manifest.write_text(json.dumps(items,ensure_ascii=False,indent=2),encoding='utf-8')
custom=ROOT/'src/custom-documents.json';custom.write_text(json.dumps([item],ensure_ascii=False,indent=2),encoding='utf-8')
runpy.run_path(str(ROOT/'scripts/index-text.py'))['index_documents'](ROOT)
print('Created',OUT,'with',len(reader.pages),'pages')
