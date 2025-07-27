import React from "react";
import { NavLink } from "react-router-dom";
import homeIcon from "../assets/home.png";
import reportIcon from "../assets/report.png";
import editIcon from "../assets/edit.png";
import chartIcon from "../assets/chart.png";
import "./Sidebar.css";

export default function Sidebar() {
  return (
    <nav className="sidebar">
      <NavLink to="/dashboard">
        <img src={homeIcon}   alt="Dashboard"   />
      </NavLink>
      <NavLink to="/track">
        <img src={editIcon}   alt="Track Expense" />
      </NavLink>
      <NavLink to="/investments">
        <img src={chartIcon}  alt="Investments" />
      </NavLink>
      <NavLink to="/reports">
        <img src={reportIcon} alt="Reports"     />
      </NavLink>
    </nav>
  );
}