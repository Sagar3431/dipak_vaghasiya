import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { Link, useNavigate } from 'react-router-dom'
import { deleteUser } from './UserReducer'

function Home() {
    const users =useSelector(state=>state.users)
   const dispatch = useDispatch()
   const Navigate = useNavigate()
  

   const loadDelete =(id)=>{
            //  dispatch(deleteusers(id))
            dispatch(deleteUser(id))
            console.log(id)
   }

   const loadEdit =(id)=>{
    
    Navigate("/Edit/"+id)
    
    
   }
   
  return (
    <div>
       <div className="container">

        <h3 className='my-3'>Users Data</h3>
        <div className='my-3'>
            <Link to="/Create" className='btn btn-info'>Add Users</Link>
        </div>
        <table className='table'>
        <thead className='table-dark'>
            <tr>
                <td>Id</td>
                <td>Name</td>
                <td>Email</td>
                <td>Action</td>
            </tr>
        </thead>
        <tbody>
            {users.map((e)=>(
                <tr key={e.id}>
                <td>{e.id}</td>
                <td>{e.name}</td>
                <td>{e.email}</td>
                <td>
                    <button className='btn btn-success me-2' onClick={()=>{loadEdit(e.id)}}>Edit</button>
                    <button className='btn btn-danger' onClick={()=>{loadDelete(e.id)}}>Delete</button>
                </td>
            </tr>
            ))}
        </tbody>
        </table>
       </div>
    </div>
  )
}

export default Home
