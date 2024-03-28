"use client";
import React from "react";
import MultipleFileUpload from "./multiple_upload";
import { useState } from "react";
import axios from "axios";

// const FileUpload = () => {
//     return(
//     <div>
//         <MultipleFileUpload></MultipleFileUpload>
//     </div>
//     );
// }

// export default FileUpload

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

        // axios.post('http://httpbin.org/post', fd, {
        //     onUploadProgress: (progressEvent) => { setProgress(prevState => {
        //         return {...prevState, pc: progressEvent.progress*100}
        //     }) },
        //     headers: {
        //         "Loading": "value",
        //     }
        // })
        // .then(res => {
        //     setMsg("upload successful");
        //     console.log(res.data)})
        // .catch(err =>{
        //     setMsg("upload failed");
        //     console.log(err)});

    }

    return (
        <div className="App">
            <h1 text-align="center">Uploading files </h1>

            <input onChange = { (e) =>  { setFiles(e.target.files) } } type="file" multiple/>

            <button onClick = { handleUpload }>Upload</button>

            {/* {progress.started && <progress max="100" value ={progress.pc}></progress> } */}
            <div >
            {msg && <span>{msg}</span> }
            </div>

        </div>
    )
}

export default App