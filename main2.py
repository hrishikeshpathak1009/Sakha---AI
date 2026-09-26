import asyncio
import re

from listen import listen
from speechr import recognize
from bolo import bolo
from graph import ask_saakhaa


# ============================================================
# EXIT COMMANDS
# ============================================================

EXIT_WORDS = {
    "exit",
    "quit",
    "stop",
    "goodbye",
    "bye",
    "shutdown",
    "terminate",
    "sleep",
    "power off",
    "turn off",
}


def should_exit(text):

    text = text.lower().strip()

    return any(
        re.search(
            rf"\b{re.escape(word)}\b",
            text
        )
        for word in EXIT_WORDS
    )


# ============================================================
# MAIN
# ============================================================

async def main():

    bolo(
        "Hello, I am your personal assistant. "
        "How can I help you?"
    )

    while True:

        try:

            # ------------------------------------------------
            # Listen
            # ------------------------------------------------

            audio = listen()

            if not audio:
                continue

            # ------------------------------------------------
            # Speech → Text
            # ------------------------------------------------

            text = recognize(audio)

            if not text:
                continue

            print(f"You: {text}")

            # ------------------------------------------------
            # Exit
            # ------------------------------------------------

            if should_exit(text):

                bolo("Goodbye.")
                break

            # ------------------------------------------------
            # LangGraph + Ollama
            # ------------------------------------------------

            response = await ask_saakhaa(
                text,
                thread_id="main"
            )

            # ------------------------------------------------
            # Text → Speech
            # ------------------------------------------------

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


# ============================================================
# START
# ============================================================

if __name__ == "__main__":

    asyncio.run(main())