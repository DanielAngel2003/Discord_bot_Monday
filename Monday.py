from discord.ext import commands
import discord

"""
discord:
Library 'discord.py' works on with events (messages, e.g.)
By definition: An event is something ypu listen for and then respond to.
"""

# Default settings for the bot
intents = discord.Intents.default() 
# Explicitely declare to interract with messages
intents.message_content = True 
# Explicitely declare to interact with member info
intents.members = True

bot = commands.Bot(command_prefix='Monday ', intents=intents, case_insensitive=True)

@bot.event
async def setup_hook():
    await bot.load_extension('monday_core')

### Logic of On/Off bot
@bot.check
async def globally_block_commands(ctx):
    #'On' is only command to detect, even when M.O.N.D.A.Y. is off
    if ctx.command.name == 'on':
        return True
    
    return bot.bot_on

#Running the bot with the token
bot.run('MTM3MzA3ODY1Nzc3NzY2ODEzOA.GiOmyL.QilIKuzchO-wBuZ5szBpk3i7Frz9udiXq6ZgV4') 
# Replace with your own token
