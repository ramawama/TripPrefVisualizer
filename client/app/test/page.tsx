"use client";
import React from "react";
import { useState } from "react";
import axios from "axios";

function App () {

    const [files, setFiles] = useState(null);
    const [progress, setProgress] = useState({started: false, pc: 0});
    const [msg, setMsg] = useState(null);

    function handleUpload() {
        if (!files){
            console.log("no file selected")
            return;
        }

        const fd = new FormData();
        for (let i = 0; i < files.length; i++) {
            fd.append(`files${i+1}`, files[i]);
        }

        setMsg("Uploading...");
        setProgress(prevState => {
            return {...prevState, started: true }
        })

        fetch('http://localhost:5000/post', {
            method: "POST",
            body: fd,
            headers: {
                "Custom-Header": "value",
            }

        })
        .then(res => {
            if(!res.ok){
                throw new Error("Bad Response");
            }
            setMsg("upload successful");
            return res.json();
        })
        .then(data => console.log(data))
        .catch(err =>{
            setMsg("upload failed");
            console.log(err)});

    }

    return (
        <div className="App">
            <h1 text-align="center">Uploading files </h1>

            <input onChange = { (e) =>  { setFiles(e.target.files) } } type="file" multiple/>

            <button onClick = { handleUpload }>Upload</button>
            <div >
            {msg && <span>{msg}</span> }
            </div>

        </div>
    )
}

export default App

// const FileUploadComponent = () => {
//     const [selectedFiles, setSelectedFiles] = useState(null);

//     const handleFileChange = (event) => {
//         setSelectedFiles(event.target.files); // Set selected files
//     };

//     const uploadFiles = async () => {
//         const formData = new FormData();

//         // Append each file to the formData
//         if (selectedFiles) {
//             Array.from(selectedFiles).forEach(file => {
//                 formData.append('files', file);
//             });
//         }

//         try {
//             // Adjust the URL to match your Flask backend URL and port
//             const response = await fetch('http://localhost:5000/upload', {
//                 method: 'POST',
//                 body: formData,
//                 
//             });
//             if (response.ok) {
//                 console.log('Files successfully uploaded');
//                 // Handle success response
//                 const data = await response.text(); 
//                 console.log(data);
//             } else {
//                 // Handle server errors (response code not OK)
//                 console.error('Server error:', response);
//             }
//         } catch (error) {
//             // Handle network errors
//             console.error('Upload failed:', error);
//         }
//     };

//     return (
//         <div>
//             <input type="file" multiple onChange={handleFileChange} />
//             <button onClick={uploadFiles}>Upload Files</button>
//         </div>
//     );
// };

// export default FileUploadComponent;


// function App() {
//   const [files, setFiles] = useState([]);
//   const [uploadedFiles, setUploadedFiles] = useState([]);

//   function handleMultipleChange(event) {
//     setFiles([...event.target.files]);
//   }

//   function handleMultipleSubmit(event) {
//     event.preventDefault();
//     const url = 'http://localhost:5000/upload';
//     const formData = new FormData();

//     files.forEach((file, index) => {
//       formData.append(`file${index}`, file);
//     });

//     const config = {
//       headers: {
//         'content-type': 'multipart/form-data',
//       },
//     };

//     axios.post(url, formData, config)
//       .then((response) => {
//         console.log("success")
//         console.log(response.data);
//         setUploadedFiles(response.data.files);
//       })
//       .catch((error) => {
//         console.error("Error uploading files: ", error);
//       });
//   }

//   useEffect(() => {
//     const fetchData = async () => {
//       try {
//         const response = await axios.get('http://localhost:3000/test'); // Updated URL to fetch files
//         setFiles(response.data.files);
//       } catch (error) {
//         console.error('Error fetching data:', error);
//       }
//     };

//     fetchData();
//   }, []); 

//   return (
//     <div className="App">
//       <h1>React Multiple Excel File Upload</h1>
//       <form onSubmit={handleMultipleSubmit}>
//         <input type="file" multiple accept=".xlsx, .xls" onChange={handleMultipleChange} />
//         <button type="submit">Upload</button>
//       </form>
//       {uploadedFiles.map((file, index) => (
//         <div key={index}>
//           <a href={file.url} target="_blank" rel="noopener noreferrer">File {index + 1}</a>
//         </div>
//       ))}
//       <div className="UploadedFiles">
//         <h2>Uploaded Files:</h2>
//         {files.map((file, index) => (
//           <div key={index}>
//             <a href={file.url} target="_blank" rel="noopener noreferrer">{file.filename}</a>
//           </div>
//         ))}
//       </div>
//     </div>
//   );
// }

// export default App;
