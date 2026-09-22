import os
from dotenv import load_dotenv
from google import genai
from google.genai import types


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


client = genai.Client(
    api_key=api_key,
    # http_options=types.HttpOptions(
    #     timeout=15000
    # )
)
chat = client.chats.create(
    model="gemini-3.5-flash"
)

def ask_ai(prompt):

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print(f"Gemini Error: {e}")
        return "Sorry, I am unable to reach my intelligence system right now."