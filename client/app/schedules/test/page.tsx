
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
        <li>
          <Link href="/">Home</Link>
        </li>
      </button>
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

    <div className='mb-5'></div>
    </div>
    </div>
  );
};

export default App;


