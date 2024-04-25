"use client";

import React, { useEffect, useState } from 'react';

const LeadersTable = () => {
  const [isLoading, setLoading] = useState(true)
  const [msg, setMsg] = useState([])
  const [leadersData, setLeadersData] = useState([])

  useEffect(() => {
    // Fetch data from the Flask API
    fetch('http://localhost:5000/visualizer')
      .then(response => response.json())
      .then(data => {
        console.log(data); // Log data to check if its being fetched
        setMsg(data.Msg); //access the data from the json object, not the msg
        setLeadersData(data.data); //access the data from the json object, not the msg
        setLoading(false);
      });
  }, []);

  if (isLoading) return <p>Loading...</p>
  if (!leadersData) return <p>No profile data</p>

  return (
    <div>
      <h1>{msg}</h1>
      <h1>Leader Preferences</h1>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Status</th>
            <th>Preferred Trip</th>
          </tr>
        </thead>
        <tbody>
          {leadersData.map((leader) => (
            <tr key={leader.id}>
              <td style={{ padding: "10px" }}>{leader.id}</td>
              <td style={{ padding: "10px" }}>{leader.name}</td>
              <td style={{ padding: "10px" }}>{leader.status}</td>
              <td style={{ padding: "10px" }}>{leader.trip}</td>
            </tr>
    ))}
        </tbody>
      </table>
    </div>
  );
};
// Can also create css classes instead of inline styles to add spacing, border, colors, etc.
export default LeadersTable;