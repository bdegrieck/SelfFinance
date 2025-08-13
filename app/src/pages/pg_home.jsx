import React, { useState, useEffect } from "react";
import { useLocation } from "react-router-dom";
import Sidebar from "../components/cmp_sidebar";

export default function HomePage() {
    const [userName, setUserName] = useState('');
    const location = useLocation();
    
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
                {/* Add your home page content here */}
            </div>
        </div>
    );
}