import discord 
from discord import commands
import asyncio 
import threading 
from voice_class import VoiceAssistant 
# Clase ya implementada

class VoiceAssistantCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.voice_assistant = VoiceAssistant()
        self.assistant_thread = None
        self.running = False
        
    @commands.command(name='asistente')
    async def iniciar_asistente(self, ctx, arg=None):
        '''
        Comando para iniciar/detener asistente de voz
        '''
        pass

        def run_assistant():
            pass
    
async def setup(bot):
    await(bot.add_cog(VoiceAssistantCog(bot)))