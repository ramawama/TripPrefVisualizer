
from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
import json
import os
import pandas as pd
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


UPLOAD_FOLDER = '/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def file_upload():
    uploaded_filenames = []  # List to store names of uploaded files

    for key in request.files.keys():
        files = request.files.getlist(key)
        for file in files:
            if file.filename == '':
                return 'No selected file', 400
            filename = secure_filename(file.filename)
            print(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            uploaded_filenames.append(filename)  # Add the filename to the list

    if not uploaded_filenames:  # Check if no files were uploaded
        return 'No files uploaded', 400

    return jsonify({'files': uploaded_filenames}), 200


if __name__ == '__main__':
    app.run(debug=True)


# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/post', methods=['POST'])
# def upload_files():
#     if request.method == 'POST':
#         uploaded_files = []
#         for file in request.files.getlist('file'):
#             filename = secure_filename(file.filename)
#             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
#             uploaded_files.append({
#                 'filename': filename,
#                 'url': f"http://localhost:5000/{app.config['UPLOAD_FOLDER']}/{filename}"
#             })
#         return jsonify({'files': uploaded_files}), 200
#     else:
#         return "Method not allowed", 405
# # returning json of this structure: 
# # {
# #   "files": [
# #     {
# #       "filename": "example_file.xlsx",
# #       "url": "/uploads/example_file.xlsx"
# #     },
# #     {
# #       "filename": "another_file.xls",
# #       "url": "/uploads/another_file.xls"
# #     }
# #     // Other uploaded files follow the same structure
# #   ]
# # }
