import sqlite3

# create table to input into; no need anymore, file created
# uses linking table: id to big table to individuals connective tables

# visualize through https://inloop.github.io/sqlite-viewer/

# conn=sqlite3.connect('./database/trip_leader.db')
# c=conn.cursor()
# c.execute("""
#         CREATE TABLE trip_leaders (
#             id INTEGER PRIMARY KEY,
#             name TEXT,
#             class_year INTEGER,
#             semesters_left INTEGER,
#             reliability_score INTEGER,
#             num_trips_assigned INTEGER,
#             preferred_co_leaders TEXT,
#             overnight_role TEXT CHECK(category IN ('Lead', 'Assistant')),
#             mountain_biking_role TEXT CHECK(category IN ('Lead', 'Assistant')),
#             spelunking_role TEXT CHECK(category IN ('Lead', 'Assistant')),
#             watersports_role TEXT CHECK(category IN ('Lead', 'Assistant')),
#             surfing_role TEXT CHECK(category IN ('Lead', 'Assistant')),
#             sea_kayaking_role TEXT CHECK(category IN ('Lead', 'Assistant'))
#         )""") 
# conn.commit()
# conn.close()


def valid_ufid(ufid):
    if not isinstance(ufid, int):
        return False
    if len(ufid) != 8:
        return False
    return True

def check_leader_parapmeter_validity(ufid, name, class_year, semesters_left, reliability_score, num_trips_assigned, overnight_role, mountain_biking_role, spelunking_role, watersports_role, surfing_role, sea_kayaking_role):
    if not valid_ufid(ufid):
        return ("Error: improper UFID format")
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
    if not isinstance(overnight_role, str):
        return ("Error: overnight_role must be a string, either 'Lead' or 'Assistant'")
    if not isinstance(mountain_biking_role, str):
        return ("Error: mountain_biking_role must be a string, either 'Lead' or 'Assistant'")
    if not isinstance(spelunking_role, str):
        return ("Error: spelunking_role must be a string, either 'Lead' or 'Assistant'")
    if not isinstance(watersports_role, str):
        return ("Error: watersports_role must be a string, either 'Lead' or 'Assistant'")
    if not isinstance(surfing_role, str):
        return ("Error: surfing_role must be a string, either 'Lead' or 'Assistant'")
    if not isinstance(sea_kayaking_role, str):
        return ("Error: sea_kayaking_role must be a string, either 'Lead' or 'Assistant'")
    
    return True

