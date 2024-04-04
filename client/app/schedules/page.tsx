"use client";
import React from "react";
import { MouseEvent } from "react";
import { useState } from "react";
import Link from "next/link";

const Schedules = () =>{

  function masterSchedule(){
    console.log("master");
  }

    return (    
        <>
        <div className="navbar bg-base-100">
        <a className="btn btn-ghost text-xl"  href="/home"> home </a>
        <a className="btn btn-ghost text-xl"  href="/displaydata"> display data</a>
        <a className="btn-clicked btn-ghost text-xl"  href="/schedules"> schedules </a>
        <a className="btn btn-ghost text-xl"  href="/about"> about </a>
        </div>
        <div className="hero min-h-screen" style={{backgroundImage: 'url(/clouds.jpg)'}}>
            <div className="hero-overlay bg-opacity-60"></div>   
              <div className="hero-content text-center text-neutral-content">
              <div className="max-w-md">
                <h1 className="mb-5-sch text-5xl font-bold">S C H E D U L E S</h1>
                  <a className="btn btn-active btn-primary" onClick={masterSchedule}>MASTER SCHEDULE</a>
                  <br />
                  <a className="btn btn-active btn-primary" >trip leader <br />preference schedule</a>
                  <br />
                  <a className="btn btn-active btn-primary">assistant guide  <br />  promotion schedule</a>
              </div>

            </div>
          </div>
        </> 
      );
}


   

export default Schedules;