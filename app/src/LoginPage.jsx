import React from "react";
import { Link } from "react-router-dom";
import logoSrc from "./assets/Logo.png";
import "./App.css";

export default function LoginPage() {
  return (
    <div className="login-page">
      <div className="login-panel left">
        <img className="login-logo" src={logoSrc} alt="Self Finance" />
      </div>

      <div className="login-panel right">
        <div className="login-form">
          <h1>Self Finance</h1>
          <input type="text" placeholder="Username" />
          <input type="password" placeholder="Password" />
          <button>LOG IN</button>
          <Link to="/forgot-password">Forgot Password?</Link>
        </div>
      </div>
    </div>
  );
}
