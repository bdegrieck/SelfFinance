import React, { useState } from "react";
import { Link } from "react-router-dom";
import "../App.css";

function PasswordInput({ value, onChange, placeholder }) {
  const [show, setShow] = useState(false);

  return (
    <div style={{ position: "relative", marginBottom: "1.5rem" }}>
      <input 
        type={show ? "text" : "password"}
        value={value}
        onChange={onChange}
        placeholder={placeholder}
        style={{ width: "100%", paddingRight: "2.75rem" }}
      />
      <button
        type="button"
        onClick={() => setShow(!show)}
        style={{
          position: "absolute", 
          right: "0.75rem", 
          top: "50%", 
          transform: "translateY(-50%)",
          background: "none",
          border: "none",
          cursor: "pointer",
          padding: 0,
          fontSize: "1rem",
          color: "#00c843"
        }}
      >
        {show ? "🙈" : "👁️"}
      </button>
    </div>
  );
}

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
        <PasswordInput
          value={password}
          onChange={e => setPassword(e.target.value)}
          placeholder="Password"
        />
        <PasswordInput
          value={retypePassword}
          onChange={e => setRetypePassword(e.target.value)}
          placeholder="Retype Password"
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
