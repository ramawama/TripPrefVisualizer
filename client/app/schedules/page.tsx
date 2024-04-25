"use client";
import React, { useEffect, useState } from "react";
import axios from "axios";
import Link from "next/link";
import { DataTable } from 'primereact/datatable';
import { Column } from 'primereact/column';
import { FilterMatchMode } from 'primereact/api';
import { InputText } from 'primereact/inputtext';

const App = () => {
  const [isLoading, setLoading] = useState(true);
  const [scheduleData, setScheduleData] = useState([]);

  const tripheader = <h1 className="mb-5 text-3xl text-center font-bold">Trip Data</h1>;
  const tripfooter = <p className='ml-1'>Total Trips: {scheduleData ? scheduleData.length : 0}</p>;

  const [filters, setFilters] = useState({
    global: {value: null, matchMode: FilterMatchMode.CONTAINS},
  });

  useEffect(() => {
    const fetchData = async () => {
      try {
        // fetch JSON data from your API endpoint
        const response = await axios.get("http://localhost:5000/schedule");
        const data = response.data;

        // separate data into individual arrays
        const { schedule } = data;

        setScheduleData(schedule);

        setLoading(false);
      } catch (error) {
        console.error("Error fetching data:", error);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (isLoading) return <p>Loading...</p>;

  return (
    <div>
    <div className="navbar bg-base-100 justify-center">
        <a className="btn btn-ghost text-xl" href="/">home</a>
        <a className="btn btn-ghost text-xl" href="/displaydata">display data</a> 
        <a className="btn btn-ghost text-xl" href="/about">about</a>
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

      <DataTable value={scheduleData} sortMode="multiple" filters={filters}
      paginator
      rows={10}
      rowsPerPageOptions={[10,20,30]}
      className="table table-sm table-zebra"
      header={tripheader}
      footer={tripfooter}
      >
        <Column field="trip_name" header="Trip Name" sortable></Column>
        <Column field="trip_id" header="Trip ID" sortable></Column>
        <Column field="lead_guides" header="Lead Guides" sortable></Column>
        <Column field="assistant_guides" header="Assistant Guides" sortable></Column>
      </DataTable>
      </div>
      </div>

  );
};

export default App;
