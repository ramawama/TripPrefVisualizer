"use client";
import React, { useState } from "react";
import { MouseEvent } from "react";
import axios from "axios";
import Link from "next/link";

const FileUpload = () => {
  const [guideFile, setGuideFile] = useState(null); 
  const [tripPrefFiles, setTripPrefFiles] = useState([]);
  const [uploaded, setUploaded] = useState(false);


  const handleFileChange = (event: any, fileType: string) => { //stores uploaded files
    const uploadedFiles = event.target.files;
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
        formData.append(`trip_pref_file_${index}`, file);
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
  };

  return (
        <>
        <div className="hero min-h-screen" style={{backgroundImage: 'url(/mountainLandscape.jpg)'}}>
            <div className="hero-overlay bg-opacity-60"></div>
                <div className="flex-col items-center hero min-h-screen justify-center items-start">
                    <div className="flex hero-content text-center text-neutral-content max-w-w mt-10">
                        <div className="mb-5">
                <h1 className="mb-10 text-7xl font-bold">Upload Files Here!</h1>
                <div className="mb-20">
                <button className="btn btn-sm">
                    <li><Link href="/">Home</Link></li>
                </button>
                <div className="mt-5 flex justify-center">
                    <label className="flex items-center justify-center form-control max-w-xs">
                        <div className="label justify-center">
                            <span className="label-text font-bold">Trip Prefrences</span>
                        </div>
                        <input type="file" className="file-input file-input-bordered max-w-xs" accept=".xlsx .csv" onChange={(e) => handleFileChange(e, "tripPref")} multiple/>
                </label>
                    <button className="btn btn-outline btn-default ml-4 mt-9" onClick={(e) => handleUpload(guideFile, tripPrefFiles)}>Upload File</button>
                </div>
                    {uploaded && <p className="text-green-500">File uploaded successfully!</p>}
                </div>
                <div className="mb-20">
                <div className="flex justify-center">
                <label className="flex justify-center form-control max-w-xs">
                    <div className="label flex justify-center">
                        <span className="label-text font-bold">Lead/Assistant Guide Status</span>
                    </div>
                    <input type="file" className="file-input file-input-bordered max-w-xs" accept=".xlsx .csv" onChange={(e) => handleFileChange(e, "guide")} />
                </label>
                    <button className="btn btn-outline btn-default ml-4 mt-9" onClick={(e) => handleUpload(guideFile, tripPrefFiles)}>Upload File</button>
                </div>
                </div>
                    {uploaded && <p className="text-green-500">File uploaded successfully!</p>}
                </div>
            </div>
        </div>
    </div>
    </>
    )
}


export default FileUpload;