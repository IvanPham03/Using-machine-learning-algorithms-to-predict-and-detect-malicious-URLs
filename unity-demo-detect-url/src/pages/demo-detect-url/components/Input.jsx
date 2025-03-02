import React, { useState } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUserSecret } from '@fortawesome/free-solid-svg-icons';
import axiosInstance from '../../../api/axiosInstance.js'
import { useDispatch } from 'react-redux';
import { addAlert, } from '../../../redux-toolkit/slice/alertSlice.jsx'
import { addSpinner, removeSpinner } from '../../../redux-toolkit/slice/spinnerSlice.jsx'
import { addResponsePredict, addInputPredict } from '../../../redux-toolkit/slice/predictSlice.jsx'
const Input = () => {
    const [input, setInput] = useState('')
    const dispatch = useDispatch()
    const isValidURL = (url) => {
        try {
            new URL(url); // Tạo một đối tượng URL, nếu lỗi xảy ra nghĩa là URL không hợp lệ
            return true;
        } catch {
            return false;
        }
    };

    const postData = async (data) => {
        // Kiểm tra giá trị đầu vào
        if (!isValidURL(data)) {
            dispatch(addAlert({ text: 'Invalid URL format.' }))
            return;
        }
        dispatch(addInputPredict({ input: data }))
        dispatch(addSpinner())
        try {
            const response = await axiosInstance.post('api/predict', { url: data });
            // Dispatch action với payload là response.data
            dispatch(addResponsePredict({ response: response.data }));
            setInput('')
            dispatch(removeSpinner())

            // console.log('Response:', response.data);
        } catch (error) {
            dispatch(removeSpinner())
            dispatch(addAlert({ text: 'The operation failed. Please ensure your input is correct and try again.' }))
            // console.error('Error:', error.response ? error.response.data : error.message);
        }
    };
    return (
        <>
            <div className='w-full my-10'>
                <div className='flex lg:flex-row flex-col items-center gap-10'>
                    <FontAwesomeIcon icon={faUserSecret} className='h-20 ' />
                    <p className='lg:text-[30px] text-[25px]'>Detect Malicious URLs Using Machine Learning and Deep Learning Algorithms</p>
                </div>
                <form
                    onSubmit={(e) => {
                        e.preventDefault();
                        postData(input)
                    }
                    }
                    action="" method="post" className='flex flex-col justify-between items-center my-10 gap-10'>
                    <input onChange={(e) => setInput(e.target.value)} type="text" value={input} placeholder='Search or scan a URL' className='break-words shadow-lg border-2 lg:w-full my-10 p-2 rounded-md border-customBlue focus:scale-110 transition ease-linear' />
                    <button
                        type="submit"
                        className="shadow-md hover:text-customBlue hover:border-customBlue text-sm sm:text-lg md:text-lg border-2 w-fit px-8 sm:px-16 py-2 rounded-md hover:opacity-90 hover:scale-95 transition ease-linear"
                    >
                        Send
                    </button>
                </form>
                <p>
                    By submitting data above, you are agreeing to our Terms of Service and Privacy Notice, and to the sharing of your URL submission with the security community. Please do not submit any personal information; we are not responsible for the contents of your submission.
                </p>
            </div>
        </>
    )
}

export default Input
