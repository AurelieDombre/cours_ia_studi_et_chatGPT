import { createStore } from 'redux'
import { counterReducer } from '../reducers/counterReducer.js'
import { rootReducer } from '../reducers/rootReducer.js'

export const store = createStore(
    rootReducer,
    window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__()
)




