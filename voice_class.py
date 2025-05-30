import speech_recognition as sr
import pyttsx3 as px3
import datetime as dt
from rapidfuzz import fuzz
import sys
import os 
import time

from discord.ext import commands

class VoiceAssistant:
    def __init__(self):
        self.engine = px3.init()
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.voice_commands_on = True
        self.select_voice = self.set_female_voice()
        self.activation_word = self.select_voice.name
        self.greetings = self.greeting_per_hour()
        self.keywords = ['hora','apagar','apágate','apagado','fuera','hola','saluda','saludo', self.greetings.lower()]

    def set_female_voice(self):
        '''
        Selección de la voz a utilizar (en este caso, femenina)
        '''
        voices = self.engine.getProperty('voices')        
        select_voice = voices[2]
        # Aurora, debido a que es sinónimo de Amanecer
        #Alba: Amanecer también, 
        select_voice.name = 'alba'

        self.engine.setProperty('voice', select_voice.id)
        return select_voice

    def greeting_per_hour(self):
        hora = dt.datetime.now().hour
        if 5 <= hora < 12:
            return "buenos días"
        elif 12 <= hora < 18:
            return "buenas tardes"
        elif 18 <= hora < 22:
            return "buenas noches"
        else:
            return "buenas madrugadas"

    def fuzzy_command(self, texto, umbral=70):
        '''
        Devuelve True si el texto supera el umbral de semejanza con una
        palabra clave
        '''
        for kw in self.keywords:
            similitud = fuzz.partial_ratio(kw, texto)
            if similitud >= umbral:
                print(f'Fuzzy detected: \'{kw}\' = \'{texto}\' ({similitud}%)')
                return True
        return False
    
    def fuzzy_name(self,texto,umbral=70):
        '''
        Devuelve True si el texto supera el umbral de semejanza
        con el nombre
        '''
        name = self.select_voice.name

        similitud = fuzz.partial_ratio(name, texto)
        if similitud >= umbral:
            print(f'Fuzzy detected: \'{name}\' = \'{texto}\' ({similitud}%)')
            return True
        return False

    def hablar(self, texto):
        '''
        Función para que pueda hablar
        '''
        print(f'{self.select_voice.name.capitalize()}: {texto}')
        self.engine.say(texto)
        self.engine.runAndWait()

    def escuchar(self, timeout=5, phrase_time=3):
        '''
        Funcion para reconocer lo que se dice
        '''
        with self.microphone as source:
            try:
                audio = self.recognizer.listen(source,timeout=timeout, phrase_time_limit=phrase_time)
                texto = self.recognizer.recognize_google(audio, language='es-MX'.lower())
                return texto.lower()
            except sr.WaitTimeoutError:
                pass # Tiempo prolongado o silencio prolongado, se ignora
                return ''
            except sr.UnknownValueError:
                 return '' # Ruido /Inentendible 
            except sr.RequestError:
                print('Error con API de reconocimiento')
                return texto
            
    def activar_comandos(self):
        self.voice_commands_on = True
        self.hablar('Activando comandos de voz')

    def desactivar_comandos(self):
        self.voice_commands_on = False
        self.hablar('Desactivando comandos de voz')

    def accion_comando(self, comando):
        if 'hora' in comando:
            hora = dt.datetime.now().strftime("%H:%M")
            self.hablar(f"Son las {hora}")
        elif  any(offs in comando for offs in ['apagar','apágate','apagado','fuera']):
            self.hablar('Saliendo del sistema')
            sys.exit()
        elif any(his in comando for his in ['hola','saluda','saludo', self.greetings.lower()]):
            self.hablar(f'{self.greetings.capitalize()} {os.getlogin()}. Gusto en Saludarte.')
        elif comando:
            self.hablar('Perdona, aún no tengo un comando para eso')
        else:
            self.hablar('No escuché ningún comando.')

    def esperar_keyword(self):
        self.hablar(f'{self.greetings.capitalize()}, {os.getlogin()}. Di mi nombre cuando me necesites')
        while True:
            texto = self.escuchar(timeout=6)

            if not texto:
                continue

            texto = texto.lower()
            print(texto)

            if self.activation_word in texto and self.fuzzy_name(texto):
                if texto == self.select_voice.name.lower():
                    print('Se detectó palabra clave')
                    self.hablar(f"Hola, soy {self.select_voice.name.capitalize()}. ¿En qué puedo ayudarte?") 
                    comando = self.escuchar()
                    self.accion_comando(comando)
                elif self.fuzzy_command(texto):
                    print('Comando posiblemente encontrado')
                    self.accion_comando(texto)

                else:
                    continue
            else:
                print('no hay contenido relevante. Se ignora comando')
                time.sleep(0.5)

'''
# Revisar como se utiliza
async def setup(bot):
    await bot.add_cog()
'''

if __name__ == "__main__":
    asistente = VoiceAssistant()
    asistente.esperar_keyword()
