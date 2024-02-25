import sqlite3

# conn=sqlite3.connect('./database/trip_preference.db')
# c=conn.cursor()

# c.execute("""
#         CREATE TABLE trip_preferences (
#             trip_leader_id INTEGER,
#             trip_id INTEGER,
#             preference INTEGER CHECK (preference IN (0, 1, 2, 3, 4, 5)),
#             PRIMARY KEY(trip_leader_id, trip_id)
#         )""")

# conn.commit()
# conn.close()