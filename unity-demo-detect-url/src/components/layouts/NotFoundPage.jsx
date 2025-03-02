import React from 'react'
import PacmanLoader from "react-spinners/ClipLoader";

import logo from '../../assets/images/logo.png'
const NotFoundPage = () => {

  return (
    <div className="w-screen h-screen flex flex-col justify-center items-center">
      <div>
        <img src={logo} alt="logo" className='w-32 my-10' />
      </div>

      <p className='text-[30px] h-fit flex justify-center items-center'>The website developing, thank you for visiting... <PacmanLoader /></p>
    </div>
  )
}

export default NotFoundPage
