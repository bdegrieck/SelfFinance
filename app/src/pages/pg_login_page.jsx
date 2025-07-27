import React, { useState } from "react";
import { Link } from "react-router-dom";
import logoSrc from "../assets/img_logo.png";
import "../App.css";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  const handleLogin = async () => {
    if (!username || !password) {
      setError("Please enter both username and password");
      return;
    }

    setIsLoading(true);
    setError("");

    try {
      const response = await fetch("http://localhost:8000/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          username: username,
          password: password,
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
    <div className="login-page">
      <div className="login-panel left">
        <img className="login-logo" src={logoSrc} alt="Self Finance" />
      </div>

      <div className="login-panel right">
        <div className="login-form">
          <h1>Self Finance</h1>
          {error && <div style={{ color: "red", marginBottom: "1rem" }}>{error}</div>}
          <input 
            type="text" 
            placeholder="Username" 
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            disabled={isLoading}
          />
          <input 
            type="password" 
            placeholder="Password" 
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            disabled={isLoading}
          />
          <button onClick={handleLogin} disabled={isLoading}>
            {isLoading ? "LOGGING IN..." : "LOG IN"}
          </button>
          <Link to="/forgot-password">Forgot Password?</Link>
          <Link to="/create-user" className="create-account-btn">Create Account</Link>
        </div>
      </div>
    </div>
  );
}
