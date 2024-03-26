from inspect import classify_class_attrs
from re import S
import ssl
import speech_recognition as sr
import pyttsx3

def interpretation():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            print('recognizing...')
            query = r.recognize_google(audio, language = 'en-US')
            print('You:', query)
        except:
            return None
    return query

def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()


