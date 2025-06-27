import React from 'react';
import './App.css';

export default function App() {
  return (
    <div className="app-container">
      <header className="app-header">
        <div className="logo">Self Finance</div>
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
