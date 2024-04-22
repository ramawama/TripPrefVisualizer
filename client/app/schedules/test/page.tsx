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
  const [tripName, setTripName] = useState('');
  const [startDateYear, setStartDateYear] = useState('');
  const [startDateMonth, setStartDateMonth] = useState('');
  const [startDateDay, setStartDateDay] = useState('');

  const [endDateYear, setEndDateYear] = useState('');
  const [endDateMonth, setEndDateMonth] = useState('');
  const [endDateDay, setEndDateDay] = useState('');




  const [showInvalidNumberAlert, setShowInvalidNumberInput] = useState(false);

  const fetchData = async () => {
    try {
      setLoading(true); // Set loading to true at the beginning of the fetch
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

  function resetDatabase() {
    fetch('http://localhost:5000/reset-database', { // Adjust the URL based on your Flask server address and port
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        alert('Database has been reset successfully!');
      } else {
        alert('Failed to reset the database.');
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
  }

  // Initial fetch on component mount
  useEffect(() => {
    fetchData();
  }, []);

  const populateTablesWithNewData = () => {
    fetchData();
  };

  const validateNumInput = (setFieldValue) => (e) => {
    const value = e.target.value;
    const semesterValue = parseInt(value, 10);
    
    if (value == '' || (!Number.isNaN(semesterValue) && (semesterValue >= 0 && semesterValue < 20))) {
      setShowInvalidNumberInput(false); // Hide error message if input is valid
    } else {
      setShowInvalidNumberInput(true); // Show error message
      setFieldValue(''); // Resets the input if out of bounds
    }
  };

  const validateYear = (setFieldValue) => (e) => {
    const value = e.target.value;
    const monthValue = parseInt(value, 10);
    
    if (value == '' || (!Number.isNaN(monthValue) && (monthValue >= 2000 && monthValue < 2100))) {
      setShowInvalidNumberInput(false); // Hide error message if input is valid
    } else {
      setShowInvalidNumberInput(true); // Show error message
      setFieldValue(''); // Resets the input if out of bounds
    }
  };

  const validateMonth = (setFieldValue) => (e) => {
    const value = e.target.value;
    const monthValue = parseInt(value, 10);
    
    if (value == '' || (!Number.isNaN(monthValue) && (monthValue >= 0 && monthValue < 13))) {
      setShowInvalidNumberInput(false); // Hide error message if input is valid
    } else {
      setShowInvalidNumberInput(true); // Show error message
      setFieldValue(''); // Resets the input if out of bounds
    }
  };

  const validateDay = (setFieldValue) => (e) => {
    const value = e.target.value;
    const monthValue = parseInt(value, 10);
    
    if (value == '' || (!Number.isNaN(monthValue) && (monthValue >= 0 && monthValue < 32))) {
      setShowInvalidNumberInput(false); // Hide error message if input is valid
    } else {
      setShowInvalidNumberInput(true); // Show error message
      setFieldValue(''); // Resets the input if out of bounds
    }
  };

  const validateTripName = (setFieldValue) => (e) => {
    const value = e.target.value;    
    if (value == '' || value.length < 50 && /^[a-zA-Z ]+$/.test(value)) {
      // 1. The input is an empty string, OR
      // 2. The string is shorter than 20 characters and contains only letters.
      setShowInvalidNumberInput(false); // Hide error message if input is valid
    } else {
      setShowInvalidNumberInput(true); // Show error message
      setFieldValue(''); // Resets the input if out of bounds
    }
  };


  const sendDataToBackend = () => {
    let dataToSend = {};
    const selects = document.querySelectorAll('select');
    selects.forEach(select => {
      // Assuming you want to use the ID as the key
      if (select.id) dataToSend[select.id] = select.value;
    });
    const textInputs = document.querySelectorAll('input[type="text"]');
    textInputs.forEach((input: HTMLInputElement) => {
      // Using placeholder as key; ensure placeholders are unique or consider a different attribute
      if (input.placeholder) dataToSend[input.placeholder] = input.value;
    });
    fetch('http://localhost:5000/api/modifyLeader', { // Update port if your Flask app runs on a different one
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(dataToSend),
    })
    .then(response => response.json())
    .then(data => alert(JSON.stringify(data)))
    .catch(error => console.error('Error:', error));
  };


  if (isLoading) return <p>Loading...</p>;

  return (
      
      <div>
        <div className="mt-5 text-center">
        <button className="btn btn-sm btn-outline btn-secondary">
          <li><Link href="/">Home</Link></li>
        </button>
      </div>

      {/* Start of the "Edit trip leader" join section */}
      <details className="collapse bg-base-200">
    <summary className="collapse-title text-l font-medium">Click to Edit Rows</summary>
    <div className="collapse-content"> 
    <div className="flex justify-center">
  <div style={{ fontSize: '15px' }}> 
    Leave fields blank if you do not want to change their value :)
  </div>
</div>
      <div className="join justify-start items-center space-x-2 p-6">
      <span className="font-semibold" style={{whiteSpace: 'nowrap'}}>Edit Trip Leader:</span>
      <select id="tripLeaderSelect" className="select select-bordered text-xs">
        <option disabled selected>Trip Leader Name</option>
        {tripLeaderData.map(trip_leader => (
          <option key={trip_leader.id} value={trip_leader.id} className="p-2 text-sm leading-6">
            {trip_leader.name}
          </option>
        ))}
      </select>
      <input type="text" placeholder="Class year" className="input input-bordered input-sm w-1/6 max-w-xs" value={classYear} onBlur={validateYear(setClassYear)}  onChange={(e) => setClassYear(e.target.value)}/>
      <input type="text" placeholder="Semesters Left" className="input input-bordered input-sm w-1/4 max-w-xs" value={semestersLeft} onBlur={validateNumInput(setSemestersLeft)}  onChange={(e) => setSemestersLeft(e.target.value)}/>
      <input type="text" placeholder="Number of Trips Assigned" className="input input-bordered input-sm w-2/5 max-w-xs" value={numTripsAssigned} onBlur={validateNumInput(setNumTripsAssigned)}  onChange={(e) => setNumTripsAssigned(e.target.value)}/>
      <select id="coLead1" className="select select-bordered text-xs">
      <option disabled selected>1st Preferred Co-Lead</option>
        {tripLeaderData.map(trip_leader => (
          <option key={trip_leader.id} value={trip_leader.id} className="p-2 text-sm leading-6">
            {trip_leader.name}
          </option>
        ))}
      </select>
      <select id="coLead2" className="select select-bordered text-xs">
      <option disabled selected>2nd Preferred Co-Lead</option>
        {tripLeaderData.map(trip_leader => (
          <option key={trip_leader.id} value={trip_leader.id} className="p-2 text-sm leading-6">
            {trip_leader.name}
          </option>
        ))}
      </select>
      <select id="coLead3" className="select select-bordered text-xs">
      <option disabled selected>3rd Preferred Co-Lead</option>
        {tripLeaderData.map(trip_leader => (
          <option key={trip_leader.id} value={trip_leader.id} className="p-2 text-sm leading-6">
            {trip_leader.name}
          </option>
        ))}
      </select>
      </div>

      <div className="join justify-start space-x-2 pl-40">
      <select id="bikingLeaderStatus" className="select select-bordered text-xs w-1/3">
        <option disabled selected>Biking Status</option>
        <option>Lead Guide</option>
        <option>Interested in Promotion</option>
        <option>Not Interested in Promotion</option>
      </select>
      <select id="overnightLeaderStatus" className="select select-bordered text-xs w-1/3">
        <option disabled selected>Overnight Status</option>
        <option>Lead Guide</option>
        <option>Interested in Promotion</option>
        <option>Not Interested in Promotion</option>
      </select>
      <select id="seaKayakingLeaderStatus" className="select select-bordered text-xs w-1/3">
        <option disabled selected>Sea Kayaking Status</option>
        <option>Lead Guide</option>
        <option>Interested in Promotion</option>
        <option>Not Interested in Promotion</option>
      </select>
      <select id="spelunkingLeaderStatus" className="select select-bordered text-xs w-1/3">
        <option disabled selected>Spelunking Status</option>
        <option>Lead Guide</option>
        <option>Interested in Promotion</option>
        <option>Not Interested in Promotion</option>
      </select>
      <select id="surfingLeaderStatus" className="select select-bordered text-xs w-1/3">
        <option disabled selected>Surfing Status</option>
        <option>Lead Guide</option>
        <option>Interested in Promotion</option>
        <option>Not Interested in Promotion</option>
      </select>
      <select id="watersportsLeaderStatus" className="select select-bordered text-xs w-1/3">
        <option disabled selected>Watersports Status</option>
        <option>Lead Guide</option>
        <option>Interested in Promotion</option>
        <option>Not Interested in Promotion</option>
      </select>
      </div>
      {/* End of the "Edit trip leader" join section */}
      
      {/* Start of the "Edit trip" join section */}
      <div className="join justify-start items-center space-x-2 p-20 py-10">
      <span className="font-semibold" style={{whiteSpace: 'nowrap'}}>Edit Trip:</span>
      <select id="tripSelect" className="select select-bordered text-xs">
        <option disabled selected>Trip ID</option>
        {tripData.map(trip => (
          <option key={trip.trip_id} value={trip.trip_id} className="p-2 text-sm leading-6">
            {trip.trip_id}
          </option>
        ))}
      </select>
      <input type="text" placeholder="Trip Name" className="input input-bordered input-sm w-1/2 max-w-xs" value={tripName} onBlur={validateTripName(setTripName)} onChange={(e) => setTripName(e.target.value)}/>
      <select id="categorySelect" className="select select-bordered text-xs">
        <option disabled selected>Trip Category</option>
        <option>Surfing</option>
        <option>Sea Kayaking</option>
        <option>Biking</option>
        <option>Watersports</option>
        <option>Spelunking</option>
        <option>Overnight</option>
      </select>
      <input type="text" placeholder="Start Date Year" className="input input-bordered input-sm w-1/4 max-w-xs" value={startDateYear} onBlur={validateYear(setStartDateYear)}  onChange={(e) => setStartDateYear(e.target.value)}/>
      <span className="font-semibold" style={{whiteSpace: 'nowrap'}}>/</span>
      <input type="text" placeholder="Start Month" className="input input-bordered input-sm w-1/5 max-w-xs" value={startDateMonth} onBlur={validateNumInput(setStartDateMonth)}  onChange={(e) => setStartDateMonth(e.target.value)}/>
      <span className="font-semibold" style={{whiteSpace: 'nowrap'}}>/</span>
      <input type="text" placeholder="Start Day" className="input input-bordered input-sm w-1/5 max-w-xs" value={startDateDay} onBlur={validateDay(setStartDateDay)}  onChange={(e) => setStartDateDay(e.target.value)}/>
      <span className="font-semibold" style={{whiteSpace: 'nowrap'}}>--></span>
      <input type="text" placeholder="End Date Year" className="input input-bordered input-sm w-1/4 max-w-xs" value={endDateYear} onBlur={validateYear(setEndDateYear)}  onChange={(e) => setEndDateYear(e.target.value)}/>
      <span className="font-semibold" style={{whiteSpace: 'nowrap'}}>/</span>
      <input type="text" placeholder="End Month" className="input input-bordered input-sm w-1/5 max-w-xs" value={endDateMonth} onBlur={validateNumInput(setEndDateMonth)}  onChange={(e) => setEndDateMonth(e.target.value)}/>
      <span className="font-semibold" style={{whiteSpace: 'nowrap'}}>/</span>
      <input type="text" placeholder="End Day" className="input input-bordered input-sm w-1/5 max-w-xs" value={endDateDay} onBlur={validateDay(setEndDateDay)}  onChange={(e) => setEndDateDay(e.target.value)}/>
      </div>
      <div className="join justify-start space-x-2 pl-40">
      <select id="leadGuidesNeeded" className="select select-bordered text-xs">
        <option disabled selected># of Lead Guides</option>
        <option>0</option>
        <option>1</option>
        <option>2</option>
        <option>3</option>
        <option>4</option>
      </select>
      <select id="totalGuidesNeeded" className="select select-bordered text-xs">
        <option disabled selected># of Total Guides</option>
        <option>0</option>
        <option>1</option>
        <option>2</option>
        <option>3</option>
        <option>4</option>
      </select>
      </div>
      <div className="flex justify-center pt-4">
      <button className="btn btn-primary  " onClick={() => {
    sendDataToBackend();
    populateTablesWithNewData();
  }}>Submit Trip Changes</button>
      </div>
      </div>
    </details>
      {/* End of the "Edit trip" join section */}
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
      <div className="flex justify-center pt-4">
      <button className="btn btn-secondary  " onClick={() => {
    resetDatabase();
    populateTablesWithNewData();
  }}>Delete All Data</button>
      </div>
      
      {/* Footer section where the alert will be conditionally displayed */}
      <div className="min-h-screen flex flex-col justify-between">
  <footer style={{ position: 'fixed', bottom: 0, width: '100%', textAlign: 'center' }}>
    {showInvalidNumberAlert && (
      <div role="alert" className="alert alert-error mt-2">
        <svg xmlns="http://www.w3.org/2000/svg" className="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
        <span>Please enter a valid input</span>
      </div>
    )}
  </footer>
</div>

    </div>
  
  );
};



export default App;