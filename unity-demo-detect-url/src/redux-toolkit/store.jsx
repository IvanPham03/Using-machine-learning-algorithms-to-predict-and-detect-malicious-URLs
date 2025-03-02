// src/app/store.js
import { configureStore } from '@reduxjs/toolkit';
import alertReducer from './slice/alertSlice'
import spinnerReducer from './slice/spinnerSlice'
import predictReducer from './slice/predictSlice'
export const store = configureStore({
    reducer: {
        alert: alertReducer,
        spinner: spinnerReducer,
        predict: predictReducer
    },
});

export default store;
