import pyowm
import pyttsx3
tts=pyttsx3.init()
voices = tts.getProperty('voices')
tts.setProperty('voice','ru')
for voice in voices:
    if voice.name == 'Anna':
        tts.setProperty('voice',voice.id)

import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import datetime
'''def speak(what):
    print( what )
    speak_engine.say( what )
    speak_engine.runAndWait()
    speak_engine.stop()
def callback(recognizer, audio):
    try:
        voice = recognizer.recognize_google(audio, language = "ru-RU").lower()
        print("[log] Распознано: " + voice)
    
 
    except sr.UnknownValueError:
        print("[log] Голос не распознан!")
    except sr.RequestError as e:
        print("[log] Неизвестная ошибка, проверьте интернет!")
 
r = sr.Recognizer()
m = sr.Microphone(device_index = 1)
with m as source:
    r.adjust_for_ambient_noise(source)
 
speak_engine = pyttsx3.init()
 
voices = speak_engine.getProperty('voices')
speak_engine.setProperty('voice', voices[1].id)

speak("Добрый день, повелитель")
speak("Кеша слушает")
 
stop_listening = r.listen_in_background(m, callback)
while True: time.sleep(0.1)'''

engine = pyttsx3.init()
engine.say("Привет")
engine.runAndWait()
engine.say("Что хочешь узнать температуру за окном? Где живёшь: ")
engine.runAndWait()       
owm =pyowm.OWM('f2e75790f4c4243a14f62871bd90dfd6',language='ru')
place=input('Что хочешь узнать температуру за окном? Где живёшь: ')
observation = owm.weather_at_place(place)
w = observation.get_weather()
temp=w.get_temperature('celsius')['temp']
print('В городе '+place+' сейчас '+w.get_detailed_status())
print('Температура сейчас в районе '+str(temp))
if temp <0:
    print('Ты уверен что тебе куда-то нужно,давай лучше с чайком под пледик')
    engine.say('Ты уверен что тебе куда-то нужно,давай лучше с чайком под пледик')
    engine.runAndWait()   
elif temp <=5:
    print('Сейчас холодно оденься по теплее')
    engine.say('Сейчас холодно оденься по теплее')
    engine.runAndWait()
elif temp>15:
    print('Тумпература норм,одевайся как  угодно')
    engine.say('Тумпература норм,одевайся как  угодно')
    engine.runAndWait()
else:
    print('Советую примотрется к охлождающим напиткам')
    engine.say('Советую примотрется к охлождающим напиткам')
    engine.runAndWait()
engine.say('В городе '+place+' сейчас '+w.get_detailed_status())
engine.runAndWait()
engine.say('Температура сейчас в районе '+str(temp))
engine.runAndWait()


    
