from typing import Literal

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

from ollama import chat

from state import SaakhaaState
from tools import TOOL_FUNCTIONS


# ============================================================
# MODEL
# ============================================================

MODEL = "qwen3.5:4b"


# ============================================================
# SYSTEM PROMPT
# ============================================================
SYSTEM_PROMPT = """
You are SAAKHAA, a personal AI voice assistant.

IDENTITY
- Your name is SAAKHAA.
- You are the user's personal assistant.
- Be calm, intelligent, concise, and natural.
- Speak like a helpful human assistant, not like a chatbot reading an essay.

CONVERSATION
- Use the conversation history when it is relevant.
- Remember information provided earlier in the current conversation.
- Understand references such as "it", "that", "there", "him", and "what I said earlier" using conversation context.
- If the user tells you personal information, acknowledge it naturally.
- Do not repeatedly ask for information that is already available in the conversation.
- Never claim to remember something that is not present in your available context.

RESPONSE STYLE
- This is a voice assistant, so responses must be easy to speak aloud.
- Keep normal answers to 1-3 sentences.
- Prefer direct answers over explanations.
- Do not repeat the user's question.
- Do not use markdown, bullet points, headings, emojis, or formatting unless specifically requested.
- Avoid unnecessary filler such as "Sure!", "Absolutely!", "Of course!".
- Do not narrate your reasoning.
- If the answer is uncertain, say so briefly.

TOOLS
You have access to tools that can interact with the user's computer and browser.

IMPORTANT:
- Only use a tool when the user's request actually requires that tool.
- Do not call a tool merely because a person, website, application, place, or topic was mentioned.
- Do not invent tool calls.
- Do not claim that an action was performed unless the corresponding tool was actually executed successfully.
- If a tool fails, honestly tell the user that the action failed. Do not pretend it succeeded.

BROWSER
- Use browser_open_website when the user explicitly asks you to open, visit, or navigate to a website.
- Use browser_search_youtube only when the user explicitly asks to search/find something on YouTube.
- Use browser_play_first_video only when the user asks to play the first/current YouTube result.
- If the user says "open YouTube", open https://www.youtube.com.
- If the user says "open Google", open https://www.google.com.
- Do not search YouTube for ordinary conversation.

APPLICATIONS
- Use open_application only when the user explicitly asks you to open an application.
- Supported applications include notepad, calculator, and paint.
- Do not open applications based only on a mention of their name.

TIME AND DATE
- Use get_current_time when the user asks for the current time.
- Use get_current_date when the user asks for today's date.
- Do not use these tools for unrelated questions.

TOOL SEQUENCING
- You may use multiple tools when necessary to complete a request.
- After receiving a tool result, evaluate whether another tool is necessary.
- Do not perform unnecessary tool calls.
- After completing the requested action, give a brief natural response.

PERSONALITY
- Be helpful without being overly enthusiastic.
- Be confident when the information is clear.
- Be honest when something is unknown or failed.
- Address the user naturally.
- Do not call the user "Sir" unless the user explicitly prefers it.

SAFETY
- Do not perform actions that were not requested.
- Before potentially consequential actions, make sure the user's request is clear.
- Never fabricate information, tool results, or actions.

Your primary goal is to understand what the user wants and accomplish it efficiently with the minimum necessary interaction.
"""
# ============================================================
# TOOL DEFINITIONS FOR OLLAMA
# ============================================================

OLLAMA_TOOLS = [
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
                "properties": {},
                "required": []
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
                "properties": {},
                "required": []
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
                "properties": {},
                "required": []
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
                        "description": "The application to open, such as notepad, calculator, or paint."
                    }
                },
                "required": ["application"]
            }
        }
    }
]


# ============================================================
# LLM NODE
# ============================================================

def call_model(state: SaakhaaState):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(state["messages"])

    response = chat(
        model=MODEL,
        messages=messages,
        tools=OLLAMA_TOOLS,
        think=False,
        options={
            "num_predict": 200
        }
    )

    message = response.message

    result = {
        "role": "assistant",
        "content": message.content or ""
    }

    # --------------------------------------------------------
    # Tool calls
    # --------------------------------------------------------

    if message.tool_calls:

        result["tool_calls"] = []

        for index, tool_call in enumerate(message.tool_calls):

            result["tool_calls"].append({
                "id": f"call_{index}",
                "function": {
                    "name": tool_call.function.name,
                    "arguments": dict(tool_call.function.arguments)
                }
            })

    return {
        "messages": [result]
    }


# ============================================================
# TOOL NODE
# ============================================================

async def execute_tools(state):

    last_message = state["messages"][-1]

    tool_calls = last_message.get("tool_calls", [])

    results = []

    for tool_call in tool_calls:

        function_name = tool_call["function"]["name"]

        arguments = tool_call["function"]["arguments"]

        function = TOOL_FUNCTIONS.get(function_name)

        if function is None:

            result = f"Unknown tool: {function_name}"

        else:

            print(f"Executing tool: {function_name}")
            print(f"Arguments: {arguments}")

            try:

                result = function(**arguments)

                # Async tool
                if hasattr(result, "__await__"):
                    result = await result

            except Exception as e:

                result = f"Tool error: {e}"

        print(f"Tool result: {result}")

        results.append({
            "role": "tool",
            "content": str(result)
        })

    return {
        "messages": results
    }
# ============================================================
# ROUTER
# ============================================================

def should_continue(
    state: SaakhaaState
) -> Literal["tools", END]:

    last_message = state["messages"][-1]

    if last_message.get("tool_calls"):
        return "tools"

    return END


# ============================================================
# BUILD GRAPH
# ============================================================

builder = StateGraph(SaakhaaState)


builder.add_node(
    "assistant",
    call_model
)

builder.add_node(
    "tools",
    execute_tools
)


builder.add_edge(
    START,
    "assistant"
)


builder.add_conditional_edges(
    "assistant",
    should_continue,
    {
        "tools": "tools",
        END: END
    }
)


builder.add_edge(
    "tools",
    "assistant"
)


# ============================================================
# MEMORY
# ============================================================

memory = MemorySaver()


graph = builder.compile(
    checkpointer=memory
)


# ============================================================
# PUBLIC FUNCTION
# ============================================================
async def ask_saakhaa(
    text: str,
    thread_id: str = "main"
):

    result = await graph.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": text
                }
            ]
        },
        config={
            "configurable": {
                "thread_id": thread_id
            }
        }
    )

    return result["messages"][-1]["content"]