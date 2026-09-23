import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from tools import TOOL_FUNCTIONS

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

tools = [
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
            )
        ]
    )
]


chat = client.chats.create(
    model="gemini-3.5-flash-lite"
)


def execute_tool(function_call):

    function_name = function_call.name
    arguments = dict(function_call.args)

    function = TOOL_FUNCTIONS.get(function_name)

    if function is None:
        print(f"Unknown tool: {function_name}")
        return None

    print(f"Executing tool: {function_name}")
    print(f"Arguments: {arguments}")

    return function(**arguments)

def ask_ai(prompt):
    try:
        

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                tools=tools
            )
        )

        function_call = response.candidates[0].content.parts[0].function_call

        if function_call:

            print(
                f"Gemini selected tool: {function_call.name}"
            )

            result = execute_tool(function_call)

            return result

        return response.text

        

    except Exception as e:
        print(f"Gemini Error: {e}")
        return (
            "Sorry, I am unable to reach my intelligence system right now. "
            "Is there something else I can help you with?"
        )