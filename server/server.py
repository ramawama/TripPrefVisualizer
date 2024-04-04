
from flask import Flask, jsonify, request
from flask_cors import CORS
import sys
sys.path.append('C:/Users/shume/Documents/GitHub/TripPrefVisualizer/database')
import trip_leader
import trip
import sqlite3
import json
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

def query_db_to_json(db_filename, table_name):
    # Construct the path to the database directory
    database_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'database')
    db_path = os.path.join(database_dir, db_filename)
    
    # Connect to the SQLite database using the full path
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Construct and execute the SQL query
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    
    # Fetch all rows from the query
    rows = cursor.fetchall()
    
    # Get column names from the cursor description
    columns = [description[0] for description in cursor.description]
    
    # Convert query results to a list of dictionaries
    results = [dict(zip(columns, row)) for row in rows]
    
    # Close the connection
    conn.close()
    
    return results

@app.route('/get-data', methods=['GET'])
def get_data():
    # Map of database paths to their respective table names
    db_table_mappings = {
        'trip_leader.db': 'trip_leaders',
        'trip_preference.db': 'trip_preferences',
        'trip.db': 'trip'
    }
    
    # Dictionary to hold data from all databases
    all_data = {}
    
    for db_filename, table_name in db_table_mappings.items():
        data = query_db_to_json(db_filename, table_name)
        key_name = db_filename.split('.')[0]
        all_data[key_name] = data
    
    return jsonify(all_data)


# @app.route("/test", methods=['GET'])
# def return_test():
#     table_data = [ # This is a list of dictionaries, we will call in the preferences later after they are set
#         {
#             "id": 1,
#             "name": "Aaron",
#             "status": "Lead Guide",
#             "trip": "Mtb biking"
#         },
#         {
#             "id": 2,
#             "name": "Rama",
#             "status": "Lead Guide",
#             "trip": "Spelunking"
#         }
#     ]
#     return jsonify({
#         'Msg': "Test Table Data",
#         'data': table_data
#     })

@app.route("/schedules/test", methods=['GET'])
def return_test():
    table_data = [ # This is a list of dictionaries, we will call in the preferences later after they are set
        {
            "id": 1,
            "name": "Aaron",
            "status": "Lead Guide",
            "trip": "Mtb biking"
        },
        {
            "id": 2,
            "name": "Rama",
            "status": "Lead Guide",
            "trip": "Spelunking"
        }
    ]
    return jsonify({
        'Msg': "Test Table Data",
        'data': table_data
    })

# may or may not send uploaded files to the back end
app.config['UPLOAD_FOLDER'] = './uploads'

@app.route("/", methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        # check if the required files are present in the request
        if 'guide_file' not in request.files or 'trip_pref_files[]' not in request.files:
            return jsonify({'error': 'Files not provided in request'}), 400

        guide_file = request.files['guide_file']
        trip_pref_files = request.files.getlist('trip_pref_files[]')

        # save the uploaded files
        guide_filename = secure_filename(guide_file.filename)
        guide_file.save(os.path.join(app.config['UPLOAD_FOLDER'], guide_filename))

        for index, trip_pref_file in enumerate(trip_pref_files):
            trip_pref_filename = secure_filename(trip_pref_file.filename)
            trip_pref_file.save(os.path.join(app.config['UPLOAD_FOLDER'], trip_pref_filename))

        return jsonify({'success': 'Files uploaded successfully'}), 200

    return "Hello, please upload files."

@app.route('/api/modifyLeader', methods=['POST'])
def updateLeaderAndTrip():
    # Parse JSON data sent to the endpoint
    data = request.get_json()
    
    # Assign each piece of data to a variable
    biking_leader_status = data.get('bikingLeaderStatus', '')
    category_select = data.get('categorySelect', '')
    class_year = data.get('Class year', '')
    co_lead1 = data.get('coLead1', '')
    co_lead2 = data.get('coLead2', '')
    co_lead3 = data.get('coLead3', '')
    end_date_year = data.get('End Date Year', '')
    end_day = data.get('End Day', '')
    end_month = data.get('End Month', '')
    lead_guides_needed = data.get('leadGuidesNeeded', '')
    number_of_trips_assigned = data.get('Number of Trips Assigned', '')
    overnight_leader_status = data.get('overnightLeaderStatus', '')
    sea_kayaking_leader_status = data.get('seaKayakingLeaderStatus', '')
    semesters_left = data.get('Semesters Left', '')
    spelunking_leader_status = data.get('spelunkingLeaderStatus', '')
    start_date_year = data.get('Start Date Year', '')
    start_day = data.get('Start Day', '')
    start_month = data.get('Start Month', '')
    surfing_leader_status = data.get('surfingLeaderStatus', '')
    total_guides_needed = data.get('totalGuidesNeeded', '')
    trip_name = data.get('Trip Name', '')
    trip_leader_select = data.get('tripLeaderSelect', '')
    trip_select = data.get('tripSelect', '')
    watersports_leader_status = data.get('watersportsLeaderStatus', '')

    print(trip_leader_select)
    trip_leader.get_leader_by_ufid(trip_leader_select)
    # oldTripInfo = trip.get_trip_by_id(trip_select)
    # print(oldLeaderInfo)
    # print(oldTripInfo)
    #trip_leader.update_leader_by_ufid(ufid, name, class_year, semesters_left, reliability_score, num_trips_assigned, preferred_co_leaders, overnight_role, mountain_biking_role, spelunking_role, watersports_role, surfing_role, sea_kayaking_role)
    return jsonify({"message": "Data received successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
