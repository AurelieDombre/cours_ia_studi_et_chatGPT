const initialState = { color : 'rgb(29,29,29)' }
export const colorReducer = (state = initialState, action)=>{
    switch(action.type){
        case 'COLOR_CHANGED':
            //Ici nous retournons un nouvel objet qui contient toutes les propriétés de notre état actuel grâce à l’opérateur de décomposition “...” 
            // et nous modifions la propriété “color” en lui assignant la valeur de “action.payload” qui correspond à notre couleur aléatoire.
            return {...state, color : action.payload }
        default : return state
    }
}