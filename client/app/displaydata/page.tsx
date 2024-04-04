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
        <div className="hero min-h-screen" style={{backgroundImage: 'url(/clouds.jpg)'}}>
          <div className="hero-overlay bg-opacity-60"></div>
           <h1 className="mb-5 text-5xl font-bold" /* GET THIS AT THE TOP */>  D I S P L A Y  D A T A</h1> 
          <label className="form-control w-full max-w-xs">
            <div className="label">
            <div className="flex justify-start">
              <span className="label-text">sort by</span>
            </div>
            <select className="select select-bordered">
              <option></option>
              <option>Trip Leader ID</option>
              <option>Trip Type</option>
              <option>Date</option>
            </select>
            </div>
          </label>
          </div>
        </> 
      );
}

export default displayData;