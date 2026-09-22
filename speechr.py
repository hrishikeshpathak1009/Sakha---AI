import speech_recognition as sr

recognizer = sr.Recognizer()


def recognize(audio):
    print("Processing...")

    try:
        text = recognizer.recognize_google(audio)
        return text

    except sr.UnknownValueError:
        print("I couldn't understand you.")
        return ""

    except sr.RequestError as e:
        print("Speech recognition error:", e)
        return ""