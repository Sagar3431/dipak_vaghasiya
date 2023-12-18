
import { BrowserRouter, Link, Route, Router, Routes } from 'react-router-dom';
import './App.css';
import Home from './Home';
import About from './About';
import Service from './Service';
import Service1 from './Service1';
import Service2 from './Service2';
import { useRef } from 'react';

function App() {
  const sagar=useRef();
  console.log(sagar)
  return (
    <div className="App">
     <BrowserRouter>
     <Link ref={sagar} to="/Home">Home</Link>
     {' '} &nbsp;&nbsp;&nbsp;
     <Link to="/About">About</Link>{' '} &nbsp;&nbsp;&nbsp;
     <Link to="/Service">Service</Link>
     
     <Routes>
      <Route path='/Home' element={<Home/>}>

      </Route>
      <Route path='/About' element={<About/>}>
        
      </Route>
      <Route path='/Service' element={<Service/>}>
        <Route path='/Service/Service1' element={<Service1/>}>

        </Route>
        <Route path='/Service/Service2' element={<Service2/>}>
          
        </Route>
      </Route>
     </Routes>
     
     </BrowserRouter>
    </div>
  );
}

export default App;
