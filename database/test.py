import trip_leader
import trip
import trip_preference
import schedule
import json

def main():

    # print("test leader")
    # l=['Jane Doe', 'John Smith']
    # l=json.dumps(l)
    # print(trip_leader.create_leader(1234, "John Doe", 2022, 4, 5, 3, l, "Lead", "Promotion", "None", "Lead", "None", "Promotion"))
    # # print(trip_leader.get_leader_by_name("John Doe"))
    # print(trip_leader.get_leader_by_ufid(1234))
    # print(trip_leader.delete_leader_by_name("John Doe"))
    # print(trip_leader.get_leader_by_name("John Doe"))
    # print(trip_leader.create_leader(1234, "John Doe", 2022, 4, 5, 3, l, "Lead", "Promotion", "None", "Lead", "None", "Promotion"))
    # print(trip_leader.create_leader(1235, "John Smith", 2022, 4, 5, 3, l, "Lead", "Promotion", "None", "Lead", "None", "Promotion"))
    # print(trip_leader.update_leader_by_ufid(1234, "John 35", 2022, 4, 5, 3, l, "Lead", "Promotion", "None", "Lead", "None", "Promotion"))
    # print(trip_leader.get_all_leaders())

    # print("test trip")
    # print(trip.create_trip(1, 'camp', 'Overnight', '2021-09-01', '2021-09-03', 2, 4))
    # print(trip.create_trip(2, 'camp', 'Overnight', '2021-09-01', '2021-09-03', 2, 4))
    # print(trip.get_trip_by_id(1))
    # print(trip.delete_trip(1))
    # print(trip.get_trip_by_id(1))
    # print(trip.create_trip(1, 'camp', 'Overnight', '2021-09-01', '2021-09-03', 2, 4))
    # print(trip.get_all_trips())


    # print("test trip_preference")
    # print(trip_preference.create_trip_preference(1234, 1, 5))
    # print(trip_preference.create_trip_preference(1235, 1, 5))
    # print(trip_preference.get_trip_preference_by_id(1235, 1))
    # print(trip_preference.get_all_trip_preferences())
    # print(trip_preference.delete_associations_by_trip_id(1))
    # print(trip_preference.get_all_trip_preferences())
    # print(trip_preference.create_trip_preference(1234, 1, 5))
    # print(trip_preference.create_trip_preference(1235, 1, 5))
    # print(trip_preference.delete_associations_by_ufid(1234))
    # print(trip_preference.get_all_trip_preferences())
    # print(trip_preference.delete_all_trip_preferences())

    # print(trip_preference.delete_all_trip_preferences())
    # print(trip.delete_all_trips())
    # print(trip_leader.delete_all_leaders())


    # print("test schedule")
    # trip.create_trip(1, 'camp', 'Overnight', '2021-09-01', '2021-09-03', 2, 4)
    # print(trip.create_trip(2, 'swim', 'Mountain Biking', '2021-09-01', '2021-09-03', 2, 4))
    
    # trip_leader.create_leader(1234, "John Doe", 2022, 4, 5, 3, json.dumps(['Jane Doe', 'John Smith']), "Lead", "Lead", "None", "Lead", "None", "Promotion")
    # trip_leader.create_leader(1235, "John Smith", 2022, 4, 5, 3, json.dumps(['Jane Doe', 'John Doe']), "Promotion", "Promotion", "None", "Lead", "None", "Promotion")
    # trip_leader.create_leader(1236, "Jane Doe", 2022, 4, 5, 3, json.dumps(['John Doe', 'John Smith']), "Promotion", "Promotion", "None", "Lead", "None", "Promotion")
    # trip_leader.create_leader(1237, "what", 2022, 4, 5, 3, json.dumps(['']), "None", "Promotion", "None", "Lead", "None", "Promotion")
    # trip_leader.create_leader(1238, "supposed leader", 2022, 4, 5, 3, json.dumps(['']), "Lead", "Promotion", "None", "Lead", "None", "Promotion")
    # trip_leader.create_leader(1239, "supposed leader2", 2022, 4, 5, 3, json.dumps(['Jane Doe', 'John Smith']), "Lead", "Lead", "None", "Lead", "None", "Promotion")
    # trip_preference.create_trip_preference(1234, 1, 5)
    # trip_preference.create_trip_preference(1235, 1, 5)
    # trip_preference.create_trip_preference(1236, 1, 5)
    # trip_preference.create_trip_preference(1237, 1, 4)
    # trip_preference.create_trip_preference(1238, 1, 5)
    # trip_preference.create_trip_preference(1239, 1, 5)

    # trip_preference.create_trip_preference(1234, 2, 1)
    # trip_preference.create_trip_preference(1235, 2, 1)
    # trip_preference.create_trip_preference(1236, 2, 1)
    # trip_preference.create_trip_preference(1237, 2, 4)
    # trip_preference.create_trip_preference(1238, 2, 5)
    # trip_preference.create_trip_preference(1239, 2, 1)

    # schedule.create_schedule()
    # print(schedule.print_schedule())

    # schedule.create_preference_schedule()
    # print(schedule.print_schedule())


    # schedule.delete_all_schedule()
    # trip.delete_all_trips
    # trip_leader.delete_all_leaders()
    # trip_preference.delete_all_trip_preferences()
    # trip_leader.delete_all_leaders()

    # print(trip_leader.get_all_leaders()+trip.get_all_trips()+trip_preference.get_all_trip_preferences()+schedule.get_all_schedule())



    print("hello")




if __name__ == "__main__":
    main()