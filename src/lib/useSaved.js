import {useState,useEffect} from 'react';
export function useSaved(key,initial){const [state,setState]=useState(()=>{try{const v=JSON.parse(localStorage.getItem('folio:'+key));return v??initial}catch{return initial}});useEffect(()=>{try{localStorage.setItem('folio:'+key,JSON.stringify(state))}catch{}},[state,key]);return[state,setState]}
