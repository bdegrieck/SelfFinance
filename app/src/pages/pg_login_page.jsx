import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import logoSrc from "../assets/img_logo.png";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async () => {
    if (!username || !password) {
      setError("Please enter both username and password");
      return;
    }

    setIsLoading(true);
    setError("");

    try {
      const response = await fetch("http://localhost:8000/login-user", {
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
        // Store user session with data from server
        localStorage.setItem('user', JSON.stringify(data.data));
        console.log("Stored user data:", localStorage.getItem("user"))
        
        // Redirect to home page with user data
        navigate("/home", { state: { userData: data.data } });
      } else {
        // Always try to use the server's detail message first
        setError(data.detail || data.message || `Error ${response.status}: Please try again.`);
      }
    } catch (err) {
      console.error("Login error:", err);
      setError("Network error. Please check your connection.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex h-screen font-primary">
      <div className="flex-1 flex justify-center items-center bg-white">
        <img className="max-w-[70%] h-auto" src={logoSrc} alt="Self Finance" />
      </div>

      <div className="flex-1 flex justify-center items-center bg-self-finance-green">
        <div className="bg-white p-8 rounded-2xl shadow-lg w-full max-w-sm text-center font-primary">
          <h1 className="mb-6 text-2xl font-semibold">Self Finance</h1>
          {error && <div className="text-red-500 mb-4">{error}</div>}
          <input 
            type="text" 
            placeholder="Username" 
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            disabled={isLoading}
            className="w-full p-3 mb-4 border border-gray-300 rounded-lg font-normal disabled:opacity-50"
          />
          <input 
            type="password" 
            placeholder="Password" 
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            disabled={isLoading}
            className="w-full p-3 mb-4 border border-gray-300 rounded-lg font-normal disabled:opacity-50"
          />
          <button 
            onClick={handleLogin} 
            disabled={isLoading}
            className="w-full p-3 bg-self-finance-green text-white border-none font-bold rounded-lg cursor-pointer mb-4 disabled:opacity-50"
          >
            {isLoading ? "LOGGING IN..." : "LOG IN"}
          </button>
          <Link to="/forgot-password" className="block text-gray-600 no-underline text-sm font-normal">
            Forgot Password?
          </Link>
          <Link to="/create-user" className="block text-self-finance-green no-underline text-sm font-medium mt-2 transition-colors duration-300 hover:text-self-finance-darker-green hover:underline">
            Create Account
          </Link>
        </div>
      </div>
    </div>
  );
}
