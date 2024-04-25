"use client";
import React from "react";
import { MouseEvent } from "react";
import { useState } from "react";
import Link from "next/link";

function aboutUs() {
    return (
        <>
        <div className="navbar bg-base-100">
        <a className="btn btn-ghost text-xl"  href="/"> home </a>
        <a className="btn btn-ghost text-xl"  href="/displaydata"> display data</a>
        <a className="btn btn-ghost text-xl"  href="/schedules"> schedules </a>
        <a className="btn-clicked btn-ghost text-xl"  href="/about"> about </a>
        </div>
        <div className="hero min-h-screen" style={{backgroundImage: 'url(/clouds2.png)'}}>
            <div className="hero-overlay bg-opacity-60"></div> 
            <div className="hero-content text-center text-neutral-content">
              <div className="max-w-md justify-start">
              <h1 className="mb-5 text-5xl font-bold">A B O U T</h1>
                <img className="headshots rounded-full" src="/aaron5.jpg" alt="Aaron Schumer" ></img><br />
                <h2 className="names font-bold text-2xl"> AARON SCHUMER </h2><br />
                <br /><p className="mb-10"> bio </p>
                <img className="headshots rounded-full" src="/rama2.jpg" alt="Rama Janco" ></img><br />
                <h2 className="names font-bold text-2xl"> RAMA JANCO </h2>
                <br /><p className="mb-10"> bio </p>
                <img className="headshots rounded-full" src="/tiger2.jpg" alt="Tiger Cao" ></img><br />
                <h2 className="names font-bold text-2xl"> TIGER CAO </h2>
                <br /><p className="mb-10"> Tiger Cao is an outstandingly intellegent individual with exceptional computer science 
                experience. He is open to any quant, AI, and senior software development roles. </p>
                <img className="headshots rounded-full" src="/lauren2.jpg" alt="Lauren Dulick" ></img><br />
                <h2 className="names font-bold text-2xl"> LAUREN DULICK </h2>
                <br /><p className="mb-10"> Lauren worked on this CORE Trip Preference Visualizer as a second-year computer science
                student in the College of Engineering at the University of Florida. In addition to being a backend developer on this
                project for Real World Engineering, she is also a member of the UF Honors Program, a University Research Scholar, and
                a YoungLife College Leader. Working in an AI-Ethics research lab, her research interests lie in Artificial Intellegence,
                Psychology, and Ethics. </p>
                <img className="headshots rounded-full" src="/anna3.jpg" alt="Anna Priore"></img><br />
                <h2 className="names font-bold text-2xl"> ANNA PRIORE </h2> 
                <br />
                <p className="mb-10"> Anna Priore is a first year Digital Arts and Sciences Major at the University of Florida. 
                    In addition to being a front end developer for this project through Real World Engineering, 
                    her other involvements include being a member of the Gator User Design Club (GUD) and a designer 
                    on GUD's First Year Design Team. She enjoys making art and practicing photography in her spare time. </p>
                <img className="headshots rounded-full" src="/alina3.jpg" alt="Alina Garib" ></img> <br />
                <br></br>
                <h2 className="names font-bold text-2xl"> ALINA GARIB </h2>
                <br /><p className="mb-10">Alina is a dedicated second-year Computer Science major with a minor in Chinese at the University of Florida. 
                    She is skilled in C++ and Python, and worked primarily in the frontend of this project.  
                    Beyond the digital world, Alina is a runner and an active participant in the Florida Run Club. 
                    She values balancing her time spent programming with time outdoors.</p>
              </div>
            </div>
          </div>
        
        </> 
    );
}

export default aboutUs;