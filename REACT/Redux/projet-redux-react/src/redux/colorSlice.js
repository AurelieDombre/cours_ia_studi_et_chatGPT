import { createSlice } from "@reduxjs/toolkit";

export const colorSlice = createSlice({
    name : "color",
    initialState : {
        value : "rgb(29, 29, 29)"
    },
    reducers : {
        randomColor : (state) => {
            const r = Math.floor(Math.random() * 255)
            const g = Math.floor(Math.random() * 255)
            const b = Math.floor(Math.random() * 255)
            let randomColor = `rgb(${r}, ${g}, ${b})`
            // ou bien :
            /* let randomColor = `rgb(${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)}, ${Math.floor(Math.random() * 255)})`  */
            state.value = randomColor
        }
    }
})

//
export const { randomColor } = colorSlice.actions
export default colorSlice.reducer