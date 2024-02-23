"""Class Attributes: 
Category: 
Type: String 
Description: Specifies the type of trip. Valid options are: 
Overnight Adventure 
Day Adventure 
Weeknight Adventure 
OLC Training TRiP 
Pro Dev 
Incentive TRiP 
Extended TRiP 

Validation Required: Ensure the category provided is one of the valid options. 

Start and End Dates: Description: Represents the start and end dates of the trip. 

Lead Guides Needed: Description: Number of lead guides required for the trip. 

Total Guides Needed: Description: Number of total guides required for the trip. 
Once the lead guide requirement is filled, the rest can be any type of guide (lead or assistant) 

A unique trip ID: An ID that separates the trip from trips of the same name """

import sqlite3

#connector: used to access the database
conn=sqlite3.connect('./trip.db')
c=conn.cursor()

# Create the table trip.db with appropriate columns; no need to create again
# c.execute("""
#     CREATE TABLE trip (
#         id INTEGER PRIMARY KEY,
#         category TEXT CHECK(category IN ('Overnight Adventure', 'Day Adventure', 'Weeknight Adventure', 'OLC Training TRiP', 'Pro Dev', 'Incentive TRiP', 'Extended TRiP')),
#         start_date TEXT,
#         end_date TEXT,
#         lead_guides_needed INTEGER,
#         total_guides_needed INTEGER
#     )
# """)
# Insert a record into the trip table; test
# c.execute("INSERT INTO trip VALUES (1, 'Overnight Adventure', '2021-09-01', '2021-09-03', 2, 4)")

def create_trip(id, category, start_date, end_date, lead_guides_needed, total_guides_needed):
    conn=sqlite3.connect('./trip.db')
    c=conn.cursor()
    if not isinstance(id, int):
        return ("Error: id must be an integer")
    if not isinstance(category, str):
        return ("Error: category must be a string") 
    if not is_trip_type(category):
        return ("Error: category must be one of the following: 'Overnight Adventure', 'Day Adventure', 'Weeknight Adventure', 'OLC Training TRiP', 'Pro Dev', 'Incentive TRiP', 'Extended TRiP'")
    if not isinstance(start_date, str):
        return ("Error: start_date must be a string")
    if not isinstance(end_date, str):
        return ("Error: end_date must be a string")
    if not isinstance(lead_guides_needed, int):
        return ("Error: lead_guides_needed must be an integer")
    if not isinstance(total_guides_needed, int):
        return ("Error: total_guides_needed must be an integer")
    c.execute("SELECT * FROM trip WHERE id=?", (id,))
    if c.fetchone() is not None:
        return ("Error: id must be unique")
    
    #everything is checked, except if category is valid within the options
    try:
        c.execute("INSERT INTO trip VALUES (?, ?, ?, ?, ?, ?)", (id, category, start_date, end_date, lead_guides_needed, total_guides_needed))
    except sqlite3.IntegrityError as e:
        return ("Error: ", e)
    
    conn.commit()
    conn.close()
    return "Success!"

#questionable: how should we return an error message?
def get_trip_by_id(id):
    conn=sqlite3.connect('./trip.db')
    c=conn.cursor()
    if not isinstance(id, int):
        return ("Error: id must be an integer")
    try:
        c.execute("SELECT * FROM trip WHERE id=?", (id,))
    except sqlite3.IntegrityError as e:
        return ("Error: ", e)
    result = c.fetchone()
    conn.close()
    return result


def update_trip(id, category, start_date, end_date, lead_guides_needed, total_guides_needed):
    conn=sqlite3.connect('./trip.db')
    c=conn.cursor()
    if not isinstance(id, int):
        return ("Error: id must be an integer")
    
    c.execute("SELECT * FROM trip WHERE id=?", (id,))
    if c.fetchone() is None:
        return ("Trip with id {} does not exist".format(id))
    
    if not isinstance(category, str):
        return ("Error: category must be a string") 
    if not is_trip_type(category):
        return ("Error: category must be one of the following: 'Overnight Adventure', 'Day Adventure', 'Weeknight Adventure', 'OLC Training TRiP', 'Pro Dev', 'Incentive TRiP', 'Extended TRiP'")
    if not isinstance(start_date, str):
        return ("Error: start_date must be a string")
    if not isinstance(end_date, str):
        return ("Error: end_date must be a string")
    if not isinstance(lead_guides_needed, int):
        return ("Error: lead_guides_needed must be an integer")
    if not isinstance(total_guides_needed, int):
        return ("Error: total_guides_needed must be an integer")
    
    try:
        c.execute("UPDATE trip SET category=?, start_date=?, end_date=?, lead_guides_needed=?, total_guides_needed=? WHERE id=?", (category, start_date, end_date, lead_guides_needed, total_guides_needed, id))
    except sqlite3.InterfaceError as e:
        return ("Error:", e)
    conn.commit()
    conn.close()
    return "Success!"

def get_all_trips():
    conn=sqlite3.connect('./trip.db')
    c=conn.cursor()
    c.execute("SELECT * FROM trip")
    records = c.fetchall()
    conn.close()
    return records

def delete_trip(id):
    conn=sqlite3.connect('./trip.db')
    c=conn.cursor()
    if not isinstance(id, int):
        return ("Error: id must be an integer")
    c.execute("SELECT * FROM trip WHERE id=?", (id,))
    if c.fetchone() is None:
        return ("Trip with id {} does not exist".format(id))
    c.execute("DELETE FROM trip WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return "Success!"


def is_trip_type(category):
    if category not in ['Overnight Adventure', 'Day Adventure', 'Weeknight Adventure', 'OLC Training TRiP', 'Pro Dev', 'Incentive TRiP', 'Extended TRiP']:
        return False
    return True