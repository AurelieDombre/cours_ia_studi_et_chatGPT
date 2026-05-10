import { store } from '../store/store.js'

// Ajouter des écouteurs d'événements
document.querySelector('#increment').addEventListener('click', () => {
    // Dispatch d'une action pour incrémenter le compteur
    store.dispatch({ type: 'COUNTER_INCREMENTED' })
})

document.querySelector('#decrement').addEventListener('click', () => {
    store.dispatch({ type: 'COUNTER_DECREMENTED' })
})