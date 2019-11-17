from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import os
import json
app = Flask(__name__)
#CORS(app)
port = int(os.getenv('PORT', 8000)) 

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/getBoats')
def getBoats():
    jsonBoat = open('JSONobjects.json')
    jsonBoatStr = jsonBoat.read()
    boatData = json.loads(jsonBoatStr)
    print(boatData)
    return jsonify(boatData)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
