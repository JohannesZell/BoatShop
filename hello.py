from flask import Flask, send_from_directory, jsonify
import os
import json
app = Flask(__name__)

port = int(os.getenv('PORT', 8000))
boat = {}

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
    # jsonBoat = open('JSONobjects.json')
    # jsonBoatStr = jsonBoat.read()
    # boatData = json.loads(jsonBoatStr)
    # for key in boatData:
    #     print(key["id"])
    #     id = key["id"]
    #     for value in key.items():
    #         print(boatData[id-1]["name"])
    app.run(host='0.0.0.0', port=port, debug=True)