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

def active():
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

def keyword_await(keyword='asistente'):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Esperando Palabra Clave...')
        while True:
            try:
                audio = recognizer.listen(source, timeout=5)
                texto = recognizer.recognize_google(audio, language='es-ES').lower()
                print(f"👂 Escuchado: {texto}")
                if keyword in texto:
                    print("✅ Palabra clave detectada.")
                    active()
                    print("Esperando nuevamente...")
            except sr.WaitTimeoutError:
                pass  # silencio prolongado, se ignora
            except sr.UnknownValueError:
                pass  # ruido o no se entendió
            except sr.RequestError:
                print("❌ Error con la API de reconocimiento.")
                break

keyword_await()

"""
26/05/2025:
Prueba principal lograda, devuelve la hora [20:32]

Ahora veré como puedo implementar cada vez más opciones dentro del modelo, tomanod esta vase que ahora tengo.
"""