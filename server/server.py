import subprocess  # For running external commands

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


# @app.route('/upload-path', methods=['POST', 'OPTIONS'])
# def receive_path():
#     if request.method == "OPTIONS":  #for preflight error
#         return '', 200

#     file_path = request.json['filePath']
#     print(f"Received file path: {file_path}")

#     try:
#         subprocess.run(['python', 'infoFilter.py'])
#         return jsonify({'success': 'infoFilter.py executed successfully'}), 200
#     except Exception as e:
#         return jsonify({'error': f'Error running infoFilter.py: {str(e)}'}), 500

#     return jsonify({'success': 'infoFilter.py executed successfully'}), 200

#     # return "Path received"

@app.route('/upload-path', methods=['POST', 'OPTIONS'])
def receive_path():
    if request.method == "OPTIONS":
        return '', 200

    file_path = request.json['filePath']
    print(f"Received file path: {file_path}")

    try:
        # Construct the relative path to the script
        current_dir = os.path.dirname(__file__)  # Gets the directory of the current script
        parent_dir = os.path.join(current_dir, '..')  # Move up to the parent directory
        script_directory = os.path.normpath(os.path.join(parent_dir, 'database'))
        script_path = os.path.join(script_directory, 'infoFilter.py')

        # Run the Python script with the provided file path from the specified directory
        result = subprocess.run(['python', script_path, file_path], cwd=script_directory, text=True, capture_output=True)
        print(f"stdout: {result.stdout}")
        print(f"stderr: {result.stderr}")

        if result.returncode != 0:
            raise Exception('infoFilter.py failed to run')

        print(f"Running: {file_path}")
        return jsonify({'success': 'infoFilter.py executed successfully', 'output': result.stdout}), 200
    except Exception as e:
        print(f"Not Running: {file_path}, Error: {e}")
        return jsonify({'error': f'Error running infoFilter.py: {str(e)}'}), 500


# @app.route('/upload-path', methods=['GET', 'OPTIONS'])
# def receive_path():
#     if request.method == "OPTIONS":  # Allow preflight checks for CORS
#         return '', 200

#     # Access the file path from the query string
#     file_path = request.args.get('filePath')
#     if not file_path:
#         return "No file path provided", 400

#     print(f"Received file path: {file_path}")
#     return f"Path received: {file_path}"


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
