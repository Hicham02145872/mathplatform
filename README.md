# Mathplatform — Folio by Hicham

Bibliothèque React de mathématiques pour la première bac Lettres et Sciences humaines au Maroc. 121 PDF, 284 pages consultables et leurs sources.

## Lancer

Sur cet ordinateur, ouvrir **Lancer Folio.cmd**. Le lanceur utilise la version construite dans `dist` et ouvre le navigateur sur une adresse locale.

Sur un autre ordinateur avec Node.js compatible Vite 8 :

```sh
npm install
npm run dev
```

```sh
npm run build
npm run preview
```

Le dossier `dist` peut être hébergé sur un serveur statique. Tous les fichiers nécessaires sont inclus ; aucun CDN, API ou compte externe n'est nécessaire au fonctionnement.

## Utilisation

- Recherche immédiate en français et en arabe, sans tenir compte des accents et des signes vocaliques arabes. Raccourci Ctrl/Cmd K.
- Filtres par chapitre, type, langue et semestre ; tri, pagination et vues liste/grille.
- Aperçu réel de chaque PDF. Sur écran compact, toucher un document ouvre directement le lecteur.
- Lecteur de pages avec zoom, navigation aux flèches du clavier et reprise à la dernière page choisie.
- Favoris, liste des documents terminés, historique et notes conservés dans le navigateur.
- Notes exportables en texte. Téléchargement des PDF et de l'archive complète.
- Thèmes clair et sombre, focus clavier, dialogues natifs, mouvements et transparence réduits.

## Architecture

React et React DOM sont les seules dépendances applicatives. Vite assure le développement et la compilation ; CSS natif pour le style, SVG intégrés pour les icônes.

- `src/App.jsx` : catalogue, filtres, bibliothèque personnelle et aperçu.
- `src/components/Reader.jsx` : lecteur et notes.
- `src/components/Icons.jsx` : icônes et boutons associés.
- `src/lib/` : métadonnées de navigation, normalisation et stockage local.
- `src/documents.json` : catalogue avec langue, pagination, type et provenance.
- `public/documents/` : PDF originaux.
- `public/pages/` : pages WebP rendues depuis les PDF pour le lecteur.
- `public/covers/` : premières pages du catalogue.

`scripts/prepare.py` prépare le catalogue depuis le dossier de documents voisin. `scripts/render-pages.py` prépare les aperçus avec pypdfium2. Le résultat est déjà inclus : Python n'est pas nécessaire pour utiliser l'application.

## Données et limites

Cette version est une application personnelle sans serveur. Les données de lecture restent dans le stockage local de ce navigateur ; elles ne sont pas partagées entre appareils. Elle ne fournit pas de gestion des utilisateurs, de contrôle d'accès par rôle ou de synchronisation d'entreprise.

Le lecteur affiche des pages rendues en images. Pour sélectionner le texte, rechercher à l'intérieur du PDF ou utiliser ses fonctions d'accessibilité, choisir **Ouvrir le PDF**. Les documents originaux proviennent d'AlloSchool et de Dyrassa ; leurs auteurs et droits restent ceux des sources indiquées dans les fiches.

La collection contient principalement des documents en arabe, deux cours en français et une sélection de 14 examens régionaux avec leurs corrigés. Elle n'est pas une archive exhaustive de toutes les années.

Les dépendances locales sont actuellement réutilisées depuis le projet voisin `cadence` via une jonction `node_modules`. Sur une autre machine, utiliser `npm install` pour créer une installation autonome.


## Outils de révision

La recherche utilise désormais le texte des 278 pages extrait par `scripts/index-text.py`, appelé également depuis `scripts/prepare.py`. L'ouverture d'un résultat mène au premier passage correspondant. Une correspondance bilingue relie « dérivée » à la racine arabe de l'اشتقاق. Les scans et polices sans texte correctement encodé nécessitent un traitement OCR distinct ; cet index ne prétend pas en effectuer.

L'espace de révision, sous le catalogue, propose un sujet régional aléatoire, un compteur de 90 minutes, sa correction et un score autoévalué sur 20. Résultats et durées sont conservés localement. Le compteur continue lors d'une fermeture puis réouverture de la page.

Les rappels par chapitre sont proposés selon les documents terminés ou annotés : J+3 puis doublement de l'intervalle après validation. Les rappels sont consultables dans l'application, sans notifications système.

Le lecteur propose un calque canvas de surlignage et dessin, stocké séparément pour chaque page avec annulation du dernier trait. Les notes textuelles restent disponibles.

La progression présente les pourcentages par chapitre et 84 jours d'activité. Le temps de lecture est mesuré lorsque la page est visible et active, puis enregistré à la fermeture du lecteur. Une fermeture forcée du navigateur peut perdre le temps de la session courante. Toutes ces données restent dans le navigateur, sans synchronisation distante.


## Série Folio by Hicham

La série 01 « Logique & calcul numérique » contient huit exercices et leurs corrigés, mis au propre à partir des photos du cahier fournies. Six pages A4, identité Folio by Hicham, texte sélectionnable, tables de vérité et tableau de signes. Une consigne quantifiée illisible est explicitement signalée et n’a pas été inventée. Les documents personnalisés sont conservés dans src/custom-documents.json et réintégrés par prepare.py. Les photos privées ne sont pas incorporées au dépôt.
