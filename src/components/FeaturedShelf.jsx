import React from 'react';
import {Icon} from './Icons.jsx';

export default function FeaturedShelf({documents, recent, onOpen}) {
  const [logic, calculation, control] = documents;
  return <section className="featured-shelf" aria-labelledby="featured-heading">
    <button className="featured-course" onClick={() => onOpen(logic)}>
      <span className="featured-copy">
        <span className="featured-eyebrow"><span className="feature-line"/> LE PREMIER CHAPITRE</span>
        <strong id="featured-heading">Notions<br/>de logique.</strong>
        <span className="featured-description">Propositions, connecteurs et raisonnement.<br/>Les bases, en 5 pages.</span>
        <span className="featured-cta">{recent.includes(logic.id) ? 'Reprendre le cours' : 'Ouvrir le cours'}<Icon name="arrow" size={18}/></span>
        <span className="featured-footnote">COURS PDF <i/> FRANÇAIS <i/> SEMESTRE 1</span>
      </span>
      <span className="featured-art" aria-hidden="true">
        <span className="math-orbit orbit-one"/>
        <span className="math-orbit orbit-two"/>
        <span className="math-expression">P ⇒ Q</span>
        <span className="featured-paper paper-back"><img src={logic.cover} alt=""/></span>
        <span className="featured-paper paper-front"><img src={logic.cover} alt=""/></span>
        <span className="paper-label"><Icon name="book" size={13}/>5 pages · Cours</span>
      </span>
    </button>
    <div className="next-courses">
      <p className="next-heading">POUR CONTINUER <Icon name="arrow" size={14}/></p>
      {[calculation,control].map((doc,index) => <button className="next-course" key={doc.id} onClick={() => onOpen(doc)}>
        <span className={'next-symbol symbol-'+index}>{index === 0 ? 'x²' : '01'}<span>{index === 0 ? 'COURS' : 'CONTRÔLE'}</span></span>
        <span className="next-copy"><span className="next-kicker">{index === 0 ? 'CHAPITRE 02' : 'MISE EN PRATIQUE'}</span><strong>{index === 0 ? 'Calcul numérique' : 'Logique & calcul'}</strong><span>{doc.pages} {doc.pages===1?'page':'pages'} · {doc.language==='fr'?'Français':'Arabe'}</span></span>
        <span className="next-arrow"><Icon name="arrow" size={17}/></span>
      </button>)}
      <p className="shelf-note"><Icon name="file" size={13}/>Documents originaux, avec leurs sources.</p>
    </div>
  </section>;
}
