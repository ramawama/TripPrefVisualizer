// import React from "react";
// import { useState } from "react";

// function MultipleFileUpload() {
//     const [files, setFile]= useState()

//     const handleChange = (event: any) => {
//         setFile(event.target.files);
//     }

//     function handleUpload() {
//         const formData = new FormData();
//         for (let i = 0; i < files.length; i++){
//             formData.append(`trip_pref_file_[${i}]`, files[0])
//         }

//         fetch('http://localhost:5000/post', {
//             method: 'POST',
//             body: formData
//         }).then(res => res.json()). 
//         then(data=> console.log(data)).
//         catch(err => console.log(err));
//     }

//     return (
//         <div>
//             <input type="file" accept=".xlsx" 
//             className="file-input file-input-bordered max-w-xs"
//             multiple onChange={handleChange}/>
//             <button onClick={handleUpload}>Upload</button>
//         </div>
//     )
// }

// export default MultipleFileUpload

