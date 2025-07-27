import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import LoginPage from "./pages/pg_login_page";
import ForgotPassword from "./pages/pg_forgot_password";
import CreateUser from "./pages/pg_create_user";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/forgot-password" element={<ForgotPassword />} />
        <Route path="/create-user" element={<CreateUser />} />
      </Routes>
    </Router>
  );
}
