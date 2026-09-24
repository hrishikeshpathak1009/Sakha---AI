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
- Keep responses natural and easy to speak aloud.
"""

def ask_ai(text):
    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": text
            }
        ],
        think=False,
        options={
            "num_predict": 100
        }
    )

    return response.message.content


if __name__ == "__main__":
    while True:
        text = input("You: ").strip()

        if text.lower() in {"exit", "quit","stop","power off"}:
            break

        answer = ask_ai(text)
        #print("SAAKHAA:", answer)
