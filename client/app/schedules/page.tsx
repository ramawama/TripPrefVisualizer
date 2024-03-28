"use client";
import React from "react";
import { MouseEvent } from "react";
import { useState } from "react";
import Link from "next/link";

const Schedules = () =>{
    
    return (
        <>
        <div className="navbar bg-base-100">
        <a className="btn btn-ghost text-xl"  href="/home"> home </a>
        <a className="btn btn-ghost text-xl"  href="/displaydata"> display data</a>
        <a className="btn-clicked btn-ghost text-xl"  href="/schedules"> schedules </a>
        <a className="btn btn-ghost text-xl"  href="/about"> about </a>
        </div>
        <div className="hero-content text-center text-neutral-content">
              <div className="max-w-md">
                <h1 className="mb-5 text-5xl font-bold">SCHEDULES</h1>
    
              </div>
            </div>
        <div className="hero min-h-screen" style={{backgroundImage: 'url(/clouds.jpg)'}}>
            <div className="hero-overlay bg-opacity-60"></div>
                
              <div className="hero-content text-center text-neutral-content">
              <div className="max-w-md">
                <h1 className="mb-5 text-5xl font-bold">SCHEDULES</h1>
                  <button className="btn btn-active">MASTER SCHEDULE</button>
                  <br />
                  <button className="btn btn-active btn-primary">trip leader preference<br />based schedule</button>
                  <br />
                  <button className="btn btn-active btn-primary">assistant guide  <br />  promotion schedule</button>
              </div>
            </div>
          </div>
          <div className="overflow-x-auto">
  
  <table className="table">
    {/* head */}
    <thead>
      <tr>
        <th></th>
        <th>Name</th>
        <th>Job</th>
        <th>Favorite Color</th>
      </tr>
    </thead>
    <tbody>
      {/* row 1 */}
      <tr>
        <th>1</th>
        <td>Cy Ganderton</td>
        <td>Quality Control Specialist</td>
        <td>Blue</td>
      </tr>
      {/* row 2 */}
      <tr className="hover">
        <th>2</th>
        <td>Hart Hagerty</td>
        <td>Desktop Support Technician</td>
        <td>Purple</td>
      </tr>
      {/* row 3 */}
      <tr>
        <th>3</th>
        <td>Brice Swyre</td>
        <td>Tax Accountant</td>
        <td>Red</td>
      </tr>
    </tbody>
  </table>
</div>
        </> 
      );
}


   

export default Schedules;