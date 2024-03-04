from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/analytics", methods=['GET'])
def return_home():
    return jsonify({
        'Trips': "Mtb biking!"
    })

@app.route("/", methods=['GET'])
def return_hello():
    return jsonify({
        'Msg': "Hello World!"
    })

@app.route("/test", methods=['GET'])
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

if __name__ == "__main__":
    app.run(debug=True)