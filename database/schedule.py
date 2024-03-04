import trip_leader
import trip
import trip_preference
import sqlite3
import json

#first come first serve u gotta update every upload... there needs to be a backend table to save each trip's leaders

def create_schedule():
    conn=sqlite3.connect('./database/schedule.db')
    c=conn.cursor()
    c.execute("""
            CREATE TABLE schedule (
                trip_id INTEGER PRIMARY KEY,
                lead_guides TEXT,
                assistant_guides TEXT
            )""") 
    conn.commit()
    c.execute("""
              Create TABLE matches (
                    trip_id INTEGER,
                    leader_id INTEGER,
                    PRIMARY_KEY(trip_id, leader_id)
              )
              """)
    c.close()
    # get all trips
    trips=trip.get_all_trips()
    # for each trip, create pairing
    for trip in trips:
        trip_id=trip[0]
        create_schedule_per_trip(trip_id)
        

def create_schedule_per_trip(trip_id):
    # get if trip exists
    trip=trip.get_trip_by_id(trip_id)
    if trip is None:
        return ("Trip with id {} does not exist".format(trip_id))
    trip_type=trip[2]

    # get leads
    leads=set_leads(trip)

    # get assistants
    assistants=set_assistants(trip)

    # add to schedule
    conn=sqlite3.connect('./database/schedule.db')
    c=conn.cursor()
    c.execute("INSERT INTO schedule (trip_id, lead_guides, assistant_guides) VALUES (?, ?, ?)", (trip_id, leads, assistants))
    conn.commit()
    conn.close()


def set_leads(trip):
    leaders=trip_leader.get_all_leads(trip[2])

    # make a dictionary of leader_id: preference
    leader_preferences={}

    conn=sqlite3.connect('./database/schedule.db')
    c=conn.cursor()

    # get all preferences for this trip type
    for leader in leaders:
        leader_id=leader[0]
        preference=trip_preference.get_trip_preference_by_id(leader_id, trip[0])
        if preference is not None:
            leader_preferences[leader_id]=preference

    remaining_leaders=trip[5]

    # if there are not enough leaders, return error
    if len(leader_preferences) < remaining_leaders:
        return ("Not enough leaders for trip with id {}".format(trip[0]))
    
    #return bracket: final leads
    leads=[]
    # while existing_leaders > 0, get leader with highest preference
    count = -1
    while remaining_leaders > 0:
        max_preference=max(leader_preferences, key=leader_preferences.get)
        c.execute("SELECT * FROM matches WHERE leader_id=?", (max_preference,))
        if len(c.fetchall()) > 3 and leader_preferences[max_preference] >=0:
            #move to bottom
            leader_preferences[max_preference]=count
            count-=1
            continue

        # add leader to schedule; either high and no matches or high and too many matched
        leads.add(max_preference)

        # remove leader from leader_preferences
        leader_preferences.pop(max_preference)
        remaining_leaders-=1

    leader_preferences.clear()
    return json.dumps(leads)

def get_leads(trip_id):
    conn=sqlite3.connect('./database/schedule.db')
    c=conn.cursor()
    c.execute("SELECT lead_guides FROM schedule WHERE trip_id=?", (trip_id,))
    result = c.fetchone()
    conn.close()
    return result

def set_assistants(trip):
    promotes=trip_leader.get_all_promotions(trip[2])
    assistant_points={}

    conn=sqlite3.connect('./database/schedule.db')
    c=conn.cursor()

    leads=get_leads(trip[0])
    leads_list=json.loads(leads)
    co_leads=[]
    for lead in leads_list:
        lead_co_leads=trip_leader.get_co_leads(lead)
        for co in lead_co_leads:
            co_leads.add(co)

    for promote in promotes:
        promote_id=promote[0]
        point = trip_preference.get_trip_preference_by_id(promote_id, trip[0])
        current=json.loads(promote[6])
        current_contains = any(item in leads_list for item in current)
        if current_contains:
            point+=1
        co_lead_contains = any(item in current for item in co_leads)
        if co_lead_contains:
            point+=1
        point-=promote[4]
        assistant_points[promote_id]=point
    
    #return bracket: final leads
    assistants=[]

    # remaining assistants
    remaining_assistants=trip[6]-trip[5]

    # while existing_leaders > 0, get leader with highest preference
    count = -40
    while remaining_assistants > 0:
        max_preference=max(assistant_points, key=assistant_points.get)
        c.execute("SELECT * FROM matches WHERE leader_id=?", (max_preference,))
        if len(c.fetchall()) > 3 and assistant_points[max_preference] >-40:
            #move to bottom
            assistant_points[max_preference]=count
            count-=1
            continue

        # add leader to schedule; either high and no matches or high and too many matched
        assistants.add(max_preference)

        # remove leader from leader_preferences
        assistant_points.pop(max_preference)
        remaining_assistants-=1

    assistant_points.clear()
    return json.dumps(assistants)
        