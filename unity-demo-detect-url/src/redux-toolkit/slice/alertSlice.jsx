import { createSlice } from '@reduxjs/toolkit';
import Image from '../../assets/images/logo.png'

export const alertSlice = createSlice({
    name: "alertSlice",
    initialState:{
        image: Image,
        text:"",
        active: false,
    },
    reducers:{
        addAlert: (state, action) => {
            state.image = action.payload.image || Image
            state.text = action.payload.text || ""
            state.active = true
            console.log("Alert added:", state.text);
        },
        removeAlert: (state) => {
            state.image = ""
            state.text = ""
            state.active = false
        }
    }

})

export const { addAlert, removeAlert } = alertSlice.actions 
export default alertSlice.reducer;
