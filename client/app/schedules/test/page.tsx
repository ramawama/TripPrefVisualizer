"use client";
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Link from 'next/link';


const App = () => {
  const [isLoading, setLoading] = useState(true);
  const [tripData, setTripData] = useState([]);
  const [tripLeaderData, setTripLeaderData] = useState([]);
  const [tripPreferenceData, setTripPreferenceData] = useState([]);
  const [classYear, setClassYear] = useState('');
  const [semestersLeft, setSemestersLeft] = useState('');
  const [numTripsAssigned, setNumTripsAssigned] = useState('');


  const [showInvalidNumberAlert, setShowInvalidNumberAlert] = useState(false);

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


  const handleClassYearChange = (e) => {
    // Perform the range validation on blur
    const yearValue = parseInt(classYear, 10);
    if (classYear !== '') {
      if (!Number.isInteger(yearValue) || (yearValue < 2024 || yearValue > 2100)) { // Adjusted the year range in the alert to match your comment
        setShowInvalidNumberAlert(true); // Show error message
        setClassYear(''); // Resets the input if out of bounds
      } else {
        setShowInvalidNumberAlert(false); // Hide error message if input is valid
      }
    }
  };

  const validateNumInput = (setFieldValue) => (e) => {
    const value = e.target.value;
    const semesterValue = parseInt(value, 10);
    
    if (value == '' || (!Number.isNaN(semesterValue) && (semesterValue >= 0 && semesterValue < 20))) {
      setShowInvalidNumberAlert(false); // Hide error message if input is valid
    } else {
      setShowInvalidNumberAlert(true); // Show error message
      setFieldValue(''); // Resets the input if out of bounds
    }
  };

  // const handleNumTripsAssigned = (e) => {
  //   const numTripsVal = parseInt(numTripsAssigned, 10);
  
  //   // Check if the input is a number and within the specified range
  //   if (!Number.isNaN(numTripsVal) && (numTripsVal >= 0 && numTripsVal < 100)) {
  //     setShowInvalidNumberAlert(false); // Hide error message if input is valid
  //   } else {
  //     setShowInvalidNumberAlert(true); // Show error message
  //     setSemestersLeft(''); // Resets the input if out of bounds
  //   }
  // };

  if (isLoading) return <p>Loading...</p>;

  return (
      
      <div>
        <div className="mt-5 text-center">
        <button className="btn btn-sm btn-outline btn-secondary">
          <li><Link href="/">Home</Link></li>
        </button>
      </div>

      {/* Start of the "Edit trip leader" join section */}
      <div className="join justify-start items-center space-x-2 p-6">
      <span className="font-semibold" style={{whiteSpace: 'nowrap'}}>Edit Trip Leader:</span>
      <select id="tripLeaderSelect" className="select select-bordered w-full max-w-xs">
      <option disabled selected>Trip Leader Name</option>
        {tripLeaderData.map(trip_leader => (
          <option key={trip_leader.id} value={trip_leader.id} className="p-2 text-sm leading-6">
            {trip_leader.name}
          </option>
        ))}
      </select>
      <input type="text" placeholder="Class year" className="input input-bordered input-sm w-full max-w-xs" value={classYear} onBlur={handleClassYearChange}  onChange={(e) => setClassYear(e.target.value)}/>
      <input type="text" placeholder="Semesters Left" className="input input-bordered input-sm w-full max-w-xs" value={semestersLeft} onBlur={validateNumInput(setSemestersLeft)}  onChange={(e) => setSemestersLeft(e.target.value)}/>
      <input type="text" placeholder="Number of Trips Assigned" className="input input-bordered input-sm w-full max-w-xs" value={numTripsAssigned} onBlur={validateNumInput(setNumTripsAssigned)}  onChange={(e) => setNumTripsAssigned(e.target.value)}/>
      <select id="coLead1" className="select select-bordered w-full max-w-xs">
      <option disabled selected>1st Preferred Co-Lead</option>
        {tripLeaderData.map(trip_leader => (
          <option key={trip_leader.id} value={trip_leader.id} className="p-2 text-sm leading-6">
            {trip_leader.name}
          </option>
        ))}
      </select>
      <select id="coLead2" className="select select-bordered w-full max-w-xs">
      <option disabled selected>2nd Preferred Co-Lead</option>
        {tripLeaderData.map(trip_leader => (
          <option key={trip_leader.id} value={trip_leader.id} className="p-2 text-sm leading-6">
            {trip_leader.name}
          </option>
        ))}
      </select>
      <select id="coLead3" className="select select-bordered w-full max-w-xs">
      <option disabled selected>3rd Preferred Co-Lead</option>
        {tripLeaderData.map(trip_leader => (
          <option key={trip_leader.id} value={trip_leader.id} className="p-2 text-sm leading-6">
            {trip_leader.name}
          </option>
        ))}
      </select>
      </div>

      <div className="join justify-start items-center space-x-2 ">
      <select id="bikingLeaderStatus" className="select select-bordered w-full max-w-xs">
        <option disabled selected>Biking Status</option>
        <option>Lead Guide</option>
        <option>Interested in Promotion</option>
        <option>Not Interested in Promotion</option>
      </select>
      <select id="overnightLeaderStatus" className="select select-bordered w-full max-w-xs">
        <option disabled selected>Overnight Status</option>
        <option>Lead Guide</option>
        <option>Interested in Promotion</option>
        <option>Not Interested in Promotion</option>
      </select>
      <select id="seaKayakingLeaderStatus" className="select select-bordered w-full max-w-xs">
        <option disabled selected>Sea Kayaking Status</option>
        <option>Lead Guide</option>
        <option>Interested in Promotion</option>
        <option>Not Interested in Promotion</option>
      </select>
      <select id="spelunkingLeaderStatus" className="select select-bordered w-full max-w-xs">
        <option disabled selected>Spelunking Status</option>
        <option>Lead Guide</option>
        <option>Interested in Promotion</option>
        <option>Not Interested in Promotion</option>
      </select>
      <select id="surfingLeaderStatus" className="select select-bordered w-full max-w-xs">
        <option disabled selected>Surfing Status</option>
        <option>Lead Guide</option>
        <option>Interested in Promotion</option>
        <option>Not Interested in Promotion</option>
      </select>
      <select id="watersportsLeaderStatus" className="select select-bordered w-full max-w-xs">
        <option disabled selected>Watersports Status</option>
        <option>Lead Guide</option>
        <option>Interested in Promotion</option>
        <option>Not Interested in Promotion</option>
      </select>
      <button className="btn btn-success">Submit Changes</button>
      </div>


      

      
      {/* End of the "Edit trip leader" join section */}
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
      
      {/* Footer section where the alert will be conditionally displayed */}
      <div className="min-h-screen flex flex-col justify-between">
  <footer style={{ position: 'fixed', bottom: 0, width: '100%', textAlign: 'center' }}>
    {showInvalidNumberAlert && (
      <div role="alert" className="alert alert-error mt-2">
        <svg xmlns="http://www.w3.org/2000/svg" className="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
        <span>Please enter a valid number</span>
      </div>
    )}
  </footer>
</div>

    </div>
  
  
  );
};



export default App;