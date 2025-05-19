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

banned_words = ['nigger', 'nigga', 'prieto']
calls = ['oye monday', 'monday', 'hey monday', 'oye, monday', 'hey, monday', 'disculpa, monday']


#Se crea una clase para facilitar
class CoreCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.bot.bot_on = True
        self.calls = ['oye monday', 'monday', 'hey monday', 'oye, monday', 'hey, monday', 'disculpa, monday']
        self.banned_words = ['nigger', 'nigga', 'prieto']

    @commands.Cog.listener()
    async def on_ready(self):
        #Inicialización
        print(f'Logged on as {self.bot.user}!')

    @commands.Cog.listener()
    async def on_member_join(self,member):
        if not self.bot.bot_on:
            return
        await member.send(f'Welcome, {member.name}')

    @commands.Cog.listener()
    async def on_message(self,message):
       
        if message.author == self.bot.user:
            return
        
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

        if 'meme' in msg:
            await message.channel.send(random.choice(meme))
            await message.channel.send(self.get_meme())

        if any(Nos in msg for Nos in banned_words):
        # Deleting the message
            await message.delete()
            await message.channel.send(f'{message.author.mention}, YOU CAN\'T USE THE N WORD HERE!!!!')

        if msg.strip() in calls:
            await message.channel.send(random.choice(answers))
            await message.channel.send('If you need help with my commands, you can say \'Monday help\'')  

        #await self.bot.process_commands(message)
    
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

    @commands.command()
    async def on(self, ctx):
        self.bot.bot_on = True
        await ctx.send('M.O.N.D.A.Y. On')

    @commands.command()
    async def off(self, ctx):
        self.bot.bot_on = False
        await ctx.send('M.O.N.D.A.Y. Off')
    
    @commands.command()
    async def sleep(self,ctx):
        await ctx.send('See you all when September ends.')
        await self.bot.close()

async def setup(bot):
    await bot.add_cog(CoreCog(bot))
