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
        
        