import time
import subprocess
import os

while True:
    print("Starting bot and webserver...")
    bot_process = subprocess.Popen(['python3', 'webserver.py'])

    while not os.path.exists('restart.txt'):
        time.sleep(120)

    print("Restart signal received. Restarting bot...")
    bot_process.terminate()
    os.remove('restart.txt')