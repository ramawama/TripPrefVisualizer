import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir=os.path.dirname(current_dir)
database_files_dir=os.path.join(root_dir, 'database')
sys.path.append(database_files_dir)


import schedule
import trip
import trip_leader
import trip_preference
import infoFilter




print(trip.get_all_trips())
print(trip_leader.get_all_leaders())
print(trip.delete_trip(1))
print(trip.get_all_trips())