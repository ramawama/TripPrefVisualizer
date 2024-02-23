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

# create table to input into; no need anymore, file created
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

def check_parapmeter_validity(name, class_year, trip_roles, trip_types, trip_preferences, semesters_left, reliability_score, num_trips_assigned, type_trips_assigned, who_lead_with):
    if not isinstance(name, str):
        return ("Error: name must be a string")
    if not isinstance(class_year, int):
        return ("Error: class_year must be an integer")
    if not isinstance(trip_roles, str):
        return ("Error: trip_roles must be a string")
    if not isinstance(trip_types, str):
        return ("Error: trip_types must be a string")
    if not isinstance(trip_preferences, str):
        return ("Error: trip_preferences must be a string")
    if not isinstance(semesters_left, int):
        return ("Error: semesters_left must be an integer")
    if not isinstance(reliability_score, int):
        return ("Error: reliability_score must be an integer")
    if not isinstance(num_trips_assigned, int):
        return ("Error: num_trips_assigned must be an integer")
    if not isinstance(type_trips_assigned, str):
        return ("Error: type_trips_assigned must be a string")
    if not isinstance(who_lead_with, str):
        return ("Error: who_lead_with must be a string")
    return True

def create_trip_leader(name, class_year, trip_roles, trip_types, trip_preferences, semesters_left, reliability_score, num_trips_assigned, type_trips_assigned, who_lead_with):
    msg = check_parapmeter_validity(name, class_year, trip_roles, trip_types, trip_preferences, semesters_left, reliability_score, num_trips_assigned, type_trips_assigned, who_lead_with)  
    if msg != True:
        return msg
    conn=sqlite3.connect('./trip_leader.db')
    c=conn.cursor()
    c.execute("INSERT INTO trip_leader VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (name, class_year, trip_roles, trip_types, trip_preferences, semesters_left, reliability_score, num_trips_assigned, type_trips_assigned, who_lead_with))
    conn.commit()
    conn.close()
    return "Success!"


#again, not sure how to return either an error message or a record
def query_trip_leader(name):
    conn=sqlite3.connect('./trip_leader.db')
    c=conn.cursor()
    c.execute("SELECT * FROM trip_leader WHERE name=?", (name,))
    records = c.fetchall()
    conn.close()
    return records

def update_trip_leader(name, class_year, trip_roles, trip_types, trip_preferences, semesters_left, reliability_score, num_trips_assigned, type_trips_assigned, who_lead_with):
    msg = check_parapmeter_validity(name, class_year, trip_roles, trip_types, trip_preferences, semesters_left, reliability_score, num_trips_assigned, type_trips_assigned, who_lead_with)  
    if msg != True:
        return msg
    conn=sqlite3.connect('./trip_leader.db')
    c=conn.cursor()
    c.execute("UPDATE trip_leader SET class_year=?, trip_roles=?, trip_types=?, trip_preferences=?, semesters_left=?, reliability_score=?, num_trips_assigned=?, type_trips_assigned=?, who_lead_with=? WHERE name=?", (class_year, trip_roles, trip_types, trip_preferences, semesters_left, reliability_score, num_trips_assigned, type_trips_assigned, who_lead_with, name))
    conn.commit()
    conn.close()
    return "Success!"

def delete_trip_leader(name):
    conn=sqlite3.connect('./trip_leader.db')
    c=conn.cursor()
    if not isinstance(name, str):
        return ("Error: name must be a string")
    c.execute("SELECT * FROM trip_leader WHERE name=?", (name,))
    if c.fetchone() is None:
        return ("Trip leader with name {} does not exist".format(name))
    c.execute("DELETE FROM trip_leader WHERE name=?", (name,))
    conn.commit()
    conn.close()
    return "Success!"

