import React from "react";
import logoSrc from "./assests/Logo.png";
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
          <a href="#">Forgot Password?</a>
        </div>
      </div>
    </div>
  );
}
