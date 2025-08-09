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
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");

  const handleCreateUser = async () => {
    if (
      !username ||
      !password ||
      !retypePassword ||
      !firstName ||
      !lastName ||
      !email
    ) {
      setError("Please fill in all fields");
      return;
    }

    if (password !== retypePassword) {
      setError("Passwords do not match");
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
          username,
          password,
          first_name: firstName,
          last_name: lastName,
          email,
        }),
      });

      const data = await response.json();

      if (response.ok) {
        alert("Account created! Please log in.");
      } else {
        setError(data.detail || "Account creation failed. Please try again.");
      }
    } catch (err) {
      console.error("Create user error:", err);
      setError("Network error. Please check your connection.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="create-user-page">
      <div className="create-user-form">
        <h1>Create Account</h1>
        {error && (
          <div style={{ color: "red", marginBottom: "1rem" }}>{error}</div>
        )}
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
        <input
          type="password"
          placeholder="Retype Password"
          value={retypePassword}
          onChange={(e) => setRetypePassword(e.target.value)}
          disabled={isLoading}
        />
        <input
          type="text"
          placeholder="First Name"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
          disabled={isLoading}
        />
        <input
          type="text"
          placeholder="Last Name"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
          disabled={isLoading}
        />
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          disabled={isLoading}
        />
        <button onClick={handleCreateUser} disabled={isLoading}>
          {isLoading ? "CREATING..." : "CREATE ACCOUNT"}
        </button>
        <Link to="/">Back to Login</Link>
      </div>
    </div>
  );
}
