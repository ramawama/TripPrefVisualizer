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
      {uploaded &&
      <>
        <a className="btn btn-ghost text-xl"  href="/displaydata"> display data</a>
        <a className="btn btn-ghost text-xl"  href="/schedules"> schedules </a> 
        </>}
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
            </div>
            </div>

            <div className='mt-20 justify-center'>
            <h2>{msg && msg}</h2>
            </div>
            </div>
        </div>    
    </> 
  );
}
export default Home;



// "use client";

// import { useState, useEffect } from 'react';
// import Menu from './menu';

// export default function Home() {
//   const [typingText, setTypingText] = useState('');
//   const fullText = "  Welcome to the future...";
//   const typingSpeed = 100; // milliseconds

//   useEffect(() => {
//     let index = 0; 
//     // Slight delay before starting typing effect
//     const startDelay = setTimeout(() => {
//       const timer = setInterval(() => {
//         setTypingText((prev) => prev + fullText.charAt(index));
//         index++;
//         if (index === fullText.length) clearInterval(timer);
//       }, typingSpeed);
//       return () => clearInterval(timer); // Ensure this cleanup runs when the effect re-runs or component unmounts
//     }, 100); // Short delay before typing starts
  
//     return () => clearTimeout(startDelay); // Cleanup the delay as well
//   }, [fullText]);

//   return (
//     <div className="hero min-h-screen" style={{backgroundImage: 'url(/mountainLandscape.jpg)'}}>
//       <div className="hero-overlay bg-opacity-60"></div>
//       <div className="flex hero min-h-screen justify-center items-start">
//         <div className="flex hero-content text-center text-neutral-content max-w-w mt-10">
//           <div className="mb-5">
//           <h1 className="mb-10 text-7xl font-bold">WELCOME</h1>
//           <p className="flex justify-center mb-10 text-center text-2xl">{typingText}</p>
//           <div> 
//             <Menu></Menu>
//           </div>
//           </div>
//         </div>
//       </div>
//     </div>
//   );
// }