def create_leader(ufid, name, class_year, semesters_left, reliability_score, num_trips_assigned, overnight_role, mountain_biking_role, spelunking_role, watersports_role, surfing_role, sea_kayaking_role):
    msg = check_leader_parapmeter_validity(ufid, name, class_year, semesters_left, reliability_score, num_trips_assigned, overnight_role, mountain_biking_role, spelunking_role, watersports_role, surfing_role, sea_kayaking_role)

    if msg != True:
        return msg
    
    conn=sqlite3.connect('./database/trip_leader.db')
    c=conn.cursor()
    c.execute("SELECT * FROM trip_leaders WHERE name=?", (name,))
    if c.fetchone() is not None:
        return ("Error: name must be unique")
    
    #everything is checked, unlikely a fail
    try:
        c.execute("INSERT INTO trip_leaders VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (ufid, name, class_year, semesters_left, reliability_score, num_trips_assigned, overnight_role, mountain_biking_role, spelunking_role, watersports_role, surfing_role, sea_kayaking_role))
    except sqlite3.IntegrityError as e:
        return ("Error: ", e)
    
    conn.commit()
    conn.close()
    return "Success!"


def delete_leader_by_ufid(ufid):
    conn=sqlite3.connect('./database/trip_leader.db')
    c=conn.cursor()
    c.execute("SELECT * FROM trip_leaders WHERE ufid=?", (ufid,))
    if c.fetchone() is None:
        return ("Error: ufid does not exist")
    c.execute("DELETE FROM trip_leaders WHERE ufid=?", (ufid,))

    # *delete all references to this leader in the linking table

    conn.commit()
    conn.close()
    return "Success!"

def delete_leader_by_name(name):
    conn=sqlite3.connect('./database/trip_leader.db')
    c=conn.cursor()
    c.execute("SELECT * FROM trip_leaders WHERE name=?", (name,))
    if c.fetchone() is None:
        return ("Error: name does not exist")
    c.execute("DELETE FROM trip_leaders WHERE name=?", (name,))

    # *delete all references to this leader in the linking table

    conn.commit()
    conn.close()
    return "Success!"

def update_leader_by_ufid(ufid, name, class_year, semesters_left, reliability_score, num_trips_assigned, overnight_role, mountain_biking_role, spelunking_role, watersports_role, surfing_role, sea_kayaking_role):
    msg = check_leader_parapmeter_validity(ufid, name, class_year, semesters_left, reliability_score, num_trips_assigned, overnight_role, mountain_biking_role, spelunking_role, watersports_role, surfing_role, sea_kayaking_role)
    if msg != True:
        return msg
    
    conn=sqlite3.connect('./database/trip_leader.db')
    c=conn.cursor()
    
    c.execute("SELECT * FROM trip_leaders WHERE ufid=?", (ufid,))
    if c.fetchone() is None:
        return ("Leader with ufid {} does not exist".format(ufid))
    try:
        c.execute("UPDATE trip_leaders SET name=?, class_year=?, semesters_left=?, reliability_score=?, num_trips_assigned=?, overnight_role=?, mountain_biking_role=?, spelunking_role=?, watersports_role=?, surfing_role=?, sea_kayaking_role=?, WHERE ufid=?", (name, class_year, semesters_left, reliability_score, num_trips_assigned, overnight_role, mountain_biking_role, spelunking_role, watersports_role, surfing_role, sea_kayaking_role, ufid))
    except sqlite3.IntegrityError as e:
        return ("Error: ", e)
    conn.commit()
    conn.close()
    return "Success!"

def update_leader_by_name(ufid, name, class_year, semesters_left, reliability_score, num_trips_assigned, overnight_role, mountain_biking_role, spelunking_role, watersports_role, surfing_role, sea_kayaking_role):
    msg = check_leader_parapmeter_validity(ufid, name, class_year, semesters_left, reliability_score, num_trips_assigned, overnight_role, mountain_biking_role, spelunking_role, watersports_role, surfing_role, sea_kayaking_role)
    if msg != True:
        return msg
    
    conn=sqlite3.connect('./database/trip_leader.db')
    c=conn.cursor()
    
    c.execute("SELECT * FROM trip_leaders WHERE name=?", (name,))
    if c.fetchone() is None:
        return ("Leader with name {} does not exist".format(name))
    try:
        c.execute("UPDATE trip_leaders SET ufid=?, class_year=?, semesters_left=?, reliability_score=?, num_trips_assigned=?, overnight_role=?, mountain_biking_role=?, spelunking_role=?, watersports_role=?, surfing_role=?, sea_kayaking_role=?, WHERE name=?", (ufid, class_year, semesters_left, reliability_score, num_trips_assigned, overnight_role, mountain_biking_role, spelunking_role, watersports_role, surfing_role, sea_kayaking_role, name))
    except sqlite3.IntegrityError as e:
        return ("Error: ", e)
    conn.commit()
    conn.close()
    return "Success!"

def get_leader_by_name(name):
    conn=sqlite3.connect('./database/trip_leader.db')
    c=conn.cursor()
    if not isinstance(name, str):
        return ("Error: name must be a string")
    try:
        c.execute("SELECT * FROM trip_leaders WHERE name=?", (name,))
    except sqlite3.IntegrityError as e:
        return ("Error: ", e)
    result = c.fetchone()
    conn.close()
    return result

def get_leader_by_ufid(ufid):
    conn=sqlite3.connect('./database/trip_leader.db')
    c=conn.cursor()
    if not isinstance(ufid, int):
        return ("Error: ufid must be a integer")
    try:
        c.execute("SELECT * FROM trip_leaders WHERE ufid=?", (ufid,))
    except sqlite3.IntegrityError as e:
        return ("Error: ", e)
    result = c.fetchone()
    conn.close()
    return result


