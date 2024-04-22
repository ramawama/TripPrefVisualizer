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
        <a className="btn btn-ghost text-xl"  href="/schedules/schedule"> schedules </a>
        <a className="btn-clicked btn-ghost text-xl"  href="/about"> about </a>
        </div>
        <div className="hero min-h-screen" style={{backgroundImage: 'url(/clouds.jpg)'}}>
            <div className="hero-overlay bg-opacity-60"></div> 
            <div className="hero-content text-center text-neutral-content">
              <div className="max-w-md justify-center">
              <h1 className="mb-5 text-5xl font-bold">A B O U T</h1>
                <img className="headshot" src="/aaron5.jpg" alt="Aaron Schumer" ></img><br />
                <h2 className="names"> <i>AARON SCHUMER</i> </h2><br />
                <br /><p> bio bio bio bio bio lorem ipisum dolor sit amet bio bio bio bio bio bio lorem ipisum dolor sit amet bio bio bio bio bio bio lorem ipisum dolor sit amet bio bio bio bio bio bio lorem ipisum dolor sit amet bio bio bio bio bio bio lorem ipisum dolor sit amet bio </p>
                <img className="headshot" src="/rama2.jpg" alt="Rama Janco" ></img><br />
                <h2 className="names"> <i>TIGER CAO</i> </h2>
                <br /><p> bio bio bio bio bio lorem ipisum dolor sit amet bio bio bio bio bio bio lorem ipisum dolor sit amet bio bio bio bio bio bio lorem ipisum dolor sit amet bio bio bio bio bio bio lorem ipisum dolor sit amet bio bio bio bio bio bio lorem ipisum dolor sit amet bio </p>
                <img className="headshot" src="/tiger2.jpg" alt="Tiger Cao" ></img><br />
                <h2 className="names"> <i>TIGER CAO</i> </h2>
                <br /><p> bio bio bio bio bio lorem ipisum dolor sit amet bio bio bio bio bio bio lorem ipisum dolor sit amet bio bio bio bio bio bio lorem ipisum dolor sit amet bio bio bio bio bio bio lorem ipisum dolor sit amet bio bio bio bio bio bio lorem ipisum dolor sit amet bio </p>
                <img className="headshot" src="/lauren2.jpg" alt="Lauren Dulick" ></img><br />
                <h2 className="names"> <i>LAUREN DULICK</i> </h2>
                <br /><p> bio bio bio bio bio lorem ipisum dolor sit amet bio bio bio bio bio bio lorem ipisum dolor sit amet bio bio bio bio bio bio lorem ipisum dolor sit amet bio bio bio bio bio bio lorem ipisum dolor sit amet bio bio bio bio bio bio lorem ipisum dolor sit amet bio </p>
                <img className="headshot" src="/anna3.jpg" alt="Anna Priore"></img><br />
                <h2 className="names"> <i> ANNA PRIORE</i> </h2> 
                <br />
                <p> Anna Priore is a first year Digital Arts and Sciences Major at the University of Florida. In addition to being a front end developer for this project through Real World Engineering, her other involvements include being a member of the Gator User Design Club (GUD) and a designer on GUD's First Year Design Team. She enjoys making art and practicing photography in her spare time. </p>
                <img className="headshot" src="/alina3.jpg" alt="Alina Garib" ></img> <br />
                <h2 className="names"> <i>ALINA GARIB </i></h2>
                <br /><p> bio bio bio bio bio lorem ipisum dolor sit amet bio bio bio bio bio bio lorem ipisum dolor sit amet bio bio bio bio bio bio lorem ipisum dolor sit amet bio bio bio bio bio bio lorem ipisum dolor sit amet bio bio bio bio bio bio lorem ipisum dolor sit amet bio </p>
              </div>
            </div>
          </div>
        
        </> 
    );
}

export default aboutUs;