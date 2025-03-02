import React, { useEffect, useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faShieldVirus } from '@fortawesome/free-solid-svg-icons';
import { useSelector } from 'react-redux';
import GoogleSafe from './GoogleSafe'
import VideoDemo from '../../../assets/images/detectUrl/demo.mp4'
const Predict = () => {
    const { response, input } = useSelector((state) => state.predict); // Ensure state structure is correct
    const [domain, setDomain] = useState('');
    const label_mapping = {
        "Benign": "Safe: The URL is safe. No threats detected.",
        "defacement": "Defacement: The URL shows signs of defacement. Proceed with caution.",
        "malware": "Malware: The URL is flagged for malware. Avoid it.",
        "phishing": "Phishing: The URL is suspected of phishing.Do not visit."
    }

    // Hàm tách domain từ URL
    const getDomainFromURL = (url) => {
        try {
            const urlObject = new URL(url);
            return urlObject.hostname; // Trả về hostname (domain)
        } catch (error) {
            return ''; // Nếu URL không hợp lệ, trả về chuỗi rỗng
        }
    };
    useEffect(() => {
        if (input) {
            const domain = getDomainFromURL(input); // Lấy domain từ URL input
            setDomain(domain); // Cập nhật state domain
        }
    }, [input]); // Chạy khi input thay đổi
    // console.log(response?.response_DOM);
    // console.log("input:", input);
    // console.log("domain:", domain);

    return (
        response ?
            (
                <div>
                    <div className='flex lg:flex-row flex-col lg:gap-10 gap-5 items-center place-content-center justify-center border-customBlue border-2 rounded py-4'>
                        <div className='w-1/4 flex items-center justify-center'>
                            <FontAwesomeIcon
                                icon={faShieldVirus}
                                className={`h-20 ${response?.Prediction === 'Benign' ? 'text-green-700' : 'text-red-700'}`}
                            />
                        </div>
                        <div className='w-3/4 lg:text-left text-center text-balance'>
                            <p className='lg:text-[26px] text-[20px]'>
                                <span className={`h-20 font-semibold ${response?.Prediction === 'Benign' ? 'text-green-700' : 'text-red-700'}`}>{label_mapping[response.Prediction]}</span>
                            </p>
                            <span className='pt-2 flex flex-col'>
                                <a href={input} className='break-words'>
                                    {input}
                                </a>
                                <a href='https://www.example.com' className='break-words'>{domain}</a>
                            </span>
                        </div>
                    </div>
                    <GoogleSafe />
                    <div className='py-10'>
                        <p className='font-bold text-[20px] text-left border-b-[2px] border-customBlue'>Domain Details</p>
                    </div>
                    <div className="text-left lg:px-0">
                        {response?.response_domain?.[0] &&
                            typeof response.response_domain[0] === 'object' &&
                            !Array.isArray(response.response_domain[0]) ? (
                            Object.entries(response.response_domain[0]).map(([key, value]) => (
                                <div
                                    className="grid grid-cols-2 gap-4 border-b border-gray-300 py-2 items-center"
                                    key={key}
                                >
                                    {/* Key column */}
                                    <p className="font-bold text-gray-700 lg:text-start text-center break-words">
                                        {key}
                                    </p>
                                    {/* Value column */}
                                    <p className="text-gray-600 lg:text-start text-center break-words">
                                        {value != null && value !== "" ? value : "null"}
                                    </p>
                                </div>
                            ))
                        ) : (
                            <p className="text-gray-500">No valid data available for response domain.</p>
                        )}
                    </div>
                </div>
            ) : (
                <div>
                    <p className='text-center text-gray-500'>No response available. Please submit a URL for analysis.</p>
                    <video src={VideoDemo} className='flex-1 my-4' autoPlay muted loop controls/>
                </div>

            )
    );
};

export default Predict;



// Safe: The URL is safe.No threats detected.

// Defacement: The URL shows signs of defacement.Proceed with caution.

// Phishing: The URL is suspected of phishing.Do not visit.

// Malware: The URL is flagged for malware.Avoid it.

// <div className='text-left lg:px-0 px-4'>
//     {
//         Object.entries(response?.response_domain[0]).map(([key, value]) => {
//             return (
//                 <div
//                     className='flex lg:flex-row flex-col break-words lg:gap-10 gap-2 border-b border-gray-300 py-2 items-center lg:text-start text-center '
//                     key={key}
//                 >
//                     {/* Cột cho key */}
//                     <p
//                         className='flex-1 font-bold text-gray-700'
//                     >
//                         {key}
//                     </p>

//                     {/* Cột cho value */}
//                     <p
//                         className='flex-1 text-gray-600 p-2 break-words'
//                     >
//                         {value != null ? value : "null"}
//                     </p>
//                 </div>
//             );
//         })
//     }
// </div>