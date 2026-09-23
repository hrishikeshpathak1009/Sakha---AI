from listen import listen
from speechr import recognize
from bolo import bolo

import os
import datetime

from ai import ask_ai
from browser import close_browser


'''bolo(
    "Hello, SAAKHAA here. "
    "Pathak ji's personal assistant. "
    "How can I help you?"
)'''


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
        # 3. STOP
        # -------------------------

        if (
            "stop" in text_lower
            or "exit" in text_lower
            or "sleep" in text_lower
        ):

            bolo("It was nice serving you.")
            break


        # -------------------------
        # 4. LOCAL COMMANDS
        # -------------------------

        elif "time" in text_lower:

            current_time = datetime.datetime.now().strftime(
                "%I:%M %p"
            )

            bolo(
                f"Sir, the time is {current_time}."
            )


        elif "play bhajan" in text_lower:

            bolo("Playing bhajan.")

            os.startfile("bhajan.mp4")

        elif "close browser" in text_lower:
            bolo("OK, closing browser.")
            close_browser()


        # -------------------------
        # 5. EVERYTHING ELSE → GEMINI
        # -------------------------

        else:

            response = ask_ai(text)

            if response:
                bolo(response)


finally:

    # Always close browser when SAAKHAA exits
    close_browser()