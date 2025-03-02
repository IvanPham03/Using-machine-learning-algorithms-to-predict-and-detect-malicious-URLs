import { createSlice } from '@reduxjs/toolkit';

export const spinnerSlice = createSlice({
    name: "spinnerSlice",
    initialState: {
        active: false,
    },
    reducers: {
        addSpinner: (state) => {
            state.active = true
        },
        removeSpinner: (state) => {
            state.active = false
        }
    }
})

export const { addSpinner, removeSpinner } = spinnerSlice.actions
export default spinnerSlice.reducer;
