#import os
#import time
#import playsound
import speech_recognition as sr
#from gtts import gTTS



def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio,language="fr-FR")
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said

text = get_audio()
if text == "4":
    exec(open("./testdesmoteurs.py").read())
else:
    exec(open("./TEST1.py").read())
    print("No match")



#if "hello" in text:
 #   print("hello, how are you?")