import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { addUser, selectUsers } from './UserReducer';
import { useNavigate } from 'react-router-dom';

function Create() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const users = useSelector(selectUsers);

  const getNextId = () => {
    if (users.length === 0) {
      return 1; // Start with ID 1 if no users exist
    } else {
      const lastId = users[users.length - 1].id;
      return lastId + 1; // Increment the last user's ID by 1 to get the next ID
    }
  };

  const [newUserData, setNewUserData] = useState({
    id: getNextId(),
    name: '',
    email: '',
    username: '',
    // Add other fields as needed (phone, website, company)
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewUserData({
      ...newUserData,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    dispatch(addUser({
      ...newUserData,
      id: getNextId() // Set the ID to the next available ID
    }));

    setNewUserData({
      id: getNextId()+1,
      name: '',
      email: '',
      username: '',
      // Reset other fields here as well
    });

    navigate('/');
  };

  return (
    <div>
      <h1>Create User</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" name="name" placeholder="Name" value={newUserData.name} onChange={handleInputChange} />
        <input type="text" name="email" placeholder="Email" value={newUserData.email} onChange={handleInputChange} />
        <input type="text" name="username" placeholder="Username" value={newUserData.username} onChange={handleInputChange} />

        {/* Add other input fields for phone, website, etc. */}
        <button type="submit">Add User</button>
      </form>
    </div>
  );
}

export default Create;
