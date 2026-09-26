from ollama import chat


TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "browser_open_website",
            "description": (
                "Open a website in the user's browser. "
                "Use this when the user explicitly asks to open "
                "or visit a website."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "The complete URL to open."
                    }
                },
                "required": ["url"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": (
                "Get the user's current local time. "
                "Use this when the user asks what time it is."
            ),
            "parameters": {
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    }
]


messages = [
    {
        "role": "system",
        "content": """
You are a personal voice assistant.

You have tools.

When the user explicitly asks you to open a website,
you MUST call browser_open_website.

When the user explicitly asks for the current time,
you MUST call get_current_time.

Do not answer these requests yourself.
Use the appropriate tool.
"""
    },
    {
        "role": "user",
        "content": "open youtube"
    }
]


response = chat(
    model="qwen3.5:4b",
    messages=messages,
    tools=TOOLS,
    think=False,
)

print("\n==============================")
print("CONTENT:")
print(repr(response.message.content))

print("\nTOOL CALLS:")
print(response.message.tool_calls)

print("\nFULL MESSAGE:")
print(response.message)
print("==============================")