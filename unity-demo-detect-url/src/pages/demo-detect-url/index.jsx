import React from 'react'
import { Input, Predict } from './components'
const index = () => {
  return (
    <div className='h-full flex justify-center text-center mx-auto'>
      <div className='lg:w-2/3 w-full lg:my-10 lg:px-6 px-4'>
        <Input />
        <Predict />
      </div>
    </div>
  )
}

export default index
