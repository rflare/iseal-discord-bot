import time
import subprocess
import os

while True:
    print("Starting bot and webserver...")
    bot_process = subprocess.Popen(['python', 'webserver.py'])

    while not os.path.exists('restart.txt'):
        time.sleep(1)

    print("Restart signal received. Restarting bot...")
    bot_process.terminate()
    os.remove('restart.txt')