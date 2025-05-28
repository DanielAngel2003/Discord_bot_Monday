import speech_recognition as sr
import pyttsx3 as px3
import datetime as dt
import sys
import os 

class VoiceAssistant:
    def __init__(self):
        self.engine = px3.init()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.voice_commands_on = True
        
