import React from "react";
import { Link } from "react-router-dom";
import "./App.css";

export default function CreateUser() {
  return (
    <div className="create-user-page">
      <div className="create-user-form">
        <h1>Create Account</h1>
        <input type="text" placeholder="Username" />
        <input type="password" placeholder="Password" />
        <input type="email" placeholder="Email" />
        <button>Create User</button>
        <Link to="/">Back to Login</Link>
      </div>
    </div>
  );
}
