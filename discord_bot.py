from flask import Flask, request, jsonify
from threading import Thread
import subprocess
import os
import sys

app = Flask(__name__)

def run_discord_bot():
    import src.main
    pass

@app.route('/Iseal-Discord-Bot', methods=['POST'])
def handle_webhook():
    try:
        payload = request.json
        if 'ref' in payload and payload['ref'] == 'refs/heads/master':
            print("Received a push to the master branch. Fetching latest code...")
            subprocess.run(['git', 'pull'])
            print("Code fetched successfully!")

            # Restart the script
            os.execv(sys.executable, ['python'] + sys.argv)

    except Exception as e:
        return jsonify({'error': str(e)})
    return jsonify({'message': 'success'})

if __name__ == '__main__':
    # Start the discord bot in a separate thread
    bot_thread = Thread(target=run_discord_bot)
    bot_thread.start()

    # Start the server
    app.run(host='0.0.0.0', port=8080)