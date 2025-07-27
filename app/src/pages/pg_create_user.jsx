import React, { useState } from "react";
import { Link } from "react-router-dom";
import "../App.css";


export default function CreateUser() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [retypePassword, setRetypePassword] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");

  return (
    <div className="create-user-page">
      <div className="create-user-form">
        <h1>Create Account</h1>
        <input 
          type="text" 
          placeholder="Username" 
          value={username}
          onChange={e => setUsername(e.target.value)}
        />
        <input 
          type="password" 
          placeholder="Password" 
          value={password}
          onChange={e => setPassword(e.target.value)}
        />
        <input 
          type="password" 
          placeholder="Retype Password" 
          value={retypePassword}
          onChange={e => setRetypePassword(e.target.value)}
        />
        <input 
          type="text" 
          placeholder="First Name" 
          value={firstName}
          onChange={e => setFirstName(e.target.value)}
        />
        <input 
          type="text" 
          placeholder="Last Name" 
          value={lastName}
          onChange={e => setLastName(e.target.value)}
        />
        <input 
          type="email" 
          placeholder="Email" 
          value={email}
          onChange={e => setEmail(e.target.value)}
        />
        <button>Create User</button>
        <Link to="/">Back to Login</Link>
      </div>
    </div>
  );
}
