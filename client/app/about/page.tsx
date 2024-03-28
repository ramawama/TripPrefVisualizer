"use client";
import React from "react";
import { MouseEvent } from "react";
import { useState } from "react";
import Link from "next/link";

function aboutUs() {
    return (
        <>
        <div className="navbar bg-base-100">
        <a className="btn btn-ghost text-xl"  href="/home"> home </a>
        <a className="btn btn-ghost text-xl"  href="/displaydata"> display data</a>
        <a className="btn btn-ghost text-xl"  href="/schedules"> schedules </a>
        <a className="btn-clicked btn-ghost text-xl"  href="/about"> about </a>
        </div>
        <div className="hero-content text-center text-neutral-content">
              <div className="max-w-md">
                <h1 className="mb-5 text-5xl font-bold"> ABOUT</h1>
              </div>
            </div>
        <div className="hero min-h-screen" style={{backgroundImage: 'url(/clouds.jpg)'}}>
            <div className="hero-overlay bg-opacity-60"></div>
                
              <div className="hero-content text-neutral-content">
              <div className="max-w-md">
                <img className="headshots" src="/aaron.jpg" alt="Aaron Schumer" ></img><br />
                <h2 className="names"> AARON SCHUMER </h2>
                <br /><p> bio </p>
                <img className="headshots" src="/rama.jpg" alt="Rama Janco" ></img><br />
                <h2 className="names"> RAMA JANCO </h2>
                <br /><p> bio </p>
                <img className="headshots" src="/tiger.jpg" alt="Tiger Cao" ></img><br />
                <h2 className="names"> TIGER CAO </h2>
                <br /><p> bio </p>
                <img className="headshots" src="/lauren.jpg" alt="Lauren Dulick" ></img><br />
                <h2 className="names"> LAUREN DULICK </h2>
                <br /><p> bio </p>
                <img className="headshots" src="/anna.jpg" alt="Anna Priore" ></img><br />
                <h2 className="names"> ANNA PRIORE </h2>
                <br /><p> Anna Priore is a first year Digital Arts and Sciences Major at the University of Florida. In addition to Real World Engineering, her other involvements include being a member of the Gator User Design Club (GUD) and a designer on GUD's First Year Design Team. She enjoys making art and practicing photography in her spare time. </p>
                <img className="headshots" src="/aline.jpg" alt="Alina Garib" ></img> <br />
                <h2 className="names"> ALINA GARIB </h2>
                <br /><p> bio </p>





              </div>
            </div>
          </div>
        
        </> 
    );
}

export default aboutUs;