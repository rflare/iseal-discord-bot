from flask import Flask, request, jsonify
from threading import Thread
import subprocess
import os
import sys
from src.main import stop
app = Flask(__name__)

def run_discord_bot():
    import src.main
    pass

@app.route('/Iseal-Discord-Bot', methods=['POST'])
def handle_webhook():
    try:
        # Pull changes from git
            subprocess.run(['git', 'pull'])
        # Stop the bot
            stop()
        # Signals watcher to restart script
            with open('restart.txt', 'w') as f:
                f.write('restart')
                f.close()

    except Exception as e:
        return jsonify({'error': str(e)})
    return jsonify({'message': 'success'})

if __name__ == '__main__':
    # Start the discord bot in a separate thread
    bot_thread = Thread(target=run_discord_bot)
    bot_thread.start()

    # Start the server
    app.run(host='0.0.0.0', port=8080)