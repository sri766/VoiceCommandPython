import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os

from wikipedia.wikipedia import random

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices)
engine.setProperty('voice' , voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak("I an Jarvis Sir.Please tell me how may I help you")


def takecommamd():
    #it takes microphone input and return output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    
    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f'user said:{query}\n')
    
    except Exception as e:
        #print(e)

        print("Say that again please....")
        return "None"
    return query





if __name__=="__main__":
    wishMe()
    string=input("DO you want to run the code:yes or no")
    while (string =='yes'):
        query=takecommamd().lower()
    #logic for exectuting task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace('wikipedia','')
            results=wikipedia.summary( query , sentences = 2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google'in query:
            webbrowser.open('google.com')
        elif 'open github' in query:
            webbrowser.open('github.com')
        elif 'play music' in query:
            music_dir='D:\songs'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.pat.join(music_dir,songs[0]))
        elif 'time 'in query:
            strTime=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"Sir,the time is {strTime}")
        elif 'open code' in query:
            codepath='C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe'
            os.startfile(codepath)

else:
    print('Have a good day,sir')
    speak('Have a good day,sir')


