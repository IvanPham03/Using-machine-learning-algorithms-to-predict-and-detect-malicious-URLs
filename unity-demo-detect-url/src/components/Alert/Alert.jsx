import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { removeAlert } from '../../redux-toolkit/slice/alertSlice';
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faXmark } from '@fortawesome/free-solid-svg-icons';
import { AnimatePresence } from "motion/react"
import * as motion from "motion/react-client"
// Your message has been successfully sent. I will respond to you as soon as possible. Thank you!
const Alert = () => {
    const dispatch = useDispatch();
    // const [active, setActive] = useState(true) test
    const { active, text, image } = useSelector((state) => state.alert);
    // console.log(active);
    // handle clode button
    const handleClose = () => {
        dispatch(removeAlert());
        // setActive(false) 
    };
    useEffect(() => {
        if (active) {
            document.body.style.overflow = 'hidden'; // Disable scrolling
        } else {
            document.body.style.overflow = 'auto'; // Enable scrolling
        }

        // Cleanup function to reset style when the component is unmounted
        return () => {
            document.body.style.overflow = 'auto';
        };
    }, [active]);

    return (
        <AnimatePresence>
            {active && (
                <div

                    className="transition ease-linear z-100 flex justify-center items-center top-0 left-0 right-0 w-screen h-screen bg-blackrgba70 aria-labelledby='modal-title' role='dialog' aria-modal='true'"
                >
                    <motion.div
                        initial={{ opacity: 0, scale: 0.8, ease: "linear" }}
                        animate={{ opacity: 1, scale: 1, ease: "linear" }}
                        exit={{ opacity: 0, scale: 0.8, ease: "linear" }}
                        key="alert"
                        className="fixed z-1000 bg-white rounded lg:w-1/3 flex flex-col justify-center items-center gap-4 text-black hover:text-red-500">
                        <div className="w-full text-right p-2">
                            <FontAwesomeIcon
                                icon={faXmark}
                                className="lg:h-10 lg:w-10 h-6 w-6 hover:cursor-pointer"
                                onClick={handleClose}
                            />
                        </div>
                        <img src={image} alt="avt" className="lg:w-16 lg:h-16 h-10 w-10 rounded-full" />
                        <div>
                            <p className="text-black lg:p-6 p-3">{text}</p>
                        </div>
                    </motion.div>
                </div>
            )}
        </AnimatePresence>

    )
}

export default Alert
