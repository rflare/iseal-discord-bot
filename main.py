# -----------------------------------------------------------------------------------------
# MIT License

# Copyright (c) 2024 Lunarcat

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# -----------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------
# Description: Main file of the bot, contains the client class and the command tree
# -----------------------------------------------------------------------------------------


# Importing the required libraries
import discord
import discord.ext
from discord import app_commands
from discord import ui
import os
from dotenv import load_dotenv
import json
import datetime

#loading the .env file for the bot token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


#opening config file to get settings and version of the bot
with open('config.json') as config_file:
    config = json.load(config_file)

VERSION = "2.0.0-develop-1"

#defining the client
class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.all())
        self.synced = False
    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #checking if commands a synced
            await tree.sync() #syncing the commands
            self.synced = True
            status_message = config['status_message']
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status_message)) #setting the bot's status, change to liking
        print(f"We have logged in as {self.user}.")
client = aclient()
tree = app_commands.CommandTree(client)

#Role check
trigger_roles = config['trigger_roles']
async def check_roles(roles):
    if any(role in roles for role in trigger_roles): 
        return True
    else: 
        return False




#running the bot
client.run(TOKEN)

