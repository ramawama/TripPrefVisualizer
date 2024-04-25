//WELCOME PAGE

"use client";

import { useState, useEffect } from 'react';
import { MouseEvent } from "react";
import axios from "axios";
import Link from "next/link";



function Home() {
  const [uploaded, setUploaded] = useState(false);
  const [filePath, setFilePath] = useState('');
  const [msg, setMsg] = useState("");

  const handleInputChange = (event) => {
      setFilePath(event.target.value);
  };

  const handleSubmit = () => {
      setMsg("file path: " + filePath);
      setUploaded(true);
      console.log(filePath);
      axios.post('http://localhost:5000/upload-path', { filePath })
          .then(response => alert(`Server response: ${response.data}`))
          .catch(error => alert(`Error: ${error.message}`));
  };

  return (
    <>
    <div className="navbar bg-base-100">
      <>
        <a className="btn btn-ghost text-xl"  href="/displaydata"> display data</a>
        <a className="btn btn-ghost text-xl"  href="/schedules"> schedules </a> 
        </>
        <a className="btn btn-ghost text-xl"  href="/about"> about </a>
    </div>
    <div className="hero min-h-screen" style={{backgroundImage: 'url(/mountainLandscape.jpg)'}}>
        <div className="hero-overlay bg-opacity-60"></div>
          <div className="hero-content text-center text-neutral-content">
            <div className="max-w-md">
              <br /><br />
              <h1 className="text-7xl font-bold">WELCOME CORE TRIP LEADERS</h1>
              <br /><br />
              <h1 className="mb-3 text-5xl font-underline">ENTER FULL FILEPATH HERE!</h1>
              <div className="flex-col items-center hero max-h-screen justify-center items-start">
            <div className="flex hero-content text-center text-neutral-content max-w-w mt-2">

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
            <h2 className='mt-10'>{msg && msg}</h2>
            </div>
            </div>
            </div>
        </div>    
    </> 
  );
}
export default Home;