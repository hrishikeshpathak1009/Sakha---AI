from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)
chat = client.chats.create(
    model="gemini-3.5-flash-lite"
)
response = chat.send_message("how many states are in india")

print(response.text)