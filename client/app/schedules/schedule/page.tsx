// @app.route('/generate-schedule', methods=['GET'])
// def get_schedule_data():
//     # Database filename and table name
//     db_filename = 'schedule.db'
//     table_name = 'schedule'
    
//     # Retrieve data from the specified database and table
//     data = query_db_to_json(db_filename, table_name)
    
//     # Prepare the response
//     response = {table_name: data}
    
//     return jsonify(response)

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
        const response = await axios.get('http://localhost:5000/generate-schedule');
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
            <th>Lead Guides</th>
            <th>Assistant Guides</th>
          </tr>
        </thead>
        <tbody>
          {scheduleData.map(schedule => (
            <tr key={schedule.trip_id}>
              <td style={{ padding: "10px" }}>{schedule.trip_id}</td>
              <td style={{ padding: "10px" }}>{schedule.lead_guides}</td>
              <td style={{ padding: "10px" }}>{schedule.assistant_guides}</td>
            </tr>
          ))}
        </tbody>
      </table>
      </div>
    </div>
  );
};

export default App;