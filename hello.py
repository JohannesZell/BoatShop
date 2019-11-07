from flask import Flask, send_from_directory
import os
app = Flask(__name__)

port = int(os.getenv('PORT', 8000))

@app.route('/')
def root():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    #app.run()
    app.run(host='0.0.0.0', port=port, debug=True)
    print( "Hello World")
