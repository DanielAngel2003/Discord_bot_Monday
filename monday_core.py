# archivo: monday_core.py
from discord.ext import commands
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

#Se crea una clase para facilitar
class CoreCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        # Propiedad para mantenerse activo
        self.bot.bot_on = True
        # Nombres para responder
        self.calls = ['oye monday', 'monday', 'hey monday', 'oye, monday', 'hey, monday', 'disculpa, monday']
        # Palabras que detecta en el mensaje para eliminarlo
        self.banned_words = ['nigger', 'nigga', 'prieto']

    ### Setting in the bot
    @commands.Cog.listener()
    async def on_ready(self):
        # Prints if the bot has logged in succesfully
        print(f'Logged on as {self.bot.user}!')

    ### Member_joining
    @commands.Cog.listener()
    async def on_member_join(self,member):
        # If M.O.N.D.A.Y. is Off
        if not self.bot.bot_on:
            return
        
        # Salutes the new user
        await member.send(f'Welcome, {member.name}')

    ### Responding to messages
    @commands.Cog.listener()
    async def on_message(self,message):
        
        # If the bot sends the message, to avoid a loop
        if message.author == self.bot.user:
            return
        
        # If M.O.N.D.A.Y. is Off
        if not self.bot.bot_on:
            await self.process_commands(message)
            return
        
         ## Variables to use
        meme = [f'A meme for monsieur/madame {message.author.name}',
        f'Hot n Ready, {message.author.name}!!!', ' Someone said... MEME?', 
        f'A MEME pleasure, {message.author.name}', 'MEMETASTIC!', f'THE MEME HAS SPOKEN!!!', 
        'MEME WARS!!!', f'ALL HAIL THE MEME, {message.author.name}!!!',]
        msg = message.content.lower() # The string of the message
        answers = [f'At your service, {message.author.name}!', f'Yes, {message.author.name}?',
        f'How can I help, {message.author.name}?', 'M.O.N.D.A.Y Reporting for Duty!!!',
        'Did somebody call?', f'I\'m right here, {message.author.name}!']

        # Send memes with the keyword 'meme'
        if 'meme' in msg:
            await message.channel.send(random.choice(meme))
            await message.channel.send(self.get_meme())

        # Eliminates any message with a banned word
        if any(Nos in msg for Nos in self.banned_words):
        # Deleting the message
            await message.delete()
            await message.channel.send(f'{message.author.mention}, YOU CAN\'T USE THE N WORD HERE!!!!')

        # Let's itself get knowed, in case 
        if msg.strip() in self.calls:
            await message.channel.send(random.choice(answers))
            await message.channel.send('If you need help with my commands, you can say \'Monday help\'')  

        #Linea comentada porque 
        #await self.bot.process_commands(message)
    
    ### Searches for memes in the url
    def get_meme(self):
        try:
            response = requests.get('https://meme-api.com/gimme')
            json_data = json.loads(response.text)
            return json_data['url']
        except:
            return 'No meme, my dudes :c'
        
    @commands.command(name='hola', aliases=['hello','bonjour'])
    async def greet(self, ctx):
        # Salutes back the person that saluted M.O.N.D.A.Y.
        await ctx.channel.send(f'Hello, {ctx.author.name}!')

    ### Command for Turning On
    @commands.command()
    async def on(self, ctx):
        # Command to detect the 'On' command for M.O.N.D.A.Y.
        # Allows M.O.N.D.A.Y. to act as it is programmed
        self.bot.bot_on = True
        await ctx.send('M.O.N.D.A.Y. On')

    ### Command for Turning Off
    @commands.command()
    async def off(self, ctx):
        #Command to detect the 'Off' for M.O.N.D.A.Y.
        self.bot.bot_on = False
        await ctx.send('M.O.N.D.A.Y. Off')
    
    ### Command for Shuting down
    @commands.command()
    async def sleep(self,ctx):
        #Command to detect the 'sleep' for M.O.N.D.A.Y.
        await ctx.send('See you all when September ends.')
        #Shuts down the bot entirely
        await self.bot.close()

# Permite que se puedan utilizar como Cogs para un bot de Discord
async def setup(bot):
    await bot.add_cog(CoreCog(bot))
