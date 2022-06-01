import logo from './logo.svg';
import './App.css';

import Home from './components/Home';
import LoginPage from './components/LoginPage';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import React, { Component }  from 'react';

function App() {
  return (
        <BrowserRouter>

      <Routes>
          <Route path="/" element={<LoginPage/>}  />
          <Route path="/home" element={<Home/>}  />
      </Routes>
      </BrowserRouter>

      
  );
  
}

export default App;
