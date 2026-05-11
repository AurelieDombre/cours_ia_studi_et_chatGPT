import { combineReducers } from "redux"
import { counterReducer } from "./counterReducer"
import { colorReducer } from "./colorReducer"

export const rootReducer = combineReducers({
    counter : counterReducer,
    color : colorReducer
})