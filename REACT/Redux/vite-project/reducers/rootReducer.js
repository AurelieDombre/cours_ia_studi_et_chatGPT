import { combineReducers } from "redux"
import { counterReducer } from "./counterReducer"
import { colorReducer } from "./colorReducer"
import { randNumberReducer } from "./randomReducer"


export const rootReducer = combineReducers({
    counter : counterReducer,
    color : colorReducer,
    randNumber : randNumberReducer,
})