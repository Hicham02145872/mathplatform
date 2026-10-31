import React from 'react';
import {createRoot} from 'react-dom/client';
import App from './App.jsx';
import './styles.css';
import './polish.css';
class ErrorBoundary extends React.Component {state={error:false};static getDerivedStateFromError(){return{error:true}}render(){return this.state.error?<main className="fatal"><h1>Folio n’a pas pu s’ouvrir.</h1><p>Rechargez la page pour retrouver vos documents.</p><button className="button primary" onClick={()=>location.reload()}>Recharger</button></main>:this.props.children}}
createRoot(document.getElementById('root')).render(<React.StrictMode><ErrorBoundary><App/></ErrorBoundary></React.StrictMode>);
