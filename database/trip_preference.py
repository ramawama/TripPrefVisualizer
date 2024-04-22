import sqlite3
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
trip_preference_db_path = os.path.join(current_dir, 'trip_preference.db')
trip_db_path=os.path.join(current_dir, 'trip.db')
trip_leader_path=os.path.join(current_dir, 'trip_leader.db')

# conn=sqlite3.connect(trip_preference_db_path)
# c=conn.cursor()
# c.execute("""
#         CREATE TABLE trip_preferences (
#             trip_leader_id INTEGER,
#             trip_leader_name TEXT,
#             trip_id INTEGER,
#             trip_name TEXT,
#             preference INTEGER CHECK (preference IN (0, 1, 2, 3, 4, 5)),
#             PRIMARY KEY(trip_leader_id, trip_id)
#             foreign key(trip_leader_id) references trip_leaders(id),
#             foreign key(trip_id) references trip(trip_id)
#         )""")
# conn.commit()
# conn.close()

def get_trip_preference_by_id(trip_leader_id, trip_id):
    conn=sqlite3.connect(trip_preference_db_path)
    c=conn.cursor()
    c.execute("SELECT * FROM trip_preferences WHERE trip_leader_id=? AND trip_id=?", (trip_leader_id, trip_id))
    result = c.fetchone()
    if result is None:
        return ("Trip with combination ufid {} and trip id {} does not exist".format(trip_leader_id, trip_id))
    conn.close()
    return result

def create_trip_preference(trip_leader_id, trip_id, preference):
    # get if both trip and trip leader exist
    
    conn=sqlite3.connect(trip_db_path)
    c=conn.cursor()
    c.execute("SELECT * FROM trip WHERE trip_id=?", (trip_id,))
    trip_info=c.fetchone()
    if trip_info is None:
        return ("Trip with id {} does not exist".format(trip_id))
    trip_name = trip_info[1]
    conn.close()
    
    conn=sqlite3.connect(trip_leader_path)
    c=conn.cursor()
    c.execute("SELECT * FROM trip_leaders WHERE id=?", (trip_leader_id,))
    leader_info = c.fetchone()
    if leader_info is None:
        return ("Leader with ufid {} does not exist".format(trip_leader_id))
    lead_name = leader_info[1]
    conn.close()
    # check if trip preference already exists
    conn=sqlite3.connect(trip_preference_db_path)
    c=conn.cursor()
    c.execute("SELECT * FROM trip_preferences WHERE trip_leader_id=? AND trip_id=?", (trip_leader_id, trip_id))
    if c.fetchone() is not None:
        return ("Trip with combination ufid {} and trip id {} already exists".format(trip_leader_id, trip_id))
    c.execute("INSERT INTO trip_preferences (trip_leader_id, trip_leader_name, trip_id, trip_name, preference) VALUES (?, ?, ?, ?, ?)", (trip_leader_id, lead_name, trip_id, trip_name, preference))
    conn.commit()
    conn.close()
    return "Success!"

def update_trip_preference(trip_leader_id, trip_id, preference):
    conn=sqlite3.connect(trip_preference_db_path)
    c=conn.cursor()
    c.execute("SELECT * FROM trip_preferences WHERE trip_leader_id=? AND trip_id=?", (trip_leader_id, trip_id))
    if c.fetchone() is None:
        return ("Trip with combination ufid {} and trip id {} does not exist".format(trip_leader_id, trip_id))
    c.execute("UPDATE trip_preferences SET preference=? WHERE trip_leader_id=? AND trip_id=?", (preference, trip_leader_id, trip_id))
    conn.commit()
    conn.close()
    return "Success!"

def delete_trip_preference(trip_leader_id, trip_id):
    conn=sqlite3.connect(trip_preference_db_path)
    c=conn.cursor()
    c.execute("SELECT * FROM trip_preferences WHERE trip_leader_id=? AND trip_id=?", (trip_leader_id, trip_id))
    if c.fetchone() is None:
        return ("Trip with combination ufid {} and trip id {} does not exist".format(trip_leader_id, trip_id))
    c.execute("DELETE FROM trip_preferences WHERE trip_leader_id=? AND trip_id=?", (trip_leader_id, trip_id))
    conn.commit()
    conn.close()
    return "Success!"

def get_all_trip_preferences():
    conn=sqlite3.connect(trip_preference_db_path)
    c=conn.cursor()
    c.execute("SELECT * FROM trip_preferences")
    result = c.fetchall()
    conn.close()
    return result

def delete_all_trip_preferences():
    conn=sqlite3.connect(trip_preference_db_path)
    c=conn.cursor()
    c.execute("DELETE FROM trip_preferences")
    conn.commit()
    conn.close()
    return "Success!"

def delete_associations_by_ufid(ufid):
    conn=sqlite3.connect(trip_preference_db_path)
    c=conn.cursor()
    c.execute("DELETE FROM trip_preferences WHERE trip_leader_id=?", (ufid,))
    conn.commit()
    conn.close()
    return "Success!"

def delete_associations_by_trip_id(id):
    conn=sqlite3.connect(trip_preference_db_path)
    c=conn.cursor()
    c.execute("DELETE FROM trip_preferences WHERE trip_id=?", (id,))
    conn.commit()
    conn.close()
    return "Success!"
