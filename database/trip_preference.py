import sqlite3

# conn=sqlite3.connect('./database/trip_preference.db')
# c=conn.cursor()

# c.execute("""
#         CREATE TABLE trip_preferences (
#             trip_leader_id INTEGER,
#             trip_id INTEGER,
#             preference INTEGER CHECK (preference IN (0, 1, 2, 3, 4, 5)),
#             PRIMARY KEY(trip_leader_id, trip_id)
#             foreign key(trip_leader_id) references trip_leaders(id),
#             foreign key(trip_id) references trip(trip_id)
#         )""")

# conn.commit()
# conn.close()

def get_trip_preference_by_id(trip_leader_id, trip_id):
    conn=sqlite3.connect('./database/trip_preference.db')
    c=conn.cursor()
    c.execute("SELECT * FROM trip_preferences WHERE trip_leader_id=? AND trip_id=?", (trip_leader_id, trip_id))
    result = c.fetchone()
    if result is None:
        return ("Trip with combination ufid {} and trip id {} does not exist".format(trip_leader_id, trip_id))
    conn.close()
    return result

def insert_trip_preference(trip_leader_id, trip_id, preference):
    conn=sqlite3.connect('./database/trip_preference.db')
    c=conn.cursor()
    c.execute("SELECT * FROM trip_preferences WHERE trip_leader_id=? AND trip_id=?", (trip_leader_id, trip_id))
    if c.fetchone() is not None:
        return ("Trip with combination ufid {} and trip id {} already exists".format(trip_leader_id, trip_id))
    c.execute("INSERT INTO trip_preferences (trip_leader_id, trip_id, preference) VALUES (?, ?, ?)", (trip_leader_id, trip_id, preference))
    conn.commit()
    conn.close()
    return "Success!"

def update_trip_preference(trip_leader_id, trip_id, preference):
    conn=sqlite3.connect('./database/trip_preference.db')
    c=conn.cursor()
    c.execute("SELECT * FROM trip_preferences WHERE trip_leader_id=? AND trip_id=?", (trip_leader_id, trip_id))
    if c.fetchone() is None:
        return ("Trip with combination ufid {} and trip id {} does not exist".format(trip_leader_id, trip_id))
    c.execute("UPDATE trip_preferences SET preference=? WHERE trip_leader_id=? AND trip_id=?", (preference, trip_leader_id, trip_id))
    conn.commit()
    conn.close()
    return "Success!"

def delete_trip_preference(trip_leader_id, trip_id):
    conn=sqlite3.connect('./database/trip_preference.db')
    c=conn.cursor()
    c.execute("SELECT * FROM trip_preferences WHERE trip_leader_id=? AND trip_id=?", (trip_leader_id, trip_id))
    if c.fetchone() is None:
        return ("Trip with combination ufid {} and trip id {} does not exist".format(trip_leader_id, trip_id))
    c.execute("DELETE FROM trip_preferences WHERE trip_leader_id=? AND trip_id=?", (trip_leader_id, trip_id))
    conn.commit()
    conn.close()
    return "Success!"
