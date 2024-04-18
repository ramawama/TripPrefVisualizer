//WELCOME PAGE

"use client";

import { useState, useEffect } from 'react';
import { MouseEvent } from "react";
import axios from "axios";
import Link from "next/link";



function Home() {
  const [typingText, setTypingText] = useState('');
  const fullText = "  we're so excited to have you.";
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

  const [guideFile, setGuideFile] = useState(null); 
  const [tripPrefFiles, setTripPrefFiles] = useState([]);
  const [uploaded, setUploaded] = useState(false);


  const handleFileChange = (event: any, fileType: string) => { //stores uploaded files
    const uploadedFiles = event.target.files;
    setUploaded(true);
    if (fileType === "guide") {
      setGuideFile(uploadedFiles[0]);
    } else if (fileType === "tripPref") {
      setTripPrefFiles(Array.from(uploadedFiles));
    }
  };

  const handleUpload = async (guideFile: any, tripPrefFiles: any[]) => {
    try {
      const formData = new FormData();
      
      //append guide file
      formData.append("guide_file", guideFile);
  
      //append multiple trip preference files with unique keys
      tripPrefFiles.forEach((file, index) => {
        formData.append(`trip_pref_file_[${index}]`, file);
      });
  
      //make POST request to upload files
      const response = await axios.post("http://localhost:5000/upload", formData);
      
      //check for error
      console.log(response.data);
      
      //set uploaded state to true upon successful upload
      setUploaded(true);
    } catch (error) {
      console.error("Error uploading files:", error);
    }
  }
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

    
    <div className="hero min-h-screen" style={{backgroundImage: 'url(/clouds.jpg)'}}>
        <div className="hero-overlay bg-opacity-60"></div>
          <div className="hero-content text-center text-neutral-content">
            <div className="max-w-md">
              <br /><br />
              <h1 className="mb-5 text-7xl font-bold">WELCOME CORE TRIP LEADERS</h1>
              <p className="mb-5 text-2xl">{typingText}</p>
              <br /><br />
              <h1 className="mb-5 text-5xl font-bold">UPLOAD FILES HERE!</h1>
          <div className="mb-20">
            <div className="mt-5 flex justify-center">
              <label className="flex items-center justify-center form-control max-w-xs">
                  <div className="label">
                    <span className="label-text font-bold">Trip Prefrences</span>
                  </div>
                  <input type="file" className="file-input file-input-bordered max-w-xs" accept=".xlsx" onChange={(e) => handleFileChange(e, "tripPref")} multiple/>
              </label>
            </div>
            {uploaded && <p className="text-green-500">File uploaded successfully!</p>}
          </div>
          <div className="mb-20">
            <div className="flex justify-center">
              <label className="flex justify-center form-control max-w-xs">
                <div className="label flex justify-center">
                  <span className="label-text font-bold">Lead/Assistant Guide Status</span>
                </div>
                <input type="file" className="file-input file-input-bordered max-w-xs" accept=".xlsx" onChange={(e) => handleFileChange(e, "guide")} />
              </label>
            </div>
          </div>
          {uploaded && <p className="text-green-500">File uploaded successfully!</p>}
          </div>
        </div>
    </div>    
    </> 
  );
}
export default Home;