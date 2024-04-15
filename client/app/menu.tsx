import React from "react";
import { MouseEvent } from "react";
import { useState } from "react";
import Link from "next/link";



function Menu() {
    const items = ['One', 'Two', 'Three', 'Test']; //creates list that will be in dropdown menu
    const handleClick = (event : MouseEvent)=>setIsOpen(!isOpen); //event handler
    const [isOpen, setIsOpen] = useState(false);

    return (
        <>
        
        <ul className="menu menu-horizontal bg-base-200 rounded-box"> 
        <li><Link href="/fileupload">Start Here!</Link></li>
        <li>
            <span 
                role="button" 
                className={`menu-dropdown-toggle ${isOpen ? 'menu-dropdown-show' : ''}`}
                onClick={handleClick}
            >Schedules</span>
            <ul className={`menu-dropdown ${isOpen ? 'menu-dropdown-show' : ''}`}>
                {items.map((item) => (
                    <li 
                    role="button"
                    className="mb-4 menu-dropdown"
                    key={item}
                    ><Link href={`/schedules/${item.toLowerCase()}`}>{item}</Link>
                    </li>
                ))}
            </ul>
            </li>
        </ul>
        </>
    );
}

export default Menu;