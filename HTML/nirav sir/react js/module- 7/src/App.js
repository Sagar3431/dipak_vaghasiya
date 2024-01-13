
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import './App.css';
import Home from './Home';
import "../node_modules/bootstrap/dist/css/bootstrap.css"
import CreateUser from './CreateUser';
import EditeUser from './EditeUser';


function App() {
  
  
  return (
    <div className="App">
     <BrowserRouter>
     <Routes>
      <Route path="/" element={<Home/>}></Route>
      <Route path="/Create" element={<CreateUser/>}></Route>
      <Route path="/Edit/:empid" element={<EditeUser/>}></Route>
     </Routes>
     </BrowserRouter>
    </div>
  );
}

export default App;
