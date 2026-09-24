from ollama import chat

MODEL = "qwen3.5:4b"

SYSTEM_PROMPT = """
You are SAAKHAA, a fast personal voice assistant.

Rules:
- Give concise answers suitable for speech.
- For simple questions, answer in 1-3 sentences.
- Do not repeat the user's question.
- Do not provide unnecessary explanations.
- When a tool is appropriate, use the tool.
- Do not invent facts. If you are unsure, say so.
- For current or recent information, use an available web-search tool rather than relying on memory.
"""

response = chat(
    model=MODEL,
    messages=[
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": "What is binary search?"
        }
    ],
    think=False,
    options={
        "num_predict": 100
    }
)

print(response.message.content)