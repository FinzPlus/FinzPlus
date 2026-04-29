/* 📂 ARCHIVO: src/App.jsx */
import React from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Registro from './pages/Registro';
import Dashboard from './pages/Dashboard';

function App() {
  return (
    <Router>
      <div className="app-container">
        {/* Barra de Navegación Simple con Bootstrap */}
        <nav className="navbar navbar-expand-lg navbar-dark bg-primary mb-4 shadow">
          <div className="container">
            <Link className="navbar-brand font-weight-bold" to="/">Finz+</Link>
            <div className="navbar-nav">
              <Link className="nav-link" to="/">Registrarse</Link>
              <Link className="nav-link" to="/dashboard">Mi Panel</Link>
            </div>
          </div>
        </nav>

        {/* Definición de Rutas */}
        <div className="container">
          <Routes>
            <Route path="/" element={<Registro />} />
            <Route path="/dashboard" element={<Dashboard />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;