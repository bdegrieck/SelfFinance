import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginPage from "./LoginPage";
import ForgotPassword from "./ForgotPassword";
import CreateUser from "./CreateUser";

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
