import sys
import speech_recognition as sr
import pyttsx3
import os
import datetime
# import openai
import wikipedia
import webbrowser
# import contact
import recoder



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning sir!")

    elif hour>=12 and hour<18:
        speak("good afternoon sir!")

    else:
        speak("good evening")

    speak("i am type bot sir please tell me how can i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en,in")
        print(f"user said: {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return"None"
    return query


if __name__=="__main__":
    speak("hello sir,type bot this side")
    wishMe()
    while True:
       query = takeCommand().lower()
       if 'wikipedia' in query:
           speak('seraching wikipedia...')
           query = query.replace("wikipedia","")
           result = wikipedia.summary(query,sentences = 2)
           speak("according to wikipedia")
           print(result)
           speak(result)

       elif 'open youtube' in query:
           webbrowser.open("youtube.com")
       #
       elif 'open google' in query:
           webbrowser.open("google.com")
       #
       elif 'open code' in query:
           codepath = "C:\Program Files\JetBrains\PyCharm Community Edition 2024.1\bin\pycharm64.exe "
           os.startfile(codepath)

       elif 'exit'.lower()in query.lower():
           exit()

