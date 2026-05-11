import { configureStore, combineReducers } from "@reduxjs/toolkit";

import counterReducer from "../redux/counterSlice.js";
import colorReducer from "../redux/colorSlice.js";
import storage from "redux-persist/es/storage"
import { persistStore, persistReducer } from "redux-persist";
import { nameSlice } from "./nameSlice.js";

// Tous les reducers
const rootReducer = combineReducers({
    counter: counterReducer,
    color: colorReducer,
    userName: nameSlice.reducer,

});

// Configuration persistence
const persistConfig = {
    key: "root",
    storage : storage,
    // blacklist : ['color'] //seul la couleur ne changera pas au rafraichissement de la page, le compteur lui se remettra à 0
    //blacklist : ['counter'],
    whitelist : ['counter'] //seule la couleur changera au rafraichissement de la page, le compteur lui reste au chiffre qu'il avait avant le rafraichissement de la page, la couleur elle se remettra à sa valeur initiale
};

// Reducer persisté
const persistedReducer = persistReducer(persistConfig, rootReducer);

// Store
export const store = configureStore({
    reducer: persistedReducer,
    
    middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
        serializableCheck: false,
    }),
});

// Persistor
export const persistor = persistStore(store);
