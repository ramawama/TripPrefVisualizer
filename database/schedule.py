import trip_leader
import trip
import trip_preference
import sqlite3
import json

#first come first serve u gotta update every upload... there needs to be a backend table to save each trip's leaders

# conn=sqlite3.connect('./database/schedule.db')
# c=conn.cursor()
# c.execute("""
#         CREATE TABLE schedule (
#             trip_id INTEGER PRIMARY KEY,
#             lead_guides TEXT,
#             assistant_guides TEXT
#         )""") 
# conn.commit()
# c.execute("""
#         Create TABLE matches (
#                 trip_id INTEGER,
#                 leader_id INTEGER,
#                 PRIMARY KEY(trip_id, leader_id)
#         )""")
# c.close()

# trip.create_trip(1, 'camp', 'Overnight', '2021-09-01', '2021-09-03', 2, 4)
# trip_leader.create_leader(1234, "John Doe", 2022, 4, 5, 3, json.dumps(['Jane Doe', 'John Smith']), "Lead", "Promotion", "None", "Lead", "None", "Promotion")
# trip_leader.create_leader(1235, "John Smith", 2022, 4, 5, 3, json.dumps(['Jane Doe', 'John Doe']), "Promotion", "Promotion", "None", "Lead", "None", "Promotion")
# trip_leader.create_leader(1236, "Jane Doe", 2022, 4, 5, 3, json.dumps(['John Doe', 'John Smith']), "Promotion", "Promotion", "None", "Lead", "None", "Promotion")
# trip_leader.create_leader(1237, "what", 2022, 4, 5, 3, json.dumps(['Jane Doe', 'John Smith']), "None", "Promotion", "None", "Lead", "None", "Promotion")
# trip_leader.create_leader(1238, "supposed leader", 2022, 4, 5, 3, json.dumps(['Jane Doe', 'John Smith']), "Lead", "Promotion", "None", "Lead", "None", "Promotion")
# trip_preference.create_trip_preference(1234, 1, 5)
# trip_preference.create_trip_preference(1235, 1, 5)
# trip_preference.create_trip_preference(1236, 1, 5)
# trip_preference.create_trip_preference(1237, 1, 5)
# trip_preference.create_trip_preference(1238, 1, 5)



def set_leads(current_trip, schedule_type):

    #make dictionary: trip type to leader tirp role
    trip_roles={'Overnight': 'overnight_role', 'Mountain Biking': 'mountain_biking_role', 'Spelunking': 'spelunking_role', 'Watersports': 'watersports_role', 'Surfing': 'surfing_role', 'Sea Kayaking': 'sea_kayaking_role'}
    #get all leads of trip type
    leaders=trip_leader.get_all_leads(trip_roles[current_trip[2]])

    # make a dictionary of leader_id: preference
    leader_preferences={}

    conn=sqlite3.connect('./database/schedule.db')
    c=conn.cursor()

    # get all preferences for this trip type
    for leader in leaders:
        leader_id=leader[0]
        preference=trip_preference.get_trip_preference_by_id(leader_id, current_trip[0])
        if preference is not None:
            leader_preferences[leader_id]=preference

    remaining_leaders=current_trip[5]

    # if there are not enough leaders, return error
    if len(leader_preferences) < remaining_leaders:
        return ("Not enough leaders for trip with id {}".format(current_trip[0]))
    
    #return bracket: final leads
    leads=[]
    # while existing_leaders > 0, get leader with highest preference
    count = -1
    while remaining_leaders > 0:
        max_preference=max(leader_preferences, key=leader_preferences.get)

        # check if leader has too many trips
        c.execute("SELECT * FROM matches WHERE leader_id=?", (max_preference,))

        #if special schedule type, skip consideration of too many trips
        #if leader has too many trips and still has a positive preference, move to bottom
        if schedule_type==2 and len(c.fetchall()) > 3 and leader_preferences[max_preference] >=0:
            #move to bottom
            leader_preferences[max_preference]=count
            count-=1
            continue

        # add leader to schedule; either high and no trips or high and too many trips
        leads.append(max_preference)

        # remove leader from leader_preferences
        leader_preferences.pop(max_preference)
        remaining_leaders-=1

    leader_preferences.clear()
    #leads are IDs
    return json.dumps(leads)


def set_assistants(trip, schedule_type):

    trip_roles={'Overnight': 7, 'Mountain Biking': 8, 'Spelunking': 9, 'Watersports': 10, 'Surfing': 11, 'Sea Kayaking': 12}

    # get all who wants promotions
    leaders=trip_leader.get_all_leaders()
    assistant_points={}

    conn=sqlite3.connect('./database/schedule.db')
    c=conn.cursor()

    #get co leaders of this trip's leader
    leads=get_leads(trip[0])
    leads_list=json.loads(leads)

    #considers schedule type 2 first: only care about max preference
    if schedule_type==2:
        for leader in leaders:
            if leader[0] in leads_list:
                continue
            # get preference; set point to preference; +3 for wanting promote
            assistant_id=leader[0]
            point=0
            curr_leader = trip_preference.get_trip_preference_by_id(assistant_id, trip[0])
            if curr_leader is None:
                point=0
            else:
                point=curr_leader[2]
            assistant_points[assistant_id]=point

        # get this many of the top assistants based on preference 
        remaining_assistants=trip[6]-trip[5]
        top_assistants=[item[0] for item in sorted(assistant_points.items(), key=lambda item: item[1], reverse=True)[:remaining_assistants]]
        return json.dumps(top_assistants)
    

    co_leads=[]
    for lead in leads_list:
        lead_co_leads=trip_leader.get_co_lead_by_name(lead)
        for co in lead_co_leads:
            co_leads.append(co)

    for leader in leaders:
        if leader[0] in leads_list:
            continue
        # get preference; set point to preference; +3 for wanting promote
        assistant_id=leader[0]
        point=0
        curr_leader = trip_preference.get_trip_preference_by_id(assistant_id, trip[0])
        if curr_leader is None:
            point=0
        else:
            point=curr_leader[2]
        if leader[trip_roles[trip[2]]] == 'Promotion':
            point+=3
        elif schedule_type==1:
            #if not promotion, skip entirely if prioritizing promotions
            continue

        #current is promote's preferred leaders
        current=json.loads(leader[6])
        current_contains = any(item in leads_list for item in current)
        if current_contains:
            point+=1
        co_lead_contains = any(item in current for item in co_leads)
        if co_lead_contains:
            point+=1

        # add reliability score
        point+=leader[4]
        assistant_points[assistant_id]=point

    
    #return bracket: final leads
    assistants=[]

    # remaining assistants
    remaining_assistants=trip[6]-trip[5]

    # if there are not enough leaders, return all there is
    if len(assistant) < remaining_assistants:
        for assistant in assistant_points:
            assistants.append(assistant)
        return json.dumps(assistants)

    # while existing_leaders > 0, get leader with highest preference
    count = -40
    while remaining_assistants > 0:
        max_preference=max(assistant_points, key=assistant_points.get)
        for assistant, points in assistant_points.items():
            if points > assistant_points[max_preference]:
                max_preference=assistant
            elif points == assistant_points[max_preference]:
                if trip_leader.get_leader_by_ufid(assistant)[3] < trip_leader.get_leader_by_ufid(max_preference)[3]:
                    max_preference=assistant
                    
        # check if leader really doesn't want the trip
        if assistant_points[max_preference] ==0 or assistant_points[max_preference] ==1:
            assistant_points[max_preference]=count
            count-=1
            continue

        # check if leader has too many matches
        c.execute("SELECT * FROM matches WHERE leader_id=?", (max_preference,))
        #if leader current top, has too many matches, and not low preference, move to bottom
        if len(c.fetchall()) > 3 and assistant_points[max_preference] >-40:
            #move to bottom
            assistant_points[max_preference]=count
            count-=1
            continue

        # add leader to schedule; either high and no matches or high and too many matched
        assistants.append(max_preference)

        # remove leader from leader_preferences
        assistant_points.pop(max_preference)
        remaining_assistants-=1

    assistant_points.clear()
    return json.dumps(assistants)



def get_leads(trip_id):
    conn=sqlite3.connect('./database/schedule.db')
    c=conn.cursor()
    c.execute("SELECT lead_guides FROM schedule WHERE trip_id=?", (trip_id,))
    result = c.fetchone()
    conn.close()
    return result[0]
        

#READ ***********
#Schedule type: 0 for regular, 1 for promotion, 2 for preference!!!!!
#READ ***********
def create_schedule_per_trip(trip_id, schedule_type):

    # get if trip exists
    current_trip=trip.get_trip_by_id(trip_id)
    if current_trip is None:
        return ("Trip with id {} does not exist".format(trip_id))

    conn=sqlite3.connect('./database/schedule.db')
    c=conn.cursor()

    # get leads
    leads=[]
    leads=set_leads(current_trip, schedule_type)

    c.execute("INSERT INTO schedule (trip_id, lead_guides, assistant_guides) VALUES (?, ?, ?)", (trip_id, leads, "tentative"))
    conn.commit()

    # get assistants
    assistants=[]
    assistants=set_assistants(current_trip, schedule_type)

    # add to schedule
    c.execute("UPDATE schedule SET assistant_guides = ? WHERE trip_id=?", (assistants, trip_id))
    conn.commit()
    conn.close()

def create_schedule(): # create schedule for all trips
    #reset schedule
    conn=sqlite3.connect('./database/schedule.db')
    c=conn.cursor()
    c.execute("DELETE FROM schedule")
    conn.commit()
    conn.close()
    # get all trips
    trips=trip.get_all_trips()
    # for each trip, create pairing
    for t in trips:
        trip_id=t[0]
        create_schedule_per_trip(trip_id, 0)


def create_promotion_schedule():
    #reset schedule
    conn=sqlite3.connect('./database/schedule.db')
    c=conn.cursor()
    c.execute("DELETE FROM schedule")
    conn.commit()
    conn.close()
    # get all trips
    trips=trip.get_all_trips()
    # for each trip, create pairing
    for t in trips:
        trip_id=t[0]
        create_schedule_per_trip(trip_id, 1)

def create_preference_schedule():
    #reset schedule
    conn=sqlite3.connect('./database/schedule.db')
    c=conn.cursor()
    c.execute("DELETE FROM schedule")
    conn.commit()
    conn.close()
    # get all trips
    trips=trip.get_all_trips()
    # for each trip, create pairing
    for t in trips:
        trip_id=t[0]
        create_schedule_per_trip(trip_id, 2)
        

        
def print_schedule():
    conn=sqlite3.connect('./database/schedule.db')
    c=conn.cursor()
    c.execute("SELECT * FROM schedule")
    records = c.fetchall()
    conn.close()
    return records

def delete_schedule():
    conn=sqlite3.connect('./database/schedule.db')
    c=conn.cursor()
    c.execute("DELETE FROM schedule")
    conn.commit()
    conn.close()
