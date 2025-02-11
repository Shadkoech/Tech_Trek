import React from 'react'

const UserItem = () => {
  return (
    <div className='flex items-center justify-between gap-2 border rounded-[8px] p-2'>
        <div className='avatar rounded-full min-h-8 min-w-8 bg-lime-500 text-white font-[700] flex items-center justify-center'>
            <p>SK</p>
        </div>
        <div className='grow'>
            <p className='text-[16px] font-bold'>Koech SK</p>
            <p className='text-[12px] text-neutral-500'>koech@gmail.com</p>
        </div>
    </div>
  )
}

export default UserItem
