
from flask import Flask, jsonify, request
from flask_cors import CORS
import sys
from database.trip_leader import get_leader_by_ufid, update_leader_by_ufid, delete_leader_by_ufid
from database.trip import get_trip_by_id
import sqlite3
import json
import os
import re
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

def query_db_to_json(db_path, table_name):
    # Construct the path to the database directory
    #database_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'database')
    #db_path = os.path.join(database_dir, db_filename)
    
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
        'database/trip_leader.db': 'trip_leaders',
        'database/trip_preference.db': 'trip_preferences',
        'database/trip.db': 'trip'
    }
    
    # Dictionary to hold data from all databases
    all_data = {}
    
    for db_filename, table_name in db_table_mappings.items():
        data = query_db_to_json(db_filename, table_name)
        match = re.search(r'/([^/.]+)\.', db_filename)
        key_name = match.group(1)
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
    ufID = data.get('tripLeaderSelect', '')
    ufID = int(ufID)
    tripID = data.get('tripSelect', '')
    if(ufID != 'Trip ID'):
        # ufID is not the default value
        old_leader_info = get_leader_by_ufid(ufID)
        name = old_leader_info[1]
        class_year = data.get('Class year', '')
        if(class_year == ''):
            class_year = old_leader_info[2]
        else:
            class_year = int(class_year)
        semesters_left = data.get('Semesters Left', '')
        if(semesters_left == ''):
            semesters_left = old_leader_info[3]
        reliability_score = old_leader_info[4]
        number_of_trips_assigned = data.get('Number of Trips Assigned', '')
        if(number_of_trips_assigned == ''): 
            number_of_trips_assigned = old_leader_info[5]
        else:
            int(number_of_trips_assigned)
        co_lead1 = data.get('coLead1', '')
        if(co_lead1 == '1st Preferred Co-Lead'):
            co_lead1 = ''
        co_lead2 = data.get('coLead2', '')
        if(co_lead2 == '2nd Preferred Co-Lead'):
            co_lead2 = ''
        co_lead3 = data.get('coLead3', '')
        if(co_lead3 == '3rd Preferred Co-Lead'):
            co_lead3 = ''
        co_leads = [co_lead1, co_lead2, co_lead3]
        co_leads = [co_lead for co_lead in co_leads if co_lead] # Remove empty strings from the list
        if(not co_leads):
            co_leads = old_leader_info[6]
        else:
            co_leads = json.dumps(co_leads)
        overnight_leader_status = data.get('overnightLeaderStatus', '')
        if(overnight_leader_status == 'Overnight Status'): 
            overnight_leader_status = old_leader_info[7]
        biking_leader_status = data.get('bikingLeaderStatus', '')
        if(biking_leader_status == 'Biking Status'):
            biking_leader_status = old_leader_info[8]
        spelunking_leader_status = data.get('spelunkingLeaderStatus', '')
        if(spelunking_leader_status == 'Spelunking Status'):
            spelunking_leader_status = old_leader_info[9]
        watersports_leader_status = data.get('watersportsLeaderStatus', '')
        if(watersports_leader_status == 'Watersports Status'):
            watersports_leader_status = old_leader_info[10]
        surfing_leader_status = data.get('surfingLeaderStatus', '')
        if(surfing_leader_status == 'Surfing Status'):
            surfing_leader_status = old_leader_info[11]
        sea_kayaking_leader_status = data.get('seaKayakingLeaderStatus', '')
        if(sea_kayaking_leader_status == 'Sea Kayaking Status'):
            sea_kayaking_leader_status = old_leader_info[12]
        print(update_leader_by_ufid(ufID, name, class_year, semesters_left, reliability_score,number_of_trips_assigned, co_leads, overnight_leader_status, biking_leader_status, spelunking_leader_status, watersports_leader_status, surfing_leader_status, sea_kayaking_leader_status))
        #delete_leader_by_ufid(ufID)
        
    if(tripID != 'Trip ID'):
        category_select = data.get('categorySelect', '')
        end_date_year = data.get('End Date Year', '')
        end_day = data.get('End Day', '')
        end_month = data.get('End Month', '')
        lead_guides_needed = data.get('leadGuidesNeeded', '')
        start_date_year = data.get('Start Date Year', '')
        start_day = data.get('Start Day', '')
        start_month = data.get('Start Month', '')
        total_guides_needed = data.get('totalGuidesNeeded', '')
        trip_name = data.get('Trip Name', '')

    # print(oldLeaderInfo)
    # print(oldTripInfo)
    # update_leader_by_ufid(ufid, name, class_year, semesters_left, reliability_score, num_trips_assigned, preferred_co_leaders, overnight_role, mountain_biking_role, spelunking_role, watersports_role, surfing_role, sea_kayaking_role)
    
    return jsonify({"message": "Data received successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
