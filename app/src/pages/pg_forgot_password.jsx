import React from "react";
import { Link } from "react-router-dom";
import "../App.css";

export default function ForgotPassword() {
  return (
    <div className="forgot-password-page">
      <div className="forgot-password-form">
        <h1>Forgot Password</h1>
        <p>Please enter your email address to reset your password.</p>
        <input type="email" placeholder="Email" />
        <button>Send Reset Link</button>
        <Link to="/">Back to Login</Link>
      </div>
    </div>
  );
}
