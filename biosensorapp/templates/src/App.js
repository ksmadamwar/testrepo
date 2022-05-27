import logo from './logo.svg';
import './App.css';

import Home from './components/Home';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import React, { Component }  from 'react';

function App() {
  return (
        <BrowserRouter>

      <Routes>
          <Route path="/" element={<Home/>}  />
      </Routes>
      </BrowserRouter>

      
  );
  
}

export default App;
