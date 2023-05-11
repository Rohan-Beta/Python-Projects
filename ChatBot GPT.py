# create chatBot using GPT API
# it is also used as voice assistance

# command line in windows

# for install openai - pip install opneai
# for install pyttsx3 - pip install pyttsx3
# for install speech_recognition - pip install SpeechRecognition

# to get openai.api_key or secret key

# Step 1. visit (https://platform.openai.com/account/api-keys) this website
# Step 2. sign up
# Step 3. click on you profile icon , then click on View API keys
# Step 4. click on create new secret key

import openai
import pyttsx3
import speech_recognition as sr
import time

# set open AI key
openai.api_key = "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" # secret key

# initialize text to speech engine
engine = pyttsx3.init()

# turns our voice command into text

def voiceToText(file): # file store text
    recognition = sr.Recognizer() # speech recognition from audio
    
    with sr.AudioFile(file) as source:
        audio = recognition.record(source) # record audio
        
    # handeling unknown speech error
    
    try :
        return recognition.recognize_google(audio)
    except:
        print("Skipping unknowns speech error")
        
# create a responce from GPT3 API

def responseAPI(promt): # promt use as generate response
    
    # create GPT API completion method to generate response
    # given in GPT Api documentation
    response = openai.Completion.create (
        
        engine = "text-davinci-003",
        prompt = promt,
        max_tokens = 4000,
        n = 1,
        stop = None,
    )
    # return generated response from gpt3 API
    return response["choices"][0]["text"]

# convert text to voice command

def textToVoice(text):
    engine.say(text) # text to be spoken
    engine.runAndWait() # to play speech now
    
# logic of how python run this script

def main():
    # this loop allow our program to listen then answer and then continue listening
    while True:
        
        # wait for user to say "hello"
        print("Say 'hello' to start recording audio")
        
        with sr.Microphone() as source: # access microphone
            recognition = sr.Recognizer() # speech recognition from audio
            
            audio = recognition.listen(source) # record audio
            
            # handeling exceptions
            try:
                # convert audio into text for recognize google method
                convert = recognition.recognize_google(audio)
                
                if convert.lower() == "hello": # is user say hello
                    # record audio
                    
                    file = "input.wav"
                    print("Say your question: ")
                    
                    with sr.Microphone() as source:
                        recognition = sr.Recognizer()
                        
                        source.pause_threshold = 1
                        audio = recognition.listen(source , phrase_time_limit= None , timeout= None)
                        
                        # create a file and store user voice command
                        with open(file , "wb") as f:
                            f.write(audio.get_wav_data())
                    
                    # transcribe record audio to text
                    text = voiceToText(file)
                    
                    # if transcribe is seccessful
                    
                    if text:
                        print(f"User: {text}")
                        
                        # generate response using GPT3
                        response = responseAPI(text)
                        print(f"Bot: {response}")
                        
                        # read response
                        textToVoice(response)
            
            except Exception as e:
                print("An error occured: {}".format(e))
main()
