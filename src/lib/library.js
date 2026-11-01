export const chapters=[['logique','Notions de logique','01'],['calcul','Calcul numérique','02'],['fonctions','Fonctions numériques','03'],['suites','Suites numériques','04'],['denombrement','Dénombrement','05'],['limites','Limites de fonctions','06'],['derivation','Dérivation','07'],['etude','Étude de fonctions','08']];
export const kinds=[['all','Tout'],['cours','Cours'],['exercices','Exercices'],['controles','Contrôles'],['examens','Régionaux']];
export const normalize=s=>s.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f\u064B-\u065F\u0670]/g,'').replace(/[أإآ]/g,'ا').replace(/ى/g,'ي');
export const readableSize=n=>n<1000000?`${Math.round(n/1000)} Ko`:`${(n/1000000).toFixed(1)} Mo`;

export const matchesWord=(text,word)=>text.includes(word)||({derivee:"اشتق",derivees:"اشتق",derivation:"اشتق"}[word]&&text.includes("اشتق"));
