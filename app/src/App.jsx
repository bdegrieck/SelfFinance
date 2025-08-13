import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginPage from "./pages/pg_login_page";
import ForgotPassword from "./pages/pg_forgot_password";
import CreateUser from "./pages/pg_create_user";
import HomePage from "./pages/pg_home";

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LoginPage />} />
        <Route path="/forgot-password" element={<ForgotPassword />} />
        <Route path="/create-user" element={<CreateUser />} />
        <Route path="/home" element={<HomePage />} />
      </Routes>
    </Router>
  );
}
