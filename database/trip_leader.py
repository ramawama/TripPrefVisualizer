import sqlite3

# create table to input into; no need anymore, file created
# uses linking table: id to big table to individuals connective tables
# c.execute("""
#         CREATE TABLE trip_leaders (
#             id INTEGER PRIMARY KEY,
#             name TEXT
#             class_year INTEGER,
#             semesters_left INTEGER,
#             reliability_score INTEGER,
#             num_trips_assigned INTEGER,
#         )""")
# c.execute("""
#         CREATE TABLE preferences (
#             id INTEGER PRIMARY KEY,
#             preference INTEGER,
#         )""")
# c.execute("""
#         CREATE TABLE roles (
#             id INTEGER PRIMARY KEY,
#             roles TEXT
#         )""")
# c.execute("""
#         CREATE TABLE trips (
#             id INTEGER PRIMARY KEY,
#             type TEXT
#         )""")
# c.execute("""
#         CREATE TABLE trip_leader_trip_types (
#             trip_leader_id INTEGER,
#             trip_type_id INTEGER,
#             preference_id INTEGER,
#             role_id INTEGER,
#             PRIMARY KEY(trip_leader_id, trip_type_id),
#             FOREIGN KEY(trip_leader_id) REFERENCES trip_leaders(id),
#             FOREIGN KEY(trip_type_id) REFERENCES trip_types(id),
#             FOREIGN KEY(preference_id) REFERENCES preferences(id),
#             FOREIGN KEY(role_id) REFERENCES roles(id)
#         )""")


def check_leader_parapmeter_validity(name, class_year, semesters_left, reliability_score, num_trips_assigned):
    if not isinstance(name, str):
        return ("Error: name must be a string")
    if not isinstance(class_year, int):
        return ("Error: class_year must be an integer")
    if not isinstance(semesters_left, int):
        return ("Error: semesters_left must be an integer")
    if not isinstance(reliability_score, int):
        return ("Error: reliability_score must be an integer")
    if not isinstance(num_trips_assigned, int):
        return ("Error: num_trips_assigned must be an integer")
    return True

def check_trip_type_parapmeter_validity(trip_type, preference, roles):
    if not isinstance(trip_type, str):
        return ("Error: trip_type must be a string")
    if not isinstance(preference, int):
        return ("Error: preference must be an integer")
    if not isinstance(roles, str):
        return ("Error: roles must be a string")
    return True
