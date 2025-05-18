import discord
from discord.ext import commands # Optimización de comandos
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
banned_words = ['nigger', 'nigga', 'prieto']

# Default settings for the bot
intents = discord.Intents.default() 

# Explicitely declare to interract with messages
intents.message_content = True 
# Explicitely declare to interact with member info
intents.members = True

bot = commands.Bot(command_prefix='Monday ', intents=intents, case_insensitive=True)
# prefix with a space for sintaxis
# Corroborar si funciona, parece que no funciona case_insensitive

# Propiedad para mantenerse activo
bot.bot_on = True

### Searches for memes in the url
def get_meme():
    response = requests.get('https://meme-api.com/gimme')
    json_data = json.loads(response.text)
    return json_data['url']

### Logic of On/Off bot

# The bot checks
@bot.check
async def globally_block_commands(ctx):
    #'On' is only command to detect, even when M.O.N.D.A.Y. is off
    if ctx.command.name == 'on':
        return True
    
    return bot.bot_on

### Setting in the bot
@bot.event 
# Declares that this is a event
async def on_ready():
    # Prints if the bot has logged in succesfully
    print('Logged on as {0}!'.format(bot.user))

### Member_joining
@bot.event
async def on_member_join(member):
    # If M.O.N.D.A.Y. is Off
    if not bot.bot_on: 
        return
    
    # Salutes the new user
    await member.send(f'Welcome, {member.name}!')

### Responding to messages
@bot.event
# Called automatically every time there is a new mesages
async def on_message(message):
    # If M.O.N.D.A.Y. is Off
    if not bot.bot_on:
        # Ignores the message until it gets on
        return
    
    ## Variables to use
    meme = [f'A meme for monsieur/madame {message.author.name}',
    f'Hot n Ready, {message.author.name}!!!', ' Someone said... MEME?', 
    f'A MEME pleasure, {message.author.name}', 'MEMETASTIC!', f'THE MEME HAS SPOKEN!!!', 
    'MEME WARS!!!', f'ALL HAIL THE MEME, {message.author.name}!!!',]
    msg = message.content.lower() # The string of the message

    # If the bot sends the message, to avoid a loop
    if message.author == bot.user:
        return

    # If there is a message with the keyword $hello
    # this would be now a command
    if any(His in msg for His in salute):
        #For name, message.author.name
        #For mention (@DanSolo), message.author.mention
        pass
        #await message.channel.send(f'Hello, {message.author.name}!')

    # command, for function
    if '$meme' in msg:
        await message.channel.send(random.choice(meme))
        await message.channel.send(get_meme())

    # keyword, for message
    if any(Nos in msg for Nos in banned_words):
        # Deleting the message
        await message.delete()
        await message.channel.send(f'{message.author.mention}, YOU CAN\'T USE THE N WORD HERE!!!!')

    # Once all the message content options are setted, we declare:
    await bot.process_commands(message)
    # With this, will get sure that searches for commands in the messag

### Commands section
# Note: the variable for every command should be 'ctx' or 'message

### Command to salute
@bot.command()
async def hola(ctx):
    # Salutes back the person that saluted M.O.N.D.A.Y.
    await ctx.channel.send(f'Hello there, {ctx.author.mention}!')

### Command for Turning On
@bot.command()
async def on(ctx):
    # Command to detect the 'On' command for M.O.N.D.A.Y.
    # Allows M.O.N.D.A.Y. to act as it is programmed
    bot.bot_on = True
    await ctx.channel.send('M.O.N.D.A.Y. On')
    return

### Command for Turning Off
@bot.command()
async def off(ctx):
    #Command to detect the 'Off' for M.O.N.D.A.Y.
    bot.bot_on = False
    await ctx.channel.send('M.O.N.D.A.Y. Off')
    return

#Running the bot with the token
bot.run('MTM3MzA3ODY1Nzc3NzY2ODEzOA.GiOmyL.QilIKuzchO-wBuZ5szBpk3i7Frz9udiXq6ZgV4') 
# Replace with your own token

"""
To get sure that it works, when you run the code you should see something like:
'Logged on as M.O.N.D.A.Y.#0282!'

Review how to improve response
"""

