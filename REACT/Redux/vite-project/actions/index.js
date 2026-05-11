import { store } from '../store/store.js'

// Ajouter des écouteurs d'événements
document.querySelector('#increment').addEventListener('click', () => {
    // Dispatch d'une action pour incrémenter le compteur
    store.dispatch({ type: 'COUNTER_INCREMENTED' })
})

document.querySelector('#decrement').addEventListener('click', () => {
    store.dispatch({ type: 'COUNTER_DECREMENTED' })
})

//Lors du clic sur le bouton qui possède l’id “randColor”, nous utilisons la méthode “dispatch” de notre store afin de transmettre une action contenant le type “COLOR_CHANGED”.
document.querySelector('#randColor').addEventListener('click', () => {
    store.dispatch({ type: 'COLOR_CHANGED' })
})