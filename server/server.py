from flask import Flask, jsonify

# creating app instance
app = Flask(__name__)


# route setup for /api/home
@app.route("/api/home", methods = {'GET'})
def return_home():
    return jsonify({
        'message' : "Hello world!"
    })

if __name__ == "__main__":
    app.run(debug=True) # remove when deploy to prod