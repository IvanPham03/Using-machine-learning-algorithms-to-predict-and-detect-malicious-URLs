import React, { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import Image from '../../../assets/images/detectUrl/logo-google-safe.png';
import axiosInstance from '../../../api/axiosInstance.js';

const GoogleSafe = () => {
    const { input } = useSelector((state) => state.predict); // Ensure state structure is correct
    const [response, setResponse] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const res = await axiosInstance.post('/api/google-safe-browsing', { url: input });
                // console.log(res.data);

                setResponse(res.data);
            } catch (error) {
                console.error("An error occurred:", error);
            }
        };

        if (input) {
            fetchData();
        }
    }, [input]);

    return (
        <div className='flex lg:flex-row flex-col lg:gap-10 gap-5 items-center place-content-center justify-center border-customBlue border-2 rounded py-4 lg:mt-10 mt-5'>
            <div className='w-1/4 flex items-center justify-center'>
                <img src={Image} alt="img google safe browsing" className='h-20 object-contain' />
            </div>
            <div className='w-3/4 lg:text-left text-center text-balance'>
                <p className='lg:text-[26px] text-[20px]'>
                    <span className={`h-20 font-semibold ${response === true ? 'text-green-700' : 'text-red-700'}`}>Result: {response ? 'Safe' : 'Malicious'} </span>
                </p>
                <p className='pt-2 break-words'>
                    Safe Browsing is a Google service that lets client applications check URLs against Google's constantly updated lists of unsafe web resources
                </p>
            </div>
        </div>

    );
};

export default GoogleSafe;
