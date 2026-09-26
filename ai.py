import os
import json
from dotenv import load_dotenv

from google import genai
from google.genai import types

from ollama import chat

from tools import TOOL_FUNCTIONS


load_dotenv()


# ============================================================
# CONFIGURATION
# ============================================================

# Change this whenever you want:
#
# "ollama" -> local Qwen
# "gemini" -> Gemini API
#
AI_PROVIDER = "ollama"

OLLAMA_MODEL = "qwen3.5:4b"

GEMINI_MODEL = "gemini-3.6-flash"


# ============================================================
# GEMINI SETUP
# ============================================================

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)


gemini_tools = [
    types.Tool(
        function_declarations=[

            types.FunctionDeclaration(
                name="browser_open_website",
                description="Open a website in SAAKHAA's browser.",
                parameters=types.Schema(
                    type=types.Type.OBJECT,
                    properties={
                        "url": types.Schema(
                            type=types.Type.STRING,
                            description="The complete URL to open."
                        )
                    },
                    required=["url"]
                )
            ),

            types.FunctionDeclaration(
                name="browser_search_youtube",
                description="Search YouTube for a given query.",
                parameters=types.Schema(
                    type=types.Type.OBJECT,
                    properties={
                        "query": types.Schema(
                            type=types.Type.STRING,
                            description="What to search for on YouTube."
                        )
                    },
                    required=["query"]
                )
            ),

            types.FunctionDeclaration(
                name="browser_play_first_video",
                description="Play the first video in the current YouTube search results.",
                parameters=types.Schema(
                    type=types.Type.OBJECT,
                    properties={}
                )
            ),

            types.FunctionDeclaration(
                name="get_current_time",
                description="Get the user's current local time.",
                parameters=types.Schema(
                    type=types.Type.OBJECT,
                    properties={}
                )
            ),

            types.FunctionDeclaration(
                name="get_current_date",
                description="Get the current date.",
                parameters=types.Schema(
                    type=types.Type.OBJECT,
                    properties={}
                )
            ),

            types.FunctionDeclaration(
                name="open_application",
                description="Open a supported application on the user's computer.",
                parameters=types.Schema(
                    type=types.Type.OBJECT,
                    properties={
                        "application": types.Schema(
                            type=types.Type.STRING,
                            description="The application to open, such as notepad, calculator, or paint."
                        )
                    },
                    required=["application"]
                )
            )
        ]
    )
]


# ============================================================
# SHARED TOOL EXECUTION
# ============================================================

def execute_tool(function_name, arguments):

    function = TOOL_FUNCTIONS.get(function_name)

    if function is None:
        print(f"Unknown tool: {function_name}")
        return f"Tool {function_name} is not available."

    print(f"Executing tool: {function_name}")
    print(f"Arguments: {arguments}")

    try:
        result = function(**arguments)

        print(f"Tool result: {result}")

        return result

    except Exception as e:
        print(f"Tool error: {e}")
        return f"Tool failed: {e}"


# ============================================================
# GEMINI
# ============================================================

def ask_gemini(prompt):

    try:

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                tools=gemini_tools
            )
        )

        if not response.candidates:
            return "I didn't receive a response."

        parts = response.candidates[0].content.parts

        for part in parts:

            if part.function_call:

                function_call = part.function_call

                print(
                    f"Gemini selected tool: {function_call.name}"
                )

                arguments = dict(function_call.args)

                result = execute_tool(
                    function_call.name,
                    arguments
                )

                return str(result)

        return response.text

    except Exception as e:

        print(f"Gemini Error: {e}")

        return (
            "Sorry, I am unable to reach Gemini right now."
        )


# ============================================================
# OLLAMA SYSTEM PROMPT
# ============================================================

OLLAMA_SYSTEM_PROMPT = """
You are SAAKHAA, a fast personal voice assistant.

You are running locally using Ollama.

Rules:

- Give concise answers suitable for speech.
- For simple questions, answer in 1-3 sentences.
- Do not repeat the user's question.
- Do not give unnecessary explanations.
- Use tools whenever a tool is appropriate.
- Never pretend that a tool was executed if it wasn't.
- Do not invent facts.
- If you don't know something, say so.
- Keep responses natural and easy to speak aloud.

Available tools include:
- opening websites
- searching YouTube
- playing YouTube videos
- getting the current time
- getting the current date
- opening supported applications
"""


# ============================================================
# OLLAMA TOOLS
# ============================================================

ollama_tools = [

    {
        "type": "function",
        "function": {
            "name": "browser_open_website",
            "description": "Open a website in SAAKHAA's browser.",
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
            "name": "browser_search_youtube",
            "description": "Search YouTube for a given query.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "What to search for on YouTube."
                    }
                },
                "required": ["query"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "browser_play_first_video",
            "description": "Play the first video in the current YouTube search results.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Get the user's current local time.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_current_date",
            "description": "Get the current date.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "open_application",
            "description": "Open a supported application on the user's computer.",
            "parameters": {
                "type": "object",
                "properties": {
                    "application": {
                        "type": "string",
                        "description": "Application to open, such as notepad, calculator, or paint."
                    }
                },
                "required": ["application"]
            }
        }
    }
]


# ============================================================
# OLLAMA
# ============================================================

def ask_ollama(prompt):

    messages = [
        {
            "role": "system",
            "content": OLLAMA_SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

    try:

        # First request
        response = chat(
            model=OLLAMA_MODEL,
            messages=messages,
            tools=ollama_tools,
            think=False,
            options={
                "num_predict": 150
            }
        )

        # Add assistant's response to conversation
        messages.append(response.message)

        # Check for tool calls
        tool_calls = response.message.tool_calls

        if tool_calls:

            for tool_call in tool_calls:

                function_name = tool_call.function.name
                arguments = tool_call.function.arguments

                print(
                    f"Ollama selected tool: {function_name}"
                )

                result = execute_tool(
                    function_name,
                    arguments
                )

                # Send tool result back to Ollama
                messages.append({
                    "role": "tool",
                    "content": str(result)
                })

            # Ask Ollama to formulate the final answer
            final_response = chat(
                model=OLLAMA_MODEL,
                messages=messages,
                think=False,
                options={
                    "num_predict": 150
                }
            )

            return final_response.message.content

        # Normal response
        return response.message.content

    except Exception as e:

        print(f"Ollama Error: {e}")

        return (
            "Sorry, I encountered an error with my local intelligence system."
        )


# ============================================================
# MAIN AI ROUTER
# ============================================================

def ask_ai(prompt):

    if AI_PROVIDER == "ollama":

        return ask_ollama(prompt)

    elif AI_PROVIDER == "gemini":

        return ask_gemini(prompt)

    else:

        return f"Unknown AI provider: {AI_PROVIDER}"