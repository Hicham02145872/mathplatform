# Vérification — 31 octobre 2026

Compilation Vite de production réussie. Application livrée avec React et React DOM comme seules dépendances d'interface.

## Fichiers

- 120 identifiants uniques ; 120 PDF dont la signature PDF a été vérifiée.
- 120 couvertures et 278 pages WebP présentes, non vides et rattachées au catalogue.
- Réponses HTTP 200 pour l'application, un PDF, sa couverture, sa page et l'archive complète.

## Parcours vérifiés dans le navigateur

- Recherche « calcul » : 19 résultats ; recherche arabe « المنطق » : 7 résultats.
- Filtre français : 2 documents ; filtre examens régionaux : 28 documents.
- État sans résultat et retour à la bibliothèque.
- Favori conservé après rechargement puis supprimé avec l'interface.
- Vue grille : 10 documents par page ; deuxième page : documents 11 à 20 sur 28.
- Lecteur : image chargée, passage de la page 1 à la page 2, zoom à 120 %, retour et reprise de la page 2 sur mobile.
- Notes conservées après fermeture du lecteur ; texte de test ensuite retiré.
- Navigation mobile : dialogue, sélection de chapitre puis ouverture directe d'un document.
- Thèmes clair et sombre observés.
- Formats ordinateur 1440 × 1000 et téléphone 390 × 844 ; absence de débordement horizontal de la bibliothèque dans les deux formats.
- Aucune image cassée dans la vue grille vérifiée.

Contrastes calculés : texte #242629 sur blanc 15,17:1 ; secondaire #6a6d75 sur blanc 5,18:1 ; accent #245ac9 sur blanc 6,21:1 ; texte sombre #eeeef2 sur #1d1e21 14,40:1 ; secondaire sombre #a6a8b2 sur #1d1e21 7,04:1.

## Limites

Vérification visuelle par échantillons, pas de relecture pédagogique des 278 pages. Les PDF sont des sources originales ; les pages du lecteur sont leurs rendus. Application personnelle et statique : ni authentification, ni rôles d'entreprise, ni synchronisation. Le traitement des limites du stockage local est tolérant aux erreurs ; les données personnelles restent dans le navigateur.

L'outil de publication Sites n'était pas disponible dans cette session. La version compilée dans dist est prête à être hébergée sur un serveur statique.


## Itération UI et identité

Nouveau logo transparent H / livre et signature Folio by Hicham intégrés au menu, à l'en-tête mobile et au favicon. Vérification du canal alpha du PNG et chargement constaté dans le navigateur.

Nouvelles vérifications : filtres mobiles ouverts/fermés, filtre français (2 résultats), navigation basse vers les chapitres puis accès au calcul numérique, ouverture du lecteur et chargement de sa page. Format ordinateur 1440 px sans débordement ni image cassée. Les deux thèmes utilisent des tokens dédiés.

Contrôle complémentaire à 320 × 780 : pas de débordement horizontal, recherche accessible depuis l’en-tête et focus reçu par le champ, recherche arabe conservée (7 résultats), navigation basse visible et mode sombre observé.


## Outils de révision — 1 novembre 2026

Compilation réussie. Index de 278 pages généré depuis les PDF avec PDFium. Vérification de 7 pages pertinentes pour « dérivée » via la correspondance bilingue et des 14 paires sujet/correction. Dans le navigateur : recherche « dérivée » (8 documents dont 4 présentent les pages textuelles correspondantes), ouverture directe de la synthèse à la page 15 ; tirage d'un examen, timer conservé après rechargement, correction présente, score 12/20 enregistré puis résultat de test supprimé. Les huit chapitres du planificateur et les 84 cellules accessibles de la heatmap sont présents. Calque canvas testé par un glisser de pointeur : trait enregistré et annulation activée, puis trait de test annulé.

Limites : aucune OCR, extraction limitée au texte encodé des PDF ; résultats d'examen autoévalués ; SRS à intervalle initial de trois jours puis doublement, sans notification système. Données locales. L'index de texte augmente le JavaScript compilé à environ 970 Ko (249 Ko gzip), avec avertissement de taille Vite.


## Série personnalisée — 1 novembre 2026

PDF de six pages créé avec ReportLab, polices mathématiques embarquées et logo transparent. Les six pages rendues ont été inspectées, dont les pages 1 et 4 après les corrections finales. Huit exercices et corrigés ; doublon photographique retiré et une consigne ambiguë exclue avec note éditoriale. Racine −1/2, conditions x≠1, intervalles et tables de vérité revérifiés. Catalogue : 121 documents, 284 pages. Archive ZIP : 121 PDF, contenu du nouveau fichier vérifié identique à l’original. Recherche « Série Hicham » : un résultat ; ouverture et image chargée en page 1 constatées dans le navigateur.
