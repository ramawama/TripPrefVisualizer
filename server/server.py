
from flask import Flask, jsonify
from flask_cors import CORS
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


@app.route('/generate-schedule', methods=['GET'])
def get_schedule_data():
    # Database filename and table name
    db_filename = 'schedule.db'
    table_name = 'schedule'
    
    # Retrieve data from the specified database and table
    data = query_db_to_json(db_filename, table_name)
    
    # Prepare the response
    response = {table_name: data}
    
    return jsonify(response)


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

if __name__ == "__main__":
    app.run(debug=True)
