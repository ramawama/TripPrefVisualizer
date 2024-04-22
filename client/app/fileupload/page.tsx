"use client";
import React, { useState } from 'react';
import axios from 'axios';
import Link from "next/link";

function App() {
    const [filePath, setFilePath] = useState('');
    const [msg, setMsg] = useState("");

    const handleInputChange = (event) => {
        setFilePath(event.target.value);
    };

    const handleSubmit = () => {
        setMsg("file path: " + filePath);
        console.log(filePath);
        axios.post('http://localhost:5000/upload-path', { filePath })
            .then(response => alert(`Server response: ${response.data}`))
            .catch(error => alert(`Error: ${error.message}`));
    };

    return (
        <div>
          <div className="hero min-h-screen" style={{backgroundImage: 'url(/mountainLandscape.jpg)'}}>
            <div className="hero-overlay bg-opacity-60">
              <div className='flex max-h-screen justify-center'>
                <h1 className="mt-20 text-7xl font-bold">Enter File Path</h1></div>
            <div className="flex max-h-screen justify-center mt-10">
            <button  
                className="btn btn-sm btn-neutral btn-outline"><li><Link href="/">Home</Link></li>
            </button>
            </div>
            <div className="flex-col items-center hero max-h-screen justify-center items-start">
            <div className="flex hero-content text-center text-neutral-content max-w-w mt-20">

            <div className="mb-20">
            <input type="text" 
                placeholder="Enter File Path" 
                className="input input-bordered input-secondary w-full max-w-xs" 
                value={filePath}
                onChange={handleInputChange}
            />
            </div>
            <div className='mb-20'>
            <button 
                onClick={handleSubmit} 
                className="btn btn-secondary">Submit Path</button>
            </div>
            </div>
            </div>
            </div>

            <div className='mt-20'>
            <h2>{msg && msg}</h2>
            </div>

            </div>
        </div>
    );
}

export default App;