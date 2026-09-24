from listen import listen
from speechr import recognize
from bolo import bolo
from ai import ask_ai

import re


def main():

    bolo(
        "Hello, I am your personal assistant. "
        "How can I help you?"
    )

    while True:

        try:

            audio = listen()

            if not audio:
                continue

            text = recognize(audio)

            if not text:
                continue

            print(f"You: {text}")

            text_lower = text.lower().strip()

            # ==========================================
            # STOP SAAKHAA
            # ==========================================

            exit_words = {
                "exit",
                "quit",
                "stop",
                "goodbye",
                "bye",
                "shutdown",                
                "terminate",
                "end",
                "sleep"
            }

            if any(
                re.search(
                    rf"\b{re.escape(word)}\b",
                    text_lower
                )
                for word in exit_words
            ):

                bolo("Goodbye.")
                break

            # ==========================================
            # AI
            # ==========================================

            response = ask_ai(text)

            print(
                "AI RESPONSE:",
                repr(response)
            )

            if response:
                bolo(response)

        except KeyboardInterrupt:

            print("\nStopping SAAKHAA...")
            break

        except Exception as e:

            print(f"Error: {e}")

            bolo(
                "Sorry, something went wrong."
            )


if __name__ == "__main__":
    main()