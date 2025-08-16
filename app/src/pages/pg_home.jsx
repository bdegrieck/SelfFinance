import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import Sidebar from "../components/cmp_sidebar";
import CustomPieChart from "../components/cmp_piechart";

export default function HomePage() {
    const [userName, setUserName] = useState('');
    const location = useLocation();
    
    // Sample financial data for the pie chart
    const pieChartData = [
        { name: 'Groceries', value: 450 },
        { name: 'Entertainment', value: 200 },
        { name: 'Transportation', value: 300 },
        { name: 'Dining Out', value: 180 },
        { name: 'Shopping', value: 250 },
        { name: 'Utilities', value: 150 },
        { name: 'Healthcare', value: 120 }
    ];
    
    useEffect(() => {
        // Get user data from navigation state or localStorage
        const userData = location.state?.userData || JSON.parse(localStorage.getItem('user') || '{}');
        // Use first_name if available, otherwise fall back to username
        const displayName = userData.first_name || userData.username;
        if (displayName) {
            setUserName(displayName);
        }
    }, [location]);
    
    return (
        <div className="flex min-h-screen bg-gray-100">
            <Sidebar />
            <div className="flex-1 ml-20 p-8 bg-white min-h-screen">
                <h1 className="text-3xl font-semibold text-gray-800 mb-4 text-center">
                    Welcome to Self Finance{userName && `, ${userName}`}!
                </h1>
                <p className="text-lg text-gray-600 leading-relaxed text-center">
                    You have successfully logged in!
                </p>
                {/* Pie Chart */}
                <div className="mt-8 max-w-2xl mx-auto">
                    <h2 className="text-xl font-semibold text-gray-700 mb-4 text-center">Monthly Spending Overview</h2>                    
                </div>
                <CustomPieChart data={pieChartData} width={1500}  height={1500}/>
            </div>
        </div>
    );
}