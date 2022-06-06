import logo from './logo.svg';
import './App.css';
import Formulaire from './components/Formulaire';
// 

import React from 'react';
import axios from 'axios'
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Form from './components/Form';

 

class App extends React.Component { 
  render() { 
      return(
          <BrowserRouter>
          <Routes>
              <Route path="/formulaire" element={<Formulaire/>}/>
              <Route path="/form" element={<Form/>}/>
              
          </Routes>
          </BrowserRouter>
         
      )} 
} 

export default App;
