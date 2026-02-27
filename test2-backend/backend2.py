from flask import Flask, jsonify
from flask_cors import CORS # This allows the frontend to talk to the backend

app = Flask(__name__)
CORS(app) # Crucial for GitHub Pages to access this API

@app.route('/api/data')
def get_data():
    return jsonify({"message": "Hello from the Python backend!"})

if __name__ == '__main__':
    app.run()
