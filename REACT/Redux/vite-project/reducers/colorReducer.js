const initialState = { color : 'rgb(29,29,29)' }
export const colorReducer = (state = initialState, action)=>{
    switch(action.type){
        case 'COLOR_CHANGED':
            let randomColor = `rgb(${Math.random()* 255},${Math.random()* 255},${Math.random()* 255})`
            return {...state, color : randomColor }
        default : return state
    }
}