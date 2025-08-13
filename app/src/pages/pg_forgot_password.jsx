import React from "react";
import { Link } from "react-router-dom";

export default function ForgotPassword() {
  return (
    <div className="flex justify-center items-center h-screen bg-gradient-to-br from-self-finance-green to-self-finance-dark-green font-primary">
      <div className="bg-white p-10 rounded-3xl shadow-2xl w-full max-w-md text-center font-primary">
        <h1 className="text-gray-800 mb-4 text-3xl font-semibold">Forgot Password</h1>
        <p className="text-gray-600 mb-8 leading-relaxed text-base font-normal">
          Please enter your email address to reset your password.
        </p>
        <input 
          type="email" 
          placeholder="Email" 
          className="w-full p-4 mb-6 border-2 border-gray-200 rounded-xl font-normal text-base transition-all duration-300 focus:border-self-finance-green focus:shadow-lg focus:shadow-self-finance-green/10 box-border"
        />
        <button className="w-full p-4 bg-self-finance-green text-white border-none font-semibold text-base rounded-xl cursor-pointer mb-6 transition-all duration-300 hover:bg-self-finance-dark-green hover:-translate-y-0.5 active:translate-y-0">
          Send Reset Link
        </button>
        <Link to="/" className="block text-self-finance-green no-underline font-medium text-sm transition-colors duration-300 hover:text-self-finance-darker-green hover:underline">
          Back to Login
        </Link>
      </div>
    </div>
  );
}
