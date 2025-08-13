import React from "react";
import { NavLink } from "react-router-dom";
import logo from "../assets/img_logo.png";
import homeIcon from "../assets/img_btn_home.png";
import analysisIcon from "../assets/img_btn_analysis.png";
import addExpenseIcon from "../assets/img_btn_add_expense.png";
import barsImage from "../assets/bars.svg";

export default function Sidebar() {
  return (
    <div className="w-20 h-screen bg-self-finance-green flex flex-col items-center fixed left-0 top-0 shadow-lg">
      {/* Logo Section */}
      <div className="bg-white w-full py-5 flex flex-col items-center mb-5">
        <img src={logo} alt="Self Finance Logo" className="w-10 h-10 mb-2" />
      </div>
      
      <div className="flex flex-col items-center justify-around flex-1 py-5">
        <NavLink to="/" className="no-underline text-inherit flex items-center justify-center w-12 h-12 rounded-lg transition-colors duration-200 hover:bg-white/20" end>
          <div className="flex items-center justify-center w-full h-full">
            <img src={homeIcon} alt="Home" className="w-10 h-10 filter brightness-0" />
          </div>
        </NavLink>
        
        <NavLink to="/analysis" className="no-underline text-inherit flex items-center justify-center w-12 h-12 rounded-lg transition-colors duration-200 hover:bg-white/20">
          <div className="flex items-center justify-center w-full h-full">
            <img src={analysisIcon} alt="Analysis" className="w-10 h-10 filter brightness-0" />
          </div>
        </NavLink>
        
        <NavLink to="/add-expense" className="no-underline text-inherit flex items-center justify-center w-12 h-12 rounded-lg transition-colors duration-200 hover:bg-white/20">
          <div className="flex items-center justify-center w-full h-full">
            <img src={addExpenseIcon} alt="Add Expense" className="w-10 h-10 filter brightness-0" />
          </div>
        </NavLink>
      </div>
      
      <div className="flex items-center justify-center mb-5 h-10">
        <img src={barsImage} alt="Bar Graph" className="w-6 h-10" />
      </div>
    </div>
  );
}