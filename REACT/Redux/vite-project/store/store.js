import { createStore } from 'redux'
import { counterReducer } from '../reducers/counterReducer.js'

export const store = createStore(counterReducer)




