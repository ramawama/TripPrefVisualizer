import React from "react";
import { useState, useEffect } from "react";


const Test = () =>{

    const [data, setData] = useState([]);
    useEffect(() => {
      fetch("/server/server.py/").then(
        res => res.json()
        ).then
        data => {
        setData(data);
          console.log(data);
        });
    }, []);
    return (
      <div>
        
        {data.map((data) => (
            <div>{data}</div>
        ))}
      </div>
    );
};

export default Test