import React from 'react';
import '../animations.css';


const Error = () => {
    return (
        <div className="flex items-center justify-center min-h-screen gradient-background-err">
            <div className="bg-white p-8 rounded-lg shadow-lg text-center">
                <h1 className="text-3xl font-bold text-red-600 mb-4">
                    Błąd 404
                </h1>
                <p className="text-gray-700 mb-6">
                    Przykro nam, ale taka strona nie istnieje.
                </p>
                <a href="/" className="text-blue-500 hover:text-blue-700 transition duration-300">
                    Wróć do strony głównej
                </a>
            </div>
        </div>
    );
};

export default Error;
