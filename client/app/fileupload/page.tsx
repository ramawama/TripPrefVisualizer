import React from "react";
import Link from "next/link";

const FileUpload = () =>{
    return (
        <>
        <div className="hero min-h-screen" style={{backgroundImage: 'url(/mountainLandscape.jpg)'}}>
            <div className="hero-overlay bg-opacity-60"></div>
                <div className="flex hero min-h-screen justify-center items-start">
                    <div className="flex hero-content text-center text-neutral-content max-w-w mt-10">
                        <div className="mb-5">
                <h1 className="mb-10 text-7xl font-bold">Upload Files Here!</h1>
                <div className="mb-20">
                <button className="btn btn-sm">
                    <li><Link href="/">Home</Link></li>
                </button>
                    <label className="flex justify-center form-control max-w-xs">
                        <div className="label justify-center">
                            <span className="label-text font-bold">Trip Prefrences</span>
                        </div>
                        <input type="file" className="file-input file-input-bordered max-w-xs" />
                    </label>
                </div>
                <div className="mb-20">
                <label className="flex justify-center form-control max-w-xs">
                    <div className="label justify-center">
                        <span className="label-text font-bold">Lead/Assistant Guide Status</span>
                    </div>
                    <input type="file" className="file-input file-input-bordered max-w-xs" />
                </label>
                </div>
                </div>
            </div>
        </div>
    </div>
    </>
    )
}

export default FileUpload;