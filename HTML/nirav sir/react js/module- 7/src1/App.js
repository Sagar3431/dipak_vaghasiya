
import './App.css';
import Home from './Home';

import '../node_modules/bootstrap/dist/css/bootstrap.css'
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Create from './Create';

function App() {
  return (
    <div className="App">
    <BrowserRouter>
    <Routes>
      <Route path='/' element={<Home/>}></Route>
      <Route path='/Create' element={<Create/>}></Route>
    </Routes>
    </BrowserRouter>
    </div>
  );
}

export default App;
