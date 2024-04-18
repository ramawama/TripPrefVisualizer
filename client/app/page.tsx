"use client";

import { useState, useEffect } from 'react';
import Menu from './menu';

export default function Home() {

  return (
    <div className="hero min-h-screen" style={{backgroundImage: 'url(/mountainLandscape.jpg)'}}>
      <div className="hero-overlay bg-opacity-60"></div>
      <div className="flex hero min-h-screen justify-center items-start">
        <div className="flex hero-content text-center text-neutral-content max-w-w mt-10">
          <div className="mb-5">
          <h1 className="mb-10 text-7xl font-bold">WELCOME</h1>
          <div> 
            <Menu></Menu>
          </div>
          </div>
        </div>
      </div>
    </div>
  );
}

