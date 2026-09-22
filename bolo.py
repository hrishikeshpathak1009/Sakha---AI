import pyttsx3


def bolo(text):
    engine = pyttsx3.init("sapi5")
    print(text)
    engine.say(text)
    engine.runAndWait()
    engine.stop()