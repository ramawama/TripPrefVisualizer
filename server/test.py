from database.trip_leader import delete_all_leaders, create_leader
from database.trip import delete_all_trips, create_trip
from database.trip_preference import delete_all_trip_preferences, create_trip_preference
import json
import random

print("Generating random data...")
#these lines delete all the past data in the tables, so we can start fresh each time
delete_all_trip_preferences()
delete_all_trips()
delete_all_leaders()

random.seed(42) #set seed for reproducibility

#defining the possible values for the fields
names = [
"Alex", "Jordan", "Taylor", "Morgan", "Casey", "River", "Jamie", "Skyler",
"Quinn", "Reese", "Avery", "Riley", "Cameron", "Sage", "Peyton", "Blake",
"Drew", "Jesse", "Kennedy", "Elliot", "Charlie", "Finley", "Rowan", "Hayden",
"Emerson", "Devin", "Dakota", "Logan", "Micah", "Spencer", "Parker", "Kai",
"Bailey", "Harley", "Phoenix", "Reagan", "Sawyer", "Teagan", "Ashton", "Dallas"
]
class_years = [2020, 2021, 2022, 2023, 2024]
semesters = [1, 2, 3, 4, 5, 6, 7, 8]
reliability_scores = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]  # Assuming a score from 1 to 5
roles = ["None", "Lead", "Promotion"] 
trip_category = ['Overnight', 'Mountain Biking', 'Spelunking', 'Watersports', 'Surfing', 'Sea Kayaking']
all_ufids = []
all_trip_ids = []

def generate_random_leader(name):
    ufid = random.randint(10000000, 99999999)  # any 8 digit number
    if ufid not in all_ufids:
        all_ufids.append(ufid)
    class_year = random.choice(class_years)
    semesters_left = random.choice(semesters)
    reliability_score = random.choice(reliability_scores)

    names_without_input_name = [n for n in names if n != name] # remove the input name from the list of names
    number_of_preferred_co_leaders = random.randint(1, 3)
    preferred_co_leaders = random.sample(names_without_input_name, number_of_preferred_co_leaders)
    preferred_co_leaders = json.dumps(preferred_co_leaders)

    overnight_role = random.choice(roles)
    mountain_biking_role = random.choice(roles)
    spelunking_role = random.choice(roles)
    watersports_role = random.choice(roles)
    surfing_role = random.choice(roles)
    sea_kayaking_role = random.choice(roles)
    
    create_leader(ufid, name, class_year, semesters_left, reliability_score, 0, preferred_co_leaders, overnight_role, mountain_biking_role, spelunking_role, watersports_role, surfing_role, sea_kayaking_role)


def generate_leaders():
    for name in names:
        generate_random_leader(name)


def generate_random_trip(trip_id):
    if trip_id not in all_trip_ids:
        all_trip_ids.append(trip_id)
    month = random.randint(1, 12)
    day = random.randint(1, 28) 
    month_str = str(month).zfill(2)
    day_str = str(day).zfill(2) 
    start_date = f"2024-{month_str}-{day_str}"

    num_of_lead_guides = random.randint(1, 2)
    if num_of_lead_guides == 1:
        num_of_leaders = 2
    else:
        num_of_leaders = 4

    random_category = random.choice(trip_category)
    trip_name = "Example " + random_category + " Trip"

    #the start date is the same as teh end date for these examples
    create_trip(trip_id, trip_name, random_category, start_date, start_date, num_of_lead_guides, num_of_leaders)

def generate_trips():
    #generate 30 random trips, the trip_id is the index
    for i in range(30):
        generate_random_trip(i)


def generate_random_trip_preference(ufid, trip_id):
    preference = random.randint(1, 5)
    create_trip_preference(ufid, trip_id, preference)

def generate_preferences():
    for ufid in all_ufids:
        for trip_id in all_trip_ids:
            generate_random_trip_preference(ufid, trip_id)

generate_leaders()
generate_trips()
generate_preferences()

print(f"Data generated successfully with seed 42!")

