from flask import Flask, jsonify
import datetime
import socket


app = Flask(__name__)

@app.route('/api/v1/customerinfo')

def customerinfo():
    return jsonify({'TraceID' : 1234567, 'message' : 'Transaction Successfull'}), 200

@app.route('/api/v1/healthz')
def health():
    return jsonify({
        'Time' : datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"), 
        'Hostname' : socket.gethostname(),
        'message' : 'Transaction Fail'}), 404

# main driver function
if __name__ == '__main__':
        app.run(host="0.0.0.0")

