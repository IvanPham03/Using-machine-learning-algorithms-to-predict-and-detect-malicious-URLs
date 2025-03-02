import React, { useEffect } from 'react';
import { AnimatePresence, motion } from 'motion/react';
import Image from '../../assets/images/logo.png';
import {useSelector } from 'react-redux';
const Spinner = () => {
    const {active} = useSelector(s => s.spinner);
    // console.log("log:", active);
    

    useEffect(() => {
        if (active) {
            document.body.style.overflow = 'hidden'; // Disable scrolling
        } else {
            document.body.style.overflow = 'auto'; // Enable scrolling
        }

        return () => {
            document.body.style.overflow = 'auto';
        };
    }, [active]);

    const radius = 50; // Bán kính quỹ đạo (px)

    return (
        <AnimatePresence>
            {active && (
                <div
                    className="transition ease-linear z-100 flex justify-center items-center top-0 left-0 right-0 w-screen h-screen bg-blackrgba70"
                    aria-labelledby="modal-title"
                    role="dialog"
                    aria-modal="true"
                >
                    <div className="w-[200px] h-[200px] relative">
                        {/* Hình ảnh chạy theo quỹ đạo hình tròn */}
                        <div className='translate-x-1/3 translate-y-full'>
                            <motion.img
                                src={Image}
                                alt="orbiting-image"
                                className="h-10 w-10"
                                animate={{
                                    x: Array.from({ length: 361 }, (_, i) =>
                                        radius * Math.cos((i * Math.PI) / 180)
                                    ),
                                    y: Array.from({ length: 361 }, (_, i) =>
                                        radius * Math.sin((i * Math.PI) / 180)
                                    ),
                                }}
                                transition={{
                                    duration: 0.5, // Thời gian quay hết vòng
                                    repeat: Infinity,
                                    ease: "linear",
                                }}
                            />
                        </div>
                    </div>
                </div>
            )}
        </AnimatePresence>
    );
};

export default Spinner;
