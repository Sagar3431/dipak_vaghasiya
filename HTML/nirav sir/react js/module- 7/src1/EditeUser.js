import React, { useState, useEffect } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { updateUser } from './UserReducer';
import { useDispatch, useSelector } from 'react-redux';

function EditUser() {
  const { id } = useParams(); // Assuming you're passing the user ID through React Router's useParams
  const users = useSelector(state => state.users);
  const dispatch = useDispatch();
  
  const [userData, setUserData] = useState({
    id: '',
    name: '',
    email: ''
  });

  useEffect(() => {
    // Find the user from the users array based on the provided ID
    const userToEdit = users.find(user => user.id === Number(id));
    
    if (userToEdit) {
      setUserData({
        id: userToEdit.id,
        name: userToEdit.name,
        email: userToEdit.email
      });
    }
  }, [id, users]);

  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    dispatch(updateUser(userData));
    navigate("/", { replace: true });
  };
   
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setUserData({ ...userData, [name]: value });
  };

  return (
    <div>
      <div className="container row justify-content-center text-start">
        <div className='col-6'>
          <form onSubmit={handleSubmit}>
            <h1 className='my-5'>Edit User</h1>
            <div className="col-12">
              <label className="form-label">Id: </label>
              <input value={userData.id} disabled type="text" className="form-control" name="id" />
            </div>
            <div className="col-12">
              <label className="form-label">Name: </label>
              <input value={userData.name} type="text" className="form-control" name="name" onChange={handleInputChange} />
            </div>
            <div className="col-12">
              <label className="form-label">Email: </label>
              <input value={userData.email} type="text" className="form-control" name="email" onChange={handleInputChange} />
            </div>
            <div className="col-12">
              <button className='btn btn-success mt-3'>Save</button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default EditUser;
