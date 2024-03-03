"use client";

import { useState, useEffect } from 'react';

export default function Home() {
  const [typingText, setTypingText] = useState('');
  const fullText = "  We have been waiting for you. Welcome to the future...";
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
      <div className="hero-content text-center text-neutral-content">
        <div className="max-w-md">
          <h1 className="mb-5 text-7xl font-bold">Hello Trip's PA</h1>
          <p className="mb-5 text-2xl">{typingText}</p>
          <button className="btn btn-outline btn-secondary">Get Started</button>
        </div>
      </div>
    </div>
  );
}
