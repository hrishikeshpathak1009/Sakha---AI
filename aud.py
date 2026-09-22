import speech_recognition as sr
import pyaudiowpatch as pyaudio
import pyttsx3

def say(text):
    print(text)

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

say("Hello, Jarvis here , Pathak jis' personal assistance")
say("How can I help you")

print("PROGRAM FINISHED")