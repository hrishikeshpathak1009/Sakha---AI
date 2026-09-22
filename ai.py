import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

chat = client.chats.create(
    model="gemini-3.5-flash-lite"
)


def ask_ai(prompt):
    try:
        response = chat.send_message(prompt)

        return response.text

    except Exception as e:
        print(f"Gemini Error: {e}")
        return (
            "Sorry, I am unable to reach my intelligence system right now. "
            "Is there something else I can help you with?"
        )