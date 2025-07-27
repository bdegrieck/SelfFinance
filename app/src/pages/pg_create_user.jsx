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

  const handleCreateUser = async () => {
    if (!username || !password) {
      setError("Please enter both username and password");
      return;
    }

    setIsLoading(true);
    setError("");

    try {
      const response = await fetch("http://localhost:8000/create-user", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: username,
          password: password,
          retyped_password: retypePassword,
          first_name: firstName,
          last_name: lastName,
          email: email
        }),
      });

      const data = await response.json();

      if (response.ok) {
        console.log("Login successful:", data);
        // Here you can redirect to dashboard or store user session
        alert("Login successful! Welcome, " + data.username);
      } else {
        setError(data.detail || "Login failed. Please try again.");
      }
    } catch (err) {
      console.error("Login error:", err);
      setError("Network error. Please check your connection.");
    } finally {
      setIsLoading(false);
    }
  };

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
        <button onClick={handleCreateUser}>Log In</button>
        <Link to="/">Back to Login</Link>
      </div>
    </div>
  );
}
