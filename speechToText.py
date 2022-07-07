import speech_recognition as sr
import pyaudio


r=sr.Recognizer()
def listening():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        data=r.record(source,duration=5)
        print("I am listening...")
        text=r.recognize_google(data,language='en')
        print (text)