from flask import Flask, jsonify
import datetime
import socket


app = Flask(__name__)

@app.route('/api/v1/info')

def info():
    return jsonify({
    	'time': datetime.datetime.now().strftime("%I:%M:%S%p  on %B %d, %Y"),
    	'hostname': socket.gethostname(),
        'message': 'You are doing great, little human! GitHup Runners. <3',
        'deployed_on': 'kubernetes, using ArgoCD 6'
    })


@app.route('/api/v1/health')
def health():
    return jsonify({'status': 'up'}), 200

# main driver function
if __name__ == '__main__':
        app.run(host="0.0.0.0")

