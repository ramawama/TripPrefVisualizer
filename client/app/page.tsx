"use client";

import { useState, useEffect } from 'react';
import Menu from './menu';

export default function Home() {
  const [typingText, setTypingText] = useState('');
  const fullText = "  Welcome to the future...";
  const typingSpeed = 100; // milliseconds

  useEffect(() => {
    let index = 0; 
    // Slight delay before starting typing effect
    const startDelay = setTimeout(() => {
      const timer = setInterval(() => {
        setTypingText((prev) => prev + fullText.charAt(index));
        index++;
        if (index === fullText.length) clearInterval(timer);
      }, typingSpeed);
      return () => clearInterval(timer); // Ensure this cleanup runs when the effect re-runs or component unmounts
    }, 100); // Short delay before typing starts
  
    return () => clearTimeout(startDelay); // Cleanup the delay as well
  }, [fullText]);

  return (
    <div className="hero min-h-screen" style={{backgroundImage: 'url(/mountainLandscape.jpg)'}}>
      <div className="hero-overlay bg-opacity-60"></div>
      <div className="flex hero min-h-screen justify-center items-start">
        <div className="flex hero-content text-center text-neutral-content max-w-w mt-10">
          <div className="mb-5">
          <h1 className="mb-10 text-7xl font-bold">Hello Trip Leaders</h1>
          <p className="flex justify-center mb-10 text-center text-2xl">{typingText}</p>
          <div> 
            <Menu></Menu>
          </div>
          </div>
        </div>
      </div>
    </div>
  );
}

