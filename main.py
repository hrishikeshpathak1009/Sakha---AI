from listen import listen
from speechr import recognize
from bolo import bolo
import webbrowser


intro="Hello, SAAKHAA here, Pathak ji's personal assistant. I am just like JARVIS of Iron man."
print(intro)
#bolo(intro)


audio = listen()

text = recognize(audio)

print(f"You said to me : {text}")

bolo(f" You said to me : {text}")

if "Open Youtube".lower() in text.lower():
    webbrowser.open("https://youtube.com")