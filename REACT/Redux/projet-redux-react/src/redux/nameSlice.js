import { createSlice } from '@reduxjs/toolkit';

export const nameSlice = createSlice({
  name: 'userName',
  initialState: {
    value: 'John Doe',
  },
  reducers: {
    setUserName: (state, action) => {
      console.log(state, action);
      state.value = action.payload;
    },
  },
});

//
export const { setUserName } = nameSlice.actions;
export default nameSlice.reducer;
