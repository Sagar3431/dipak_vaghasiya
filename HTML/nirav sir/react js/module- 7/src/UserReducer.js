import { createSlice } from "@reduxjs/toolkit";
import {userData} from "./Data"


const userReducerData = createSlice({
    name:"users",
    initialState:userData,
    reducers:{
        addUsers:(state,action)=>{
            state.push(action.payload)
            console.log(action)
            console.log(action.payload)
        },
        deleteUser:(state,action)=>{
            
            return state.filter(user => user.id !== action.payload);
            
        },
        updateUser:(state,action)=>{
            const { id, name, email } = action.payload;
      const existingUser = state.find(user => user.id === id);
      if (existingUser) {
        existingUser.name = name;
        existingUser.email = email;
      }
        }
        
    }
})

// export const {addUsers} = userReducerData.actions;
// export const {deleteUser} = userReducerData.actions;
export const {addUsers , deleteUser,updateUser}=userReducerData.actions
export default userReducerData.reducer;