# used as chat gpt or voice assistance

import openai
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pywhatkit

# to get current time
time = datetime.datetime.now()

t1 = time.strftime("%y-%m-%d")
t2 = time.strftime("%H:%M:%S")

# set open AI key
openai.api_key = "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" # secret key

engine = pyttsx3.init("sapi5") # microsoft voice api

voices = engine.getProperty("voices")

engine.setProperty("voice" , voices[1].id)

# convert text to voice command

def speak(text):
    engine.say(text) # text to be spoken
    engine.runAndWait() # to play speech now
    
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

# turns our voice command into text and take command from user

def voiceToText(): # file store text
    
    while True:
        recognition = sr.Recognizer() # speech recognition from audio
    
        with sr.Microphone() as source:
            audio = recognition.listen(source) # record audio
            recognition.pause_threshold = 1
        
        # handeling unknown speech error
    
        try :
            user = recognition.recognize_google(audio) # convert audio into string
            # print(user)
        except:
            print("Not audible properly")
            return ""
    
        return user
        
# create a responce from GPT API

def responseAPI(promt): # promt use as generate response
    
    # create GPT API completion method to generate response
    response = openai.Completion.create (
        
        engine = "text-davinci-003",
        prompt = promt,
        max_tokens = 4000,
        n = 1,
        stop = None,
    )
    # return generated response from gpt3 API
    return response["choices"][0]["text"]

# logic of how python run this script

def main():
        
    # this loop allow our program to listen then answer and then continue listening
    while True:
        
        # wait for user to say "hello"
        print("Say 'jarvis' to start recording audio")
        
        with sr.Microphone() as source: # access microphone
            recognition = sr.Recognizer() # speech recognition from audio
            
            audio = recognition.listen(source) # record audio
            
            # handeling exceptions
            try:
                # convert audio into text for recognize google method
                convert = recognition.recognize_google(audio)
                
                if convert.lower() == "jarvis": # if user say hello
                    # record audio
                    
                    print("Listening....")
                    
                    # transcribe record audio to text
                    user = voiceToText().lower()
                    
                    # if transcribe is seccessful
                        
                    if("who created you" in user):
                        speak("Iron Man , also known as Tony Stark")
                        
                    elif("your name" in user or "tell me about yourself" in user or "who are you" in user):
                        speak("hey , my name is Jarvis and I am a ai based program")
                        
                    elif("open youtube" in user):
                        speak("opening youtube")
                        webbrowser.open("youtube.com")
                        
                    elif("open google" in user):
                        speak("opening google")
                        webbrowser.open("google.com")
                        
                    elif("play" in user):
                        song = user.replace("play" , "")
                        speak("playing" + song)
                        pywhatkit.playonyt(song)
                        
                    elif("open microsoft 365" in user or "open word" in user or "open excel" in user or "open powerpoint" in user
                          or "open outlook" in user or "open drive" in user or "open teams" in user or "open 1 note" in user):
                        
                        speak("opening")
                        webbrowser.open("https://www.office.com/?auth=1")
                        
                    elif("time in kolkata" in user):
                        speak(f"date is {t1}")
                        speak(f"and time is: {t2}")
                                                
                    else :
                        if user:
                            print(f"User: {user}")
                        
                            # generate response using GPT3
                            response = responseAPI(user)
                            print(f"Bot: {response}")
                        
                            # read response
                            speak(response)
            
            except Exception as e:
                print("An error occured: {}".format(e))        

greet()
main()
