#Codigo de prueba brindado por ChatGPT para poder inicializar la utilización de asistente por voz

import speech_recognition as sr
import pyttsx3
import datetime
import sys
import os

# Inicializar el motor de voz
engine = pyttsx3.init()

# Obtener todas las voces disponibles
voices = engine.getProperty('voices')
"""
Lista de Voces:
Microsoft Helena Desktop
Microsoft Zira Desktop
Microsoft Sabina Desktop

Parámetros: ID,Nombre,Idioma,Género
"""
select_voice = voices[2]
select_voice.name = 'aurora'
print(select_voice)

def hablar(texto):
    global select_voice
    print(f'Evening: {texto}')
    engine.setProperty('voice', select_voice.id)
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

def active():
    global select_voice
    # Ejemplo de funcionamiento
    hablar(f"Hola, soy {select_voice.name.capitalize()}. ¿En qué puedo ayudarte?") # Aurora, debido a que es sinónimo de Amanecer
    comando = escuchar()
    if 'hora' in comando:
        hora = datetime.datetime.now().strftime("%H:%M")
        hablar(f"Son las {hora}")
    elif  any(offs in comando for offs in ['apagar','apágate','apagado','fuera']):
        hablar('Saliendo del sistema')
        sys.exit()
    elif any(his in comando for his in ['hola','saluda','saludo']):
        hablar(f'Hola {os.getlogin()}. Gusto en Saludarte.')
    elif comando:
        hablar('Perdona, aún no tengo un comando para eso')

    else:
        hablar('No escuché ningún comando.')

def keyword_await(keyword='asistente'):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Esperando Palabra Clave...')
        while True:
            try:
                audio = recognizer.listen(source, timeout=1)
                texto = recognizer.recognize_google(audio, language='es-MX').lower()
                if keyword in texto:
                    print("Palabra clave detectada.")
                    active()
                    print("Esperando nuevamente...")
            except sr.WaitTimeoutError:
                pass  # silencio prolongado, se ignora
            except sr.UnknownValueError:
                pass  # ruido o no se entendió
            except sr.RequestError:
                print("Error con la API de reconocimiento.")
                break

keyword_await(select_voice.name)

"""
26/05/2025:
Prueba principal lograda, devuelve la hora [20:32]

Ahora veré como puedo implementar cada vez más opciones dentro del modelo, tomanod esta vase que ahora tengo.
"""