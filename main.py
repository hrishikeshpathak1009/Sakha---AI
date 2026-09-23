from listen import listen
from speechr import recognize
from bolo import bolo
import os
import datetime

from ai import ask_ai
from browser import (
    open_website,
    search_youtube,
    play_first_video,
    close_browser
)


bolo("Hellow, SAAKHAA here. Pathak ji's personal assistant. How can I help you?")


try:

    while True:

        # -------------------------
        # 1. LISTEN
        # -------------------------

        audio = listen()

        # -------------------------
        # 2. SPEECH → TEXT
        # -------------------------

        text = recognize(audio)

        if not text:
            continue

        text_lower = text.lower().strip()

        print(f"You said: {text}")

        # -------------------------
        # STOP
        # -------------------------

        if "stop" in text_lower or "exit" in text_lower or "sleep" in text_lower:

            bolo("It was nice serving you.")
            break

        # -------------------------
        # AI
        # -------------------------

        elif "using your intelligence" in text_lower or "do you think" in text_lower or "brain" in text_lower or "think and answer" in text_lower:

            prompt = text_lower.replace("using your intelligence", "").strip()

            if not prompt:
                bolo("What would you like me to think about?")
                continue

            answer = ask_ai(prompt)

            
            bolo(answer)

        # -------------------------
        # WEBSITES
        # -------------------------

        elif "play the first video" in text_lower:

            bolo("Playing the first video.")

            play_first_video()

        elif "search youtube for" in text_lower:

            query = text_lower.replace(
                "search youtube for",
                 ""
            ).strip()

            if not query:
                bolo("What should I search for?")
                continue

            bolo(f"Searching YouTube for {query}.")

            search_youtube(query)

        elif "open youtube" in text_lower:

            bolo("Opening YouTube.")
            open_website("https://www.youtube.com")

        elif "open instagram" in text_lower:

            bolo("Opening Instagram.")
            open_website("https://www.instagram.com")

        elif "open gmail" in text_lower:

            bolo("Opening Gmail.")
            open_website("https://mail.google.com")

        elif "open google" in text_lower:

            bolo("Opening Google.")
            open_website("https://www.google.com")

        # -------------------------
        # BHAJAN
        # -------------------------

        elif "play bhajan" in text_lower:

            bolo("Playing bhajan.")
            os.startfile("bhajan.mp4")

        # -------------------------
        # TIME
        # -------------------------

        elif "time" in text_lower:

            current_time = datetime.datetime.now().strftime("%I:%M %p")

            bolo(f"Sir, the time is {current_time}.")

        # -------------------------
        # UNKNOWN REQUEST
        # -------------------------

        else:

            bolo("I don't know how to do that yet.")

finally:

    # Always close browser when program exits
    close_browser()