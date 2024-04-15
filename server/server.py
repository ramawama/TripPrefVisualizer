
from flask import Flask, jsonify, request
import sys
import os
from flask_cors import CORS
import sqlite3
import json
from werkzeug.utils import secure_filename

app = Flask(__name__)
CORS(app)

current_dir = os.path.dirname(os.path.abspath(__file__))
root_dir=os.path.dirname(current_dir)
database_files_dir=os.path.join(root_dir, 'database')
sys.path.append(database_files_dir)

#import schedule
import trip
import trip_leader
#import trip_preference
#import infoFilter

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
    promotion_status_map = {
        "Lead Guide": "Lead",
        "Interested in Promotion": "Promotion",
        "Not Interested in Promotion": "None"
    }
    
    # Assign each piece of data to a variable
    ufID = data.get('tripLeaderSelect', '')
    tripID = data.get('tripSelect', '')
    if(ufID != 'Trip Leader Name'):
        ufID = int(ufID)
        old_leader_info = trip_leader.get_leader_by_ufid(ufID)
        name = old_leader_info[1]
        class_year = data.get('Class year', '')
        if(class_year == ''):
            class_year = old_leader_info[2]
        else:
            class_year = int(class_year)
        semesters_left = data.get('Semesters Left', '')
        if(semesters_left == ''):
            semesters_left = old_leader_info[3]
        else:
            semesters_left = int(semesters_left)
        reliability_score = old_leader_info[4]
        number_of_trips_assigned = data.get('Number of Trips Assigned', '')
        if(number_of_trips_assigned == ''): 
            number_of_trips_assigned = old_leader_info[5]
        else:
           number_of_trips_assigned = int(number_of_trips_assigned)
        co_lead1 = data.get('coLead1', '')
        if(co_lead1 == '1st Preferred Co-Lead'):
            co_lead1 = ''
        else:
            co_lead1Array = trip_leader.get_leader_by_ufid(int(co_lead1))
            co_lead1 = co_lead1Array[1]
        co_lead2 = data.get('coLead2', '')
        if(co_lead2 == '2nd Preferred Co-Lead'):
            co_lead2 = ''
        else:
            co_lead2Array = trip_leader.get_leader_by_ufid(int(co_lead2))
            co_lead2 = co_lead2Array[1]
        co_lead3 = data.get('coLead3', '')
        if(co_lead3 == '3rd Preferred Co-Lead'):
            co_lead3 = ''
        else:
            co_lead3Array = trip_leader.get_leader_by_ufid(int(co_lead3))
            co_lead3 = co_lead3Array[1]
        co_leads = [co_lead1, co_lead2, co_lead3]
        co_leads = [co_lead for co_lead in co_leads if co_lead] # Remove empty strings from the list
        if(not co_leads):
            co_leads = old_leader_info[6]
        else:
            co_leads = json.dumps(co_leads)
        overnight_leader_status = data.get('overnightLeaderStatus', '')
        if(overnight_leader_status == 'Overnight Status'): 
            overnight_leader_status = old_leader_info[7]
        else:
            overnight_leader_status = promotion_status_map[overnight_leader_status]
        biking_leader_status = data.get('bikingLeaderStatus', '')
        if(biking_leader_status == 'Biking Status'):
            biking_leader_status = old_leader_info[8]
        else:
            biking_leader_status = promotion_status_map[biking_leader_status]
        spelunking_leader_status = data.get('spelunkingLeaderStatus', '')
        if(spelunking_leader_status == 'Spelunking Status'):
            spelunking_leader_status = old_leader_info[9]
        else:
            spelunking_leader_status = promotion_status_map[spelunking_leader_status]
        watersports_leader_status = data.get('watersportsLeaderStatus', '')
        if(watersports_leader_status == 'Watersports Status'):
            watersports_leader_status = old_leader_info[10]
        else:
            watersports_leader_status = promotion_status_map[watersports_leader_status]
        surfing_leader_status = data.get('surfingLeaderStatus', '')
        if(surfing_leader_status == 'Surfing Status'):
            surfing_leader_status = old_leader_info[11]
        else:
            surfing_leader_status = promotion_status_map[surfing_leader_status]
        sea_kayaking_leader_status = data.get('seaKayakingLeaderStatus', '')
        if(sea_kayaking_leader_status == 'Sea Kayaking Status'):
            sea_kayaking_leader_status = old_leader_info[12]
        else:
            sea_kayaking_leader_status = promotion_status_map[sea_kayaking_leader_status]
        print(trip_leader.update_leader_by_ufid(ufID, name, class_year, semesters_left, reliability_score,number_of_trips_assigned, co_leads, overnight_leader_status, biking_leader_status, spelunking_leader_status, watersports_leader_status, surfing_leader_status, sea_kayaking_leader_status))
        
    if(tripID != 'Trip ID'):
        tripID = int(tripID)
        old_trip_info = trip.get_trip_by_id(tripID)
        trip_name = data.get('Trip Name', '')
        if(trip_name == ''):
            trip_name = old_trip_info[1]
        category_select = data.get('categorySelect', '')
        if(category_select == 'Trip Category'):
            category_select = old_trip_info[2]
        start_date_year = data.get('Start Date Year', '')
        start_day = data.get('Start Day', '')
        start_month = data.get('Start Month', '')
        if(start_date_year == '' or start_day == '' or start_month == ''):
            start_date = old_trip_info[4]
        else:
            start_date = f"{start_date_year}-{start_month}-{start_day}"
        end_date_year = data.get('End Date Year', '')
        end_day = data.get('End Day', '')
        end_month = data.get('End Month', '')
        if(end_date_year == '' or end_day == '' or end_month == ''):
            end_date = old_trip_info[3]
        else:
            end_date = f"{end_date_year}-{end_month}-{end_day}"
        lead_guides_needed = data.get('leadGuidesNeeded', '')
        if(lead_guides_needed == '# of Lead Guides'):
            lead_guides_needed = old_trip_info[5]
        else:
            lead_guides_needed = int(lead_guides_needed)
        total_guides_needed = data.get('totalGuidesNeeded', '')
        if(total_guides_needed == '# of Total Guides'):
            total_guides_needed = old_trip_info[6]
        else:
            total_guides_needed = int(total_guides_needed)
        print(trip.update_trip(tripID, trip_name, category_select, start_date, end_date, lead_guides_needed, total_guides_needed))
    
    return jsonify({"Message": "Data received successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
