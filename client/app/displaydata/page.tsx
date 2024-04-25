"use client";
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Link from 'next/link';
import { PrimeReactProvider, PrimeReactContext } from 'primereact/api';
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { FilterMatchMode } from 'primereact/api';
import { InputText } from 'primereact/inputtext';


const App = () => {
    //table display variables
    const [isLoading, setLoading] = useState(true);
    const [tripData, setTripData] = useState([]);
    const [tripLeaderData, setTripLeaderData] = useState([]);
    const [tripPreferenceData, setTripPreferenceData] = useState([]);
    const [filters, setFilters] = useState({
        global: {value: null, matchMode: FilterMatchMode.CONTAINS},
    });

    const tripheader = <h1 className="mb-5 text-3xl text-center font-bold">Trip Data</h1>;
    const tripfooter = <p className='ml-1'>Total Trips: {tripData ? tripData.length : 0}</p>;

    const leadheader = <h1 className="mb-5 text-3xl text-center font-bold">Trip Leader Data</h1>;
    const leadfooter = <p className='ml-1'>Total Leaders: {tripLeaderData ? tripLeaderData.length : 0}</p>;

    const prefheader = <h1 className="mb-5 text-3xl text-center font-bold">Trip Preference Data</h1>;
    const preffooter = <p className='ml-1'>Total Prefrences: {tripPreferenceData ? tripPreferenceData.length : 0}</p>;

//edit data variables 
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
    <div>
    <div>
    <div className="navbar bg-base-100 justify-center">
        <a className="btn btn-ghost text-xl" href="/">home</a>
        <a className="btn btn-ghost text-xl" href="/schedules">schedules</a> 
        <a className="btn btn-ghost text-xl" href="/about">about</a>
    </div>

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
      {/* End of the "Edit trip" join section, start displaying data */}
      <div className='mt-5 App'>

      <h1 className='text-xs font-bold mb-1 ml-2'>Search and Filter: </h1>
      <InputText 
      className="ml-1 input input-bordered input-secondary input-sm max-w-xs"
      onInput={(e) => 
        setFilters({
          global: {value: e.target.value, matchMode: FilterMatchMode.CONTAINS},
        })
      }
      />

      <DataTable value={tripData} sortMode="multiple" filters={filters}
      paginator
      rows={10}
      rowsPerPageOptions={[10,20,30]}
      className="table table-sm table-zebra"
      header={tripheader}
      footer={tripfooter}
      >
        <Column field="trip_id" header="Trip ID" sortable></Column>
        <Column field="name" header="Name" sortable></Column>
        <Column field="category" header="Category" sortable></Column>
        <Column field="start_date" header="Start Date" sortable></Column>
        <Column field="end_date" header="End Date" sortable></Column>
        <Column field="lead_guides_needed" header="Lead Guides Needed" sortable></Column>
        <Column field="total_guides_needed" header="Total Guides Needed" sortable></Column>
      </DataTable>
      </div>

      <div className='mt-5 App'>

      <h1 className='text-xs font-bold mb-1 ml-2'>Search and Filter: </h1>
      <InputText 
      className="ml-1 input input-bordered input-secondary input-sm max-w-xs"
      onInput={(e) => 
      setFilters({
        global: {value: e.target.value, matchMode: FilterMatchMode.CONTAINS},
      })
      }
      />

      <div className="overflow-x-auto">
      <DataTable value={tripLeaderData} sortMode="multiple" filters={filters}
      paginator
      rows={10}
      rowsPerPageOptions={[10,20,30]}
      className="table table-sm table-zebra"
      header={leadheader}
      footer={leadfooter}
      >
      <Column field="id" header="ID" sortable></Column>
      <Column field="name" header="Name" sortable></Column>
      <Column field="class_year" header="Class Year" sortable></Column>
      <Column field="semesters_left" header="Semesters Left" sortable></Column>
      <Column field="num_trips_assigned" header="Num Trips Assigned" sortable></Column>
      <Column field="preferred_co_leaders" header="Preferred Co-Leaders" sortable></Column>
      <Column field="reliability_score" header="Reliability Score" sortable></Column>
      <Column field="mountain_biking_role" header="Mountain Biking Roll" sortable></Column>
      <Column field="overnight_role" header="Overnight Role" sortable></Column>
      <Column field="sea_kayaking_role" header="Sea Kayaking Role" sortable></Column>
      <Column field="spelunking_Role" header="Spelunking Role" sortable></Column>
      <Column field="surfing_role" header="Surfing Role" sortable></Column>
      <Column field="watersports_role" header="Watersports Role" sortable></Column>
      </DataTable>
      </div>
      </div>

      <div className='mt-5 App'>

      <h1 className='text-xs font-bold mb-1 ml-2'>Search and Filter: </h1>
      <InputText 
      className="ml-1 input input-bordered input-secondary input-sm max-w-xs"
      onInput={(e) => 
      setFilters({
        global: {value: e.target.value, matchMode: FilterMatchMode.CONTAINS},
      })
      }
      />

      <DataTable value={tripPreferenceData} sortMode="multiple" filters={filters}
      paginator
      rows={10}
      rowsPerPageOptions={[10,20,30]}
      className="table table-sm table-zebra"
      header={prefheader}
      footer={preffooter}
      >
      <Column field="trip_leader_id" header="Trip Leader ID" sortable></Column>
      <Column field="trip_id" header="Trip ID" sortable></Column>
      <Column field="preference" header="Preference" sortable></Column>
      </DataTable>
      </div>
      </div>
      <div className="mt-10"></div>
      <div className="flex justify-center pt-4">
      <button className="btn btn-outline text-xl mb-5" onClick={() => {
    resetDatabase();
    populateTablesWithNewData();
    }}>Delete All Data</button>
      </div>

    </div>
      
      
    
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