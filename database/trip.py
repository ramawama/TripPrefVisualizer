import sqlite3
import trip_preference

# conn=sqlite3.connect('./trip.db')
# c=conn.cursor()
# # Create the table trip.db with appropriate columns; no need to create again
# c.execute("""
#     CREATE TABLE trip (
#         trip_id INTEGER PRIMARY KEY,
#         name TEXT,
#         category TEXT CHECK(category IN ('Overnight', 'Mountain Biking', 'Spelunking', 'Watersports', 'Surfing', 'Sea Kayaking')),
#         start_date TEXT,
#         end_date TEXT,
#         lead_guides_needed INTEGER,
#         total_guides_needed INTEGER
#     )
# """)
# conn.commit()
# conn.close()

# Insert a record into the trip table; test
# c.execute("INSERT INTO trip VALUES (1, 'Overnight', '2021-09-01', '2021-09-03', 2, 4)")

def check_parapmeter_validity(id, name, category, start_date, end_date, lead_guides_needed, total_guides_needed):
    if not isinstance(id, int):
        return ("Error: id must be an integer")
    if not isinstance(name, str):
        return ("Error: name must be a string")
    if not isinstance(category, str):
        return ("Error: category must be a string") 
    if not is_trip_type(category):
        return ("Error: category must be one of the following: 'Overnight', 'Mountain Biking', 'Spelunking', 'Watersports', 'Surfing', 'Sea Kayaking', 'Other'")
    if not isinstance(start_date, str):
        return ("Error: start_date must be a string")
    if not isinstance(end_date, str):
        return ("Error: end_date must be a string")
    if not isinstance(lead_guides_needed, int):
        return ("Error: lead_guides_needed must be an integer")
    if not isinstance(total_guides_needed, int):
        return ("Error: total_guides_needed must be an integer")
    return True

def create_trip(id, name, category, start_date, end_date, lead_guides_needed, total_guides_needed):
    
    msg = check_parapmeter_validity(id, name, category, start_date, end_date, lead_guides_needed, total_guides_needed)
    if msg != True:
        return msg
    
    conn=sqlite3.connect('./trip.db')
    c=conn.cursor()
    c.execute("SELECT * FROM trip WHERE trip_id=?", (id,))
    if c.fetchone() is not None:
        return ("Error: id must be unique")
    
    #everything is checked, unlikely a fail
    try:
        c.execute("INSERT INTO trip VALUES (?, ?, ?, ?, ?, ?, ?)", (id, name, category, start_date, end_date, lead_guides_needed, total_guides_needed))
    except sqlite3.IntegrityError as e:
        return ("Error: ", e)
    
    conn.commit()
    conn.close()
    return "Success!"

#questionable: how should we return an error message?
def get_trip_by_id(id):
    conn=sqlite3.connect('./trip.db')
    c=conn.cursor()
    if not isinstance(id, int):
        return ("Error: id must be an integer")
    try:
        c.execute("SELECT * FROM trip WHERE trip_id=?", (id,))
    except sqlite3.IntegrityError as e:
        return ("Error: ", e)
    result = c.fetchone()
    conn.close()
    return result


def update_trip(id, name, category, start_date, end_date, lead_guides_needed, total_guides_needed):
    msg = check_parapmeter_validity(id, name, category, start_date, end_date, lead_guides_needed, total_guides_needed)
    if msg != True:
        return msg
    
    conn=sqlite3.connect('./trip.db')
    c=conn.cursor()
    
    c.execute("SELECT * FROM trip WHERE trip_id=?", (id,))
    if c.fetchone() is None:
        return ("Trip with id {} does not exist".format(id))
    try:
        c.execute("UPDATE trip SET name=?, category=?, start_date=?, end_date=?, lead_guides_needed=?, total_guides_needed=? WHERE trip_id=?", (name, category, start_date, end_date, lead_guides_needed, total_guides_needed, id))
    except sqlite3.InterfaceError as e:
        return ("Error:", e)
    conn.commit()
    conn.close()
    return "Success!"

def get_all_trips():
    conn=sqlite3.connect('./trip.db')
    c=conn.cursor()
    c.execute("SELECT * FROM trip")
    records = c.fetchall()
    conn.close()
    return records

def delete_trip(id):
    conn=sqlite3.connect('./trip.db')
    c=conn.cursor()
    if not isinstance(id, int):
        return ("Error: id must be an integer")
    c.execute("SELECT * FROM trip WHERE trip_id=?", (id,))
    if c.fetchone() is None:
        return ("Trip with id {} does not exist".format(id))
    c.execute("DELETE FROM trip WHERE trip_id=?", (id,))
    conn.commit()
    conn.close()
    trip_preference.delete_associations_by_trip_id(id)
    return "Success!"


def is_trip_type(category):
    if category not in ['Overnight', 'Mountain Biking', 'Spelunking', 'Watersports', 'Surfing', 'Sea Kayaking', 'Other']:
        return False
    return True

def delete_all_trips():
    conn=sqlite3.connect('./trip.db')
    c=conn.cursor()
    c.execute("DELETE FROM trip")
    conn.commit()
    conn.close()
    trip_preference.delete_all_trip_preferences()
    return "Success!"

#delete_all_trips()