from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/analytics", methods=['GET'])
def return_home():
    return jsonify({
        'Trips': "Mtb biking!"
    })

if __name__ == "__main__":
    app.run(debug=True)