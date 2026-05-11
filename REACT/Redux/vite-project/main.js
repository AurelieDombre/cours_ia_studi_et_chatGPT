import { store } from './store/store.js'
import './actions/index.js'

// Récupérer le conteneur du compteur
const counterContainer = document.getElementById('counter')
const body = document.querySelector('body')
const randNumberContainer = document.getElementById('randNumber')

// Affichage initial du compteur
const render = () => {
    // Récupérer la valeur du compteur depuis le state
    const { counter, color, randNumber } = store.getState()

    // Afficher la valeur du compteur dans le conteneur
    counterContainer.innerHTML = counter.counter

    body.style.backgroundColor = color.color
    
    randNumberContainer.innerHTML = ` Nombre aléatoire : ${randNumber.randNumber}`
}

render()

// S'abonner aux changements de state
store.subscribe(render)