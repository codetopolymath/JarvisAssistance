import pyttsx3
from decouple import config

# import from speak
from datetime import datetime

# import from takeUserInput
import speech_recognition as sr
from random import choice
from utils import opening_text

# accessing envoirnment variables
USERNAME = config('USER')
BOTNAME = config('BOTNAME')

# init method in pyttsx3 requires driverName, default=None
# sapi5 is microsoft speechAPI
engine = pyttsx3.init('sapi5')

# set Rate, Volume 
# setProperty method requires name[voice, rate or volume[0.0 - 1.0]] & value
engine.setProperty('rate', 190)
engine.setProperty('volume', 1.0)

# set voice (Female)
# getProperty method requires name[voices, voice, rate, volume]
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Text To Speech Conversion
def speak(text):
    """ speek based on given text """
    # say method requires text & name
    engine.say(text)
    engine.runAndWait() # to clear up all task uptill this checkpoint [speeking all text here is task]

# Greetings
def greetUser():
    """ greets user based on current timezone """
    hour = datetime.now().hour
    if (hour >= 6) or (hour < 12):
        # speak method is combination of say & runAndWait method and works when engine initiated
        speak(f"good morning {USERNAME}")
    elif (hour >= 12) or (hour < 16):
        speak(f"good afternoon {USERNAME}")
    elif (hour >= 16) or (hour < 19):
        speak(f"good evening {USERNAME}")
    else:
        speak(f"you are drunk dude")
    speak(f"tell me your wish {USRNAME}, i am {BOTNAME} here to help you?")

# Take User Input From Mic
def takeUserInput():
    """ speech to text conversion takes place here - get speech from user and convert it into text """
    r = sr.Recognizer() # recognizer class instance, represent collection of recognition functionality
    with sr.Microphone() as source: # Microphone class instance represent physical microphone from computer
        print(f"{USERNAME} state your wish, i am listening")
        r.pause_threshold = 1 # sec of non-speaking audio for check phrase is complete or not
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language="en-in") # google speech recognition API
        if not "exit" in query or "stop" in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour>=21 or hour<6:
                speak("Good night fellow, have a nice sleep")
            else:
                speak("Good day brother/sister, hope is new capetown")
            exit()
    except Exception:
        speak("i ran into exeption, maybe you were not clear enough")
        return 'None'











































