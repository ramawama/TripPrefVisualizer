"use client";
import React from "react";
import { MouseEvent } from "react";
import { useState } from "react";
import Link from "next/link";

function displayData() {

    return (
        <>
        <div className="navbar bg-base-100">
        <a className="btn btn-ghost text-xl"  href="/home"> home </a>
        <a className="btn-clicked btn-ghost text-xl"  href="/displaydata"> display data</a>
        <a className="btn btn-ghost text-xl"  href="/schedules"> schedules </a>
        <a className="btn btn-ghost text-xl"  href="/about"> about </a>
        </div>
        <div className="hero-content text-center text-neutral-content">
              <div className="max-w-md">
                <h1 className="mb-5 text-5xl font-bold"> DISPLAY DATA</h1>
    
              </div>
            </div>
        <div className="hero min-h-screen" style={{backgroundImage: 'url(/clouds.jpg)'}}>
            <div className="hero-overlay bg-opacity-60"></div>
                
          </div>

          <label className="form-control w-full max-w-xs">
  <div className="label">
    <span className="label-text">sort by</span>
  </div>
  <select className="select select-bordered">
    <option></option>
    <option>Harry Potter</option>
    <option>Lord of the Rings</option>
    <option>Planet of the Apes</option>
    <option>Star Trek</option>
  </select>
</label>
        
        </> 
      );

}

export default displayData;