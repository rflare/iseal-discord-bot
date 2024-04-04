from flask import Flask, request, jsonify
import subprocess
import os
import signal
import sys

app = Flask(__name__)

@app.route('/Iseal-Discord-Bot', methods=['POST'])
def handle_webhook():
    try:
        payload = request.json
        if 'ref' in payload and payload['ref'] == 'refs/heads/master':
            print("Received a push to the master branch. Fetching latest code...")
            subprocess.run(['git', 'pull'])
            print("Code fetched successfully!")
            jsonify({'message': 'Webhook received, code fetched, and script restarted!'})
            return os.execv(sys.executable, ['python', '~/src/main.py'] + sys.argv)
        else:
            return jsonify({'message': 'Ignoring non-master branch push event.'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

os.execv(sys.executable, ['python', '~/src/main.py'])