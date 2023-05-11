# AI voice assistance

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pywhatkit
import os

engine = pyttsx3.init("sapi5") # use microsoft voice api

voices = engine.getProperty("voices") # get voices

# voices[1].id = female voice and voices[0].id = male voice
engine.setProperty("voice" , voices[1].id) # set voice

# speak output
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# greet according to time
def greet():
    
    time = int(datetime.datetime.now().hour) # get current time in hour
    
    if(time >= 6 and time < 12):
        speak("good morning , how can i help you")
    
    elif(time >= 12 and time < 16):
        speak("good afternoon , how can i help you")
    
    elif(time >= 16 and time < 20):
        speak("good evening , how can i help you")
        
    else :
        speak("good night , how can i help you")
    
# take input from user and return string output
def takeCommand():
    
    recognition = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening....")
        recognition.pause_threshold = 1 # seconds of non-speaking audio
        audio = recognition.listen(source) # listing user input command
        
    try:
        user = recognition.recognize_google(audio) # convert audio into string
        print(f"User: {user}")
        
    except Exception as e:
        print("Not audible properly , please say that again")
        return "None"
    
    return user

# task execute by bot
def execute():
    
    while True:
        user = takeCommand().lower() # conver input string into lowercase
        
        
        if("wikipedia" in user):
            ans = user.replace("wikipidea" , "")
            answer = wikipedia.summary(ans)
            
            print(answer)
            speak(answer)
        
        elif("open youtube" in user):
            speak("opening youtube")
            webbrowser.open("youtube.com")
            
        elif("open google" in user):
            speak("opening google")
            webbrowser.open("google.com")
            
        elif("play" in user) :
            song = user.replace("play" , "")
            speak("playing" + song)
            pywhatkit.playonyt(song)
            
        elif("open vs code" in user):
            path = "D:\\Microsoft VS Code\\Code.exe"
            speak("opening vs code")
            os.startfile(path)
            
        elif("open microsoft 365" in user or "open word" in user or "open excel" in user or "open powerpoint" in user
             or "open outlook" in user or "open drive" in user or "open teams" in user or "open 1 note" in user):
            speak("opening")
            webbrowser.open("https://www.office.com/?auth=1")
            
        elif("open email" in user or "open gmail" in user):
            speak("opening mail")
            webbrowser.open("mail.google.com")
    
greet()
execute()
