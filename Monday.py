import discord
import requests
import json

"""
discord:
Library 'discord.py' works on with events (messages, e.g.)
By definition: An event is something ypu listen for and then respond to.

requests:
Package that allows to make HTTP request to any URL.

json:
Package that allows to read json data. Most info in the web is JSON format.
"""

salute = ['$hello','$hola','$bonjour']

# Class created to responde to common events
class MyClient(discord.Client): 
    # Called when login is successful
    async def on_ready(self): 
        print('Logged on as {0}!'.format(self.user))

    # Responding to messages
    # Called automatically every time there is a new mesage
    async def on_message(self, message):
        # If the bot sends the message, to avoid a loop
        if message.author == self.user:
            return
        
        # If there is a message with the keyword $hello
        if any (His in message.content.lower() for His in salute):
            await message.channel.send('Hello World!')

# Default settings for the bot
intents = discord.Intents.default() 
# Explicitely declare to interract with messages
intents.message_content = True 

# Calling of the MyClient class
client = MyClient(intents=intents) 
# Client uses the token to authenticate itself
client.run('MTM3MzA3ODY1Nzc3NzY2ODEzOA.GiOmyL.QilIKuzchO-wBuZ5szBpk3i7Frz9udiXq6ZgV4') # Replace with your own token

"""
To get sure that it works, when you run the code you should see something like:
'Logged on as Monday#0282!'

Review how to improve response
"""

