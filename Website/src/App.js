import React, { useState } from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
} from 'react-router-dom';
import FileUpload from './components/fileUpload';
import InfoCard from './components/infoCard';
import List from './components/list';
import SignUp from './components/signUp';
import Login from './components/login';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/info-card" element={<InfoCard />} />
        <Route path="/list" element={<List />} />
        <Route path="/dashboard" element={<FileUpload />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/login" element={<Login />} />
        <Route path="/" element={<Navigate replace to="/login" />} />
      </Routes>
    </Router>
  );
}

export default App;
