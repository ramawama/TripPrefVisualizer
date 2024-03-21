"use client";
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Link from 'next/link';


const App = () => {
  const [isLoading, setLoading] = useState(true);
  const [tripData, setTripData] = useState([]);
  const [tripLeaderData, setTripLeaderData] = useState([]);
  const [tripPreferenceData, setTripPreferenceData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      try {
        // fetch JSON data from your API endpoint
        const response = await axios.get('http://localhost:5000/get-data');
        const data = response.data; 

        // separate data into individual arrays
        const { trip, trip_leader, trip_preference } = data;
        setTripData(trip);
        setTripLeaderData(trip_leader);
        setTripPreferenceData(trip_preference);

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
      
      <div>
        <div className="mt-5 text-center">
        <button className="btn btn-sm btn-outline btn-secondary">
          <li><Link href="/">Home</Link></li>
        </button>
      </div>
      <div className="mb-10"></div>
      <h1 className="mb-5 text-center font-bold">Trip Table</h1>
      <div className="overflow-x-auto h-96">
      <table className="table table-xs table-zebra table-pin-rows table-pin-cols">
        <thead>
          <tr>
            <th>Trip ID</th>
            <th>Name</th>
            <th>Category</th>
            <th>Start Date</th>
            <th>End Date</th>
            <th>Lead Guides Needed</th>
            <th>Total Guides Needed</th>
          </tr>
        </thead>
        <tbody>
          {tripData.map(trip => (
            <tr key={trip.trip_id}>
              <td style={{ padding: "10px" }}>{trip.trip_id}</td>
              <td style={{ padding: "10px" }}>{trip.name}</td>
              <td style={{ padding: "10px" }}>{trip.category}</td>
              <td style={{ padding: "10px" }}>{trip.start_date}</td>
              <td style={{ padding: "10px" }}>{trip.end_date}</td>
              <td style={{ padding: "10px" }}>{trip.lead_guides_needed}</td>
              <td style={{ padding: "10px" }}>{trip.total_guides_needed}</td>
            </tr>
          ))}
        </tbody>
      </table>
      </div>
      <div className="mb-10"></div>
      <h1 className="mb-5 text-center font-bold">Trip Leader Table</h1>
      <div className="overflow-x-auto h-96">
      <table className="table table-xs table-zebra table-pin-rows table-pin-cols">
      <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Class Year</th>
            <th>Semesters Left</th>
            <th>Num Trips Assigned</th>
            <th>Preferred Co-leaders</th>
            <th>Reliability Score</th>
            <th>Mountain Biking Role</th>
            <th>Overnight Role</th>
            <th>Sea Kayaking Role</th>
            <th>Spelunking Role</th>
            <th>Surfing Role</th>
            <th>Watersports Role</th>
          </tr>
        </thead>
        <tbody>
          {tripLeaderData.map(trip_leader => (
            <tr key={trip_leader.id}>
              <td style={{ padding: "10px" }}>{trip_leader.id}</td>
              <td style={{ padding: "10px" }}>{trip_leader.name}</td>
              <td style={{ padding: "10px" }}>{trip_leader.class_year}</td>
              <td style={{ padding: "10px" }}>{trip_leader.semesters_left}</td>
              <td style={{ padding: "10px" }}>{trip_leader.num_trips_assigned}</td>
              <td style={{ padding: "10px" }}>{trip_leader.preferred_co_leaders}</td>
              <td style={{ padding: "10px" }}>{trip_leader.reliability_score}</td>
              <td style={{ padding: "10px" }}>{trip_leader.mountain_biking_role}</td>
              <td style={{ padding: "10px" }}>{trip_leader.overnight_role}</td>
              <td style={{ padding: "10px" }}>{trip_leader.sea_kayaking_role}</td>
              <td style={{ padding: "10px" }}>{trip_leader.spelunking_role}</td>
              <td style={{ padding: "10px" }}>{trip_leader.surfing_role}</td>
              <td style={{ padding: "10px" }}>{trip_leader.watersports_role}</td>
            </tr>
          ))}
        </tbody>
      </table>
      </div>

      <div className="mb-10"></div>
      <h1 className= "mb-5 font-bold text-center" >Trip Preference Table</h1>
      <div className="overflow-x-auto h-96">
      <table className="table table-xs table-zebra table-pin-rows table-pin-cols">
      <thead>
          <tr>
            <th>Trip Leader ID</th>
            <th>Trip ID</th>
            <th>Preference</th>
          </tr>
        </thead>
        <tbody>
          {tripPreferenceData.map(trip_preference => (
            <tr key={trip_preference.trip_leader_id}>
              <td style={{ padding: "10px" }}>{trip_preference.trip_leader_id}</td>
              <td style={{ padding: "10px" }}>{trip_preference.trip_id}</td>
              <td style={{ padding: "10px" }}>{trip_preference.preference}</td>
            </tr>
          ))}
        </tbody>
      </table>
      </div>
      <div className="mt-10"></div>
    </div>
  );
};

export default App;