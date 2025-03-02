import { createSlice } from '@reduxjs/toolkit';


export const predictSlice = createSlice({
    name: "predict",
    initialState: {
        input: '',
        response: '',
    },
    reducers: {
        addInputPredict: (state, action) => {
            state.input = action.payload.input
            state.response = ''
        
        },
        addResponsePredict: (state, action) => {
            state.response = action.payload.response
        },

        clearPredict: (state) => {
            state.input = ''
            state.response = ''
            state.domain = ''
        }
    }
})

export const { addInputPredict, addResponsePredict, clearPredict } = predictSlice.actions
export default predictSlice.reducer;
