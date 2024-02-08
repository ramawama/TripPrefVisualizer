"use client";

import React, { useEffect, useState } from 'react';

const AnalyticsComponent = () => {
  const [data, setData] = useState({});

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch('http://localhost:5000/analytics');
      const jsonData = await response.json();
      setData(jsonData);
    };

    fetchData().catch(console.error);
  }, []);

  return (
    <div>
      <h1>Analytics</h1>
      <p>Trips: {data.Trips}</p>
    </div>
  );
};

export default AnalyticsComponent;
