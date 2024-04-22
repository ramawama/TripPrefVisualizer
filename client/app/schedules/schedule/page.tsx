"use client";
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Link from 'next/link';


const App = () => {
  const [isLoading, setLoading] = useState(true);
  const [scheduleData, setScheduleData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        // fetch JSON data from your API endpoint
        const response = await axios.get('http://localhost:5000/schedule');
        const data = response.data; 

        // separate data into individual arrays
        const { schedule } = data;

        setScheduleData(schedule);

        setLoading(false);
      } catch (error) {
        console.error('Error fetching data:', error);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (isLoading) return <p>Loading...</p>;

  return (
    <>
    <div className="navbar bg-base-100">
    
      <>
        {/*<a className="btn btn-ghost text-xl"  href="/displaydata"> display data</a>
        <a className="btn btn-ghost text-xl"  href="/schedules"> schedules </a> */}
        </>
        <a className="btn btn-ghost text-xl"  href="/home"> home </a>
        <a className= "btn-clicked btn-ghost text-xl" href="/schedule"> schedules </a>
        <a className="btn btn-ghost text-xl"  href="/about"> about </a>
    </div>
  <div className="flex flex-col  h-screen p-10 w-full max-w-screen-xl mx-auto">
  <div className="hero-overlay bg-opacity-60"> 
  <div className="hero-content text-center text-neutral-content">
              <div className="max-w-md justify-start">
    <h1 className="mb-5 text-5xl font-bold">TRIP SCHEDULE:</h1>
    <div className="overflow-h-96 w-full">
      <table className="table table-xs table-zebra table-pin-rows table-pin-cols w-full">
        <thead>
          <tr>
            <th className="p-5">Trip ID</th>
            <th className="p-5">Lead Guides</th>
            <th className="p-5">Assistant Guides</th>
          </tr>
        </thead>
        <tbody>
          {scheduleData.map(schedule => (
            <tr key={schedule.trip_id}>
              <td className="p-2">{schedule.trip_id}</td>
              <td className="p-2">{schedule.lead_guides}</td>
              <td className="p-2">{schedule.assistant_guides}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
    </div>
  </div>
  </div>
  </div>
  
  </>
);
};

export default App;