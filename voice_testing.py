#Codigo de prueba brindado por ChatGPT para poder inicializar la utilización de asistente por voz

import speech_recognition as sr
import pyttsx3
import datetime

# Inicializar el motor de voz
engine = pyttsx3.init()

def hablar(texto):
    print(f'Evening: {texto}')
    engine.say(texto)
    engine.runAndWait()

def escuchar():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        audio = r.listen(source)
        try:
            texto = r.recognize_google(audio, language='es-ES')
            print(f'Usuario: {texto}')
            return texto.lower()
        except sr.UnknownValueError:
            return 'No entendí eso'
        except sr.RequestError:
            return 'Error con reconocimiento'

# Ejemplo de funcionamiento
hablar("Hola, ¿en qué puedo ayudarte?")
comando = escuchar()
if "hora" in comando:
    hora = datetime.datetime.now().strftime("%H:%M")
    hablar(f"Son las {hora}")
elif comando: 
    hablar('Perdona, aún no tengo un comando para eso')
else:
    hablar('No escuché ningún comando.')

