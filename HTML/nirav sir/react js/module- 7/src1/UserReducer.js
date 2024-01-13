import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  users: [],
  loading: false,
  error: null,
};

const usersSlice = createSlice({
  name: 'users',
  initialState,
  reducers: {
    fetchUsersStart(state) {
      state.loading = true;
      state.error = null;
    },
    fetchUsersSuccess(state, action) {
      state.loading = false;
      state.users = action.payload;
    },
    fetchUsersFailure(state, action) {
      state.loading = false;
      state.error = action.payload;
    },
    addUserStart(state) {
      state.loading = true;
      state.error = null;
    },
    addUserSuccess(state, action) {
      state.loading = false;
      state.users.push(action.payload);
    },
    addUserFailure(state, action) {
      state.loading = false;
      state.error = action.payload;
    },
  },
});

export const {
  fetchUsersStart,
  fetchUsersSuccess,
  fetchUsersFailure,
  addUserStart,
  addUserSuccess,
  addUserFailure,
} = usersSlice.actions;

export const fetchUsers = () => async (dispatch) => {
  dispatch(fetchUsersStart());
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/users');
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    const users = await response.json();
    dispatch(fetchUsersSuccess(users));
  } catch (error) {
    dispatch(fetchUsersFailure(error.message));
  }
};

export const addUser = (userData) => async (dispatch) => {
  dispatch(addUserStart());
  try {
    const response = await fetch('https://jsonplaceholder.typicode.com/users', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userData),
    });

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    const newUser = await response.json();

    dispatch(addUserSuccess(newUser));
  } catch (error) {
    dispatch(addUserFailure(error.message));
  }
};

export const selectUsers = (state) => state.users.users;
export const selectUsersLoading = (state) => state.users.loading;
export const selectUsersError = (state) => state.users.error;

export default usersSlice.reducer;
