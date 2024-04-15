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








// "use client";
// import React, { useState } from "react";
// import { MouseEvent } from "react";
// import axios from "axios";
// import Link from "next/link";

// const FileUpload = () => {
//   const [guideFile, setGuideFile] = useState(null); 
//   const [tripPrefFiles, setTripPrefFiles] = useState([]);
//   const [uploaded, setUploaded] = useState(false);


//   const handleFileChange = (event: any, fileType: string) => { //stores uploaded files
//     const uploadedFiles = event.target.files;
//     if (fileType === "guide") {
//       let guideFile = null;
//       for (let i = 0; i < uploadedFiles.length; i++) {
//         const file = uploadedFiles[i];
//         if (file.name === "guide_file.xlsx") { 
//           guideFile = file;
//           break; // Exit the loop once guide file is found
//         }
//       }
//       if (guideFile) {
//         setGuideFile(guideFile);
//       } else {
//         console.error("Guide file not found in uploaded files");
//       }
//     } else if (fileType === "tripPref") {
//       setTripPrefFiles(Array.from(uploadedFiles));
//     }
//   };

//   const handleUpload = async (guideFile: any, tripPrefFiles: any[]) => {
//     try {
//       const formData = new FormData();
      
//       //append guide file
//       formData.append("guide_file", guideFile);
  
//       //append multiple trip preference files with unique keys
//       tripPrefFiles.forEach((file, index) => {
//         formData.append(`trip_pref_file_[${index}]`, file);
//       });
  
//       //make POST request to upload files
//       const response = await axios.post("http://localhost:5000/upload", formData);
      
//       //check for error
//       console.log(response.data);
      
//       //set uploaded state to true upon successful upload
//       setUploaded(true);
//     } catch (error) {
//       console.error("Error uploading files:", error);
//     }
//   };

//   return (
//         <>
//         <div className="hero min-h-screen" style={{backgroundImage: 'url(/mountainLandscape.jpg)'}}>
//             <div className="hero-overlay bg-opacity-60"></div>
//                 <div className="flex-col items-center hero min-h-screen justify-center items-start">
//                     <div className="flex hero-content text-center text-neutral-content max-w-w mt-10">
//                         <div className="mb-5">
//                 <h1 className="mb-10 text-7xl font-bold">Upload Files Here!</h1>
//                 <div className="mb-20">
//                 <button className="btn btn-sm">
//                     <li><Link href="/">Home</Link></li>
//                 </button>
//                 <div className="mt-5 flex justify-center">
//                     <label className="flex items-center justify-center form-control max-w-xs">
//                         <div className="label justify-center">
//                             <span className="label-text font-bold">Trip Prefrences</span>
//                         </div>
//                         <form method="post" action="http://localhost:5000/upload" encType="multipart/form-data">
//                           <div>
//                             <input type="file" className="file-input file-input-bordered max-w-xs"
//                               multiple accept=".xlsx" onChange={(e) => handleFileChange(e, "tripPref")}/>
//                           </div>
//                         </form>
//                     </label>
//                   </div>
//                 </div>
//                 <div className="mb-20">
//                 <div className="flex justify-center">
//                 <label className="flex items-center justify-center form-control max-w-xs">
//                         <div className="label justify-center">
//                             <span className="label-text font-bold">Lead/Assistant Guide Status</span>
//                         </div>
//                         <form method="post" action="http://localhost:5000/upload" encType="multipart/form-data">
//                           <div>
//                             <input type="file" className="file-input file-input-bordered max-w-xs"
//                               multiple accept=".xlsx" onChange={(e) => handleFileChange(e, "guide")}/>
//                           </div>
//                         </form>
//                     </label>
//                 </div>
//                 </div>
//                     {uploaded && <p className="text-green-500">File uploaded successfully!</p>}
//                     <button className="btn btn-outline btn-default mb-10" onClick={(e) => handleUpload(guideFile, tripPrefFiles)}>Upload Files</button>
//                 </div>
//             </div>
//         </div>
//     </div>
//     </>
//     )
// }


// export default FileUpload;