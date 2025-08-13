import React, { useState } from "react";
import { Link, Navigate, useNavigate } from "react-router-dom";

export default function CreateUser() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [retypePassword, setRetypePassword] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");
  const navigate = useNavigate();

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
        navigate("/")
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
    <div className="flex justify-center items-center h-screen bg-gradient-to-br from-self-finance-green to-self-finance-dark-green font-primary">
      <div className="bg-white p-10 rounded-3xl shadow-2xl w-full max-w-md text-center font-primary">
        <h1 className="text-gray-800 mb-6 text-3xl font-semibold">Create Account</h1>
        {error && (
          <div className="text-red-500 mb-4">{error}</div>
        )}
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          disabled={isLoading}
          className="w-full p-4 mb-6 border-2 border-gray-200 rounded-xl font-normal text-base transition-all duration-300 focus:border-self-finance-green focus:shadow-lg focus:shadow-self-finance-green/10 box-border disabled:opacity-50"
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          disabled={isLoading}
          className="w-full p-4 mb-6 border-2 border-gray-200 rounded-xl font-normal text-base transition-all duration-300 focus:border-self-finance-green focus:shadow-lg focus:shadow-self-finance-green/10 box-border disabled:opacity-50"
        />
        <input
          type="password"
          placeholder="Retype Password"
          value={retypePassword}
          onChange={(e) => setRetypePassword(e.target.value)}
          disabled={isLoading}
          className="w-full p-4 mb-6 border-2 border-gray-200 rounded-xl font-normal text-base transition-all duration-300 focus:border-self-finance-green focus:shadow-lg focus:shadow-self-finance-green/10 box-border disabled:opacity-50"
        />
        <input
          type="text"
          placeholder="First Name"
          value={firstName}
          onChange={(e) => setFirstName(e.target.value)}
          disabled={isLoading}
          className="w-full p-4 mb-6 border-2 border-gray-200 rounded-xl font-normal text-base transition-all duration-300 focus:border-self-finance-green focus:shadow-lg focus:shadow-self-finance-green/10 box-border disabled:opacity-50"
        />
        <input
          type="text"
          placeholder="Last Name"
          value={lastName}
          onChange={(e) => setLastName(e.target.value)}
          disabled={isLoading}
          className="w-full p-4 mb-6 border-2 border-gray-200 rounded-xl font-normal text-base transition-all duration-300 focus:border-self-finance-green focus:shadow-lg focus:shadow-self-finance-green/10 box-border disabled:opacity-50"
        />
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          disabled={isLoading}
          className="w-full p-4 mb-6 border-2 border-gray-200 rounded-xl font-normal text-base transition-all duration-300 focus:border-self-finance-green focus:shadow-lg focus:shadow-self-finance-green/10 box-border disabled:opacity-50"
        />
        <button 
          onClick={handleCreateUser} 
          disabled={isLoading}
          className="w-full p-4 bg-self-finance-green text-white border-none font-semibold text-base rounded-xl cursor-pointer mb-6 transition-all duration-300 hover:bg-self-finance-dark-green hover:-translate-y-0.5 active:translate-y-0 disabled:opacity-50"
        >
          {isLoading ? "CREATING..." : "CREATE ACCOUNT"}
        </button>
        <Link to="/" className="block text-self-finance-green no-underline font-medium text-sm mt-2 transition-colors duration-300 hover:text-self-finance-darker-green hover:underline">
          Back to Login
        </Link>
      </div>
    </div>
  );
}
