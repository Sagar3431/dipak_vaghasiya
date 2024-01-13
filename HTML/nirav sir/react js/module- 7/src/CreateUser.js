import React, { useState } from 'react'
import { useDispatch, useSelector } from 'react-redux';
import { addUsers } from './UserReducer';
import { useNavigate } from 'react-router-dom';


function CreateUser() {
  const users = useSelector(state=>state.users)
 const dispatch= useDispatch();
 const navigate = useNavigate();
  
  const[name,setName]=useState("");
  const[email,setEmail]=useState("");
  const handlesubmit=(e)=>{
    e.preventDefault();
    dispatch(addUsers({id:users[users.length -1].id+1,name,email}))
    navigate("/")

  }
  return (
    <div>
      <div className="container row justify-content-center text-start">
        <div className="col-6">
       <form onSubmit={handlesubmit}>
        <h1 className='my-5'>Add user</h1>
        <div className='col-12'>
        <label className='form-label'>Id</label>
        <input disabled="disabled" className='form-control' type="text" />
        </div>

        <div>
        <label className='form-label'>Name</label>
        <input value={name} className='form-control' type="text" onChange={(e)=>{setName(e.target.value)}} />
        </div>

        <div>
        <label className='form-label'>Email</label>
        <input value={email} className='form-control' type="text" onChange={(e)=>{setEmail(e.target.value)}}/>
        </div>

        <div>
        <button className='btn btn-info me-2 mt-2'>Save</button>
        </div>
       </form>
       </div>
      </div>
    </div>
  )
}

export default CreateUser
