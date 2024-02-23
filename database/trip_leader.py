"""Develop a TripLeader class to manage detailed information about trip leaders 

Class Attributes: 
Name: 
Description: The full name of the trip leader. 
Class Year: 
Description: The year the trip leader joined the trip leader program 
Trip Roles: 
Description: A structure to store the trip leader's designated role (lead or assistant guide) for different types of trips. 
Trip Types: Overnight, Mountain Biking, Spelunking, Watersports, Surfing, Sea Kayaking. 
Each trip type will have an associated role (lead or assistant). 
Trip Preferences: 
Description: A separate structure to store the trip leader's ranking for different types of trips. 

Each trip type will have an associated ranking from 0 to 5. 
Blank : Not available 
5: Would love to lead 
4: Willing to lead 
3: Neutral 
2: Prefer not to lead 
1: Would rather not lead 

Semesters left: 
Description: The number of semesters the trip leader has left.

Reliability score: 
Based on how many trips a trip leader has cancelled and how many trips a 
trip leader has picked up (which is when a trip leader takes over a trip 
that another trip leader is supposed to lead, but cannot for whatever reason) 

Number of trips assigned (semester by semester, not total): 
How many trips has this leader already been assigned this semester? 
What kinds of trips have they been assigned to  

Who would they like to lead with? 
Which trip leaders would this trip leader like to lead with 

 """

import sqlite3

conn=sqlite3.connect('./trip_leader.db')

c=conn.cursor()

# c.execute("""
#         CREATE TABLE trip_leader (
#         name TEXT,
#         class_year INTEGER,
#         trip_roles TEXT,
#         trip_types TEXT,
#         trip_preferences TEXT,
#         semesters_left INTEGER,
#         reliability_score INTEGER,
#         num_trips_assigned INTEGER,
#         type_trips_assigned TEXT,
#         who_lead_with TEXT
#         )"""
#         )

# c.execute("INSERT INTO trip_leader VALUES ('John Doe', 2023, 'lead', 'Overnight', '5', 3, 5, 2, 'Overnight', 'Jane Doe')")
conn.commit()

c.execute("SELECT * FROM trip_leader")

# Fetch all the records
records = c.fetchall()

# Print each record
for record in records:
    print(record)

#safely close file
conn.close()