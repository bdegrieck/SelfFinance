import React from 'react';
import './App.css';
import Logo from'./logo.jsx'

export default function App() {
  return (
    <div className="app-container">
      <header className="app-header">
        <Logo />
        <h1 className="welcome">Welcome Ben</h1>
      </header>
      <div className="button-container">
        <button>Track Expense</button>
        <button>View Investments</button>
        <button>View Reports</button>
      </div>
    </div>
  );
}
