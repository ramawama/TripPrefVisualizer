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
# conn.commit()

# Query the database and return all records
c.execute("SELECT * FROM trip")

# Fetch all the records
records = c.fetchall()

# Print each record
for record in records:
    print(record)

#safely close file
conn.close()