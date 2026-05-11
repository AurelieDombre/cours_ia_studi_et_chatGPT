const initialState = { randNumber : 0 }

export const randNumberReducer = (state = initialState, action)=>{
    switch(action.type){
        case 'RAND_NUMBER_CHANGED':
            //Ici nous retournons un nouvel objet qui contient toutes les propriétés de notre état actuel grâce à l’opérateur de décomposition “...” 
            // et nous modifions la propriété “randNumber” en lui assignant la valeur de “action.payload” qui correspond à notre nombre aléatoire.
            return {...state, randNumber : action.payload }
        default : return state
    }
}