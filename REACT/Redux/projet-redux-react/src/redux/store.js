import { configureStore } from "@reduxjs/toolkit";
import counterReducer from "../redux/counterSlice.js";
import colorReducer from "../redux/colorSlice.js";

const store = configureStore({
  reducer: {
    counter: counterReducer,
    color: colorReducer,
  },
});

export default store;
