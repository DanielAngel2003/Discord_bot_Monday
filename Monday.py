import discord
import requests
import json
import random

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

# Searches for memes in the url
def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

# Class created to responde to common events
class MyClient(discord.Client): 
    # Called when login is successful
    def __init__(self, *, intents, **options):
        super().__init__(intents=intents, **options)
        # Bot is on from the beggining
        self.bot_on = True

    async def on_ready(self): 
        print('Logged on as {0}!'.format(self.user))

    # Responding to messages
    # Called automatically every time there is a new mesage
    async def on_message(self, message):
        # Variables to use
        meme = [f'A meme for monsieur/madame {message.author.name}',
        f'Hot n Ready, {message.author.name}!!!', ' Someone said... MEME?', 
        f'A MEME pleasure, {message.author.name}', 'MEMETASTIC!', f'THE MEME HAS SPOKEN!!!', 
        'MEME WARS!!!', f'ALL HAIL THE MEME, {message.author.name}!!!',]

        # If the bot sends the message, to avoid a loop
        if message.author == self.user:
            return

        # Conditional to detect the 'Off' command for Monday
        if 'monday off' in message.content.lower():
            # Executes if string IN the message
            self.bot_on = False
            await message.channel.send('M.O.N.D.A.Y. Apagado')
            return

        # Conditional to detect the 'On' command for Monday
        if 'monday on' in message.content.lower():
            # Executes if string IN the message
            self.bot_on = True
            await message.channel.send('M.O.N.D.A.Y. Encendido')
            return
        
        # If the bot is off
        if not self.bot_on:
            # Ignores the message until it gets on
            return

        # If there is a message with the keyword $hello
        if any (His in message.content.lower() for His in salute):
            #For name, message.author.name
            #For mention (@DanSolo), message.author.mention
            await message.channel.send(f'Hello, {message.author.name}!')

        if '$meme' in message.content.lower():
            await message.channel.send(random.choice(meme))
            await message.channel.send(get_meme())

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
'Logged on as M.O.N.D.A.Y.#0282!'

Review how to improve response
"""

