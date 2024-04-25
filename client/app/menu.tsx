import React from "react";
import { MouseEvent } from "react";
import { useState } from "react";
import Link from "next/link";


function Menu() {
  const items = ['visualizer', 'schedule']; // creates list that will be in dropdown menu
  const [isOpen, setIsOpen] = useState(false);

  const handleClick = () => {
    setIsOpen(!isOpen); // Toggles the dropdown open and close
  };

  return (
    <div className="flex justify-around items-center space-x-2">
      {/* Button that links to file upload */}
      <a href="/fileupload" className="btn btn-primary">
        Start Here!
      </a>

      {/* Dropdown Menu */}
      <div className={`dropdown ${isOpen ? 'dropdown-open' : ''}`}>
        <button tabIndex={0} className="btn btn-secondary" onClick={handleClick}>
          Schedules
        </button>
        <ul tabIndex={0} className={`dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52 ${isOpen ? 'block' : 'hidden'}`}>
          {items.map((item) => (
            <li key={item}>
              <a href={`/schedules/${item.toLowerCase()}`} className="block px-4 py-2 text-normal">
                {item.charAt(0).toUpperCase() + item.slice(1)} {/* Capitalize first letter */}
              </a>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Menu;
