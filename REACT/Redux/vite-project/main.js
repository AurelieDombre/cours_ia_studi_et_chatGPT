import { store } from './store/store.js'
import './actions/index.js'

// Récupérer le conteneur du compteur
const counterContainer = document.getElementById('counter')
const body = document.querySelector('body')

// Affichage initial du compteur
const render = () => {
    // Récupérer la valeur du compteur depuis le state
    const { counter, color } = store.getState()

    // Afficher la valeur du compteur dans le conteneur
    counterContainer.innerHTML = counter.counter

    body.style.backgroundColor = color.color
}

render()

// S'abonner aux changements de state
store.subscribe(render)