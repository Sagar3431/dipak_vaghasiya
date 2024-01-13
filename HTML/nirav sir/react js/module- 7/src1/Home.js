import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { fetchUsers, selectUsers, selectUsersError, selectUsersLoading } from './UserReducer'
import { Link } from 'react-router-dom';

function Home() {
    const users = useSelector(selectUsers);
    const isLoading = useSelector(selectUsersLoading);
    const error = useSelector(selectUsersError);
    const dispatch = useDispatch();
   
   

    useEffect(() => {
        dispatch(fetchUsers());
        
      }, [dispatch]);
    
      if (isLoading) {
        return <div>Loading...</div>;
      }
    
      if (error) {
        return <div>Error: {error}</div>;
      }
  return (
    <div>
         <div className='container'>
      <h1 className='my-3'>User List</h1>
      <div className='my-2'>
            <Link to="/Create" className='btn btn-info'>Add Users</Link>
        </div>
      <table className='table'>
        <thead className='table-dark'>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Username</th>
            <th>Action</th>
           
          </tr>
        </thead>
        <tbody>
          {users.map((user) => (
            <tr key={user.id}>
              <td>{user.id}</td>
              <td>{user.name}</td>
              <td>{user.email}</td>
              <td>{user.username}</td>
              <td>
                <button className='btn btn-success me-2'>Edit</button>
                <button className='btn btn-danger'>Delete</button>
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
