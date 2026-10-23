# SAKHA — A Personal Agentic AI Assistant

<p align="center">
  <strong>Building intelligence beyond conversation.</strong>
</p>

<p align="center">
  A personal AI assistant that listens, reasons, selects tools, and performs tasks in the digital environment.
</p>

---

## Overview

**SAKHA** is a personal agentic AI assistant built with Python that aims to go beyond traditional conversational AI. Instead of simply generating text in response to a prompt, SAKHA can understand user requests, reason about tasks, select appropriate tools, and execute actions through an integrated agent workflow.

Powered by **Ollama, LangGraph, Playwright, and IndicVoice**, SAKHA combines local language-model inference, tool orchestration, browser automation, speech recognition, and text-to-speech into a unified assistant.

The goal is to build an assistant that can interact with the digital world, automate repetitive activities, and provide a natural voice-driven interface.

> **SAKHA is an evolving personal AI project** focused on agentic reasoning, tool use, voice interaction, and autonomous task execution.

## ✨ Key Features

### 🧠 Agentic AI and Tool Calling
- Understands natural-language requests.
- Uses an LLM to determine appropriate actions.
- Selects and invokes available tools based on the task.
- Processes tool results to formulate responses.
- Uses LangGraph to organize the agent workflow and conversation state.

### 🗣️ Voice Interaction
- Accepts spoken commands through a microphone.
- Converts speech into text for processing.
- Generates spoken responses using IndicVoice.
- Integrates speech recognition, reasoning, and speech synthesis into a single interaction loop.

### 🌐 Browser Automation
- Opens websites using Playwright.
- Navigates to requested pages.
- Performs browser-based actions through registered tools.
- Supports website-specific workflows, including search and video interaction.
- Maintains a persistent Chromium browser profile where configured.

### ▶️ YouTube Automation
- Searches YouTube for requested content.
- Opens videos through browser automation.
- Supports playing the first video in search results.
- Connects YouTube actions to the agent's tool-calling workflow.

### 💻 System and Application Tools
- Integrates tools for supported desktop and system operations.
- Can be extended with additional actions as the project evolves.
- Uses a tool-based architecture to separate action execution from the language model.

### 💬 Conversation State
- Uses LangGraph state management to organize interactions.
- Supports conversation checkpointing through `MemorySaver`, where configured.
- Provides a foundation for maintaining conversational context across turns.

### 🧩 Modular Architecture
- Separates speech input, speech output, agent orchestration, and tool execution.
- Keeps browser automation logic separate from the main interaction loop.
- Allows new capabilities to be integrated as additional tools.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application and tool implementation |
| Ollama | Local language-model runtime |
| Qwen | Language model used during development |
| LangGraph | Agent orchestration and state management |
| Playwright | Browser automation |
| SpeechRecognition | Speech input and recognition |
| IndicVoice | Text-to-speech generation |
| SoundDevice | Audio playback |
| NumPy | Audio-array processing |
| Chromium | Browser automation runtime |

*The exact dependencies and supported capabilities depend on the current project files and installed package versions.*

## 🏗️ Architecture

SAKHA connects voice input, agent reasoning, tools, and spoken output in a single workflow.

```text
                    ┌──────────────────────┐
                    │         USER         │
                    │   Voice / Commands    │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Speech Input      │
                    │  Listen + Recognize  │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   Agent Orchestrator │
                    │      LangGraph       │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Ollama + LLM     │
                    │ Reasoning + Tool Use │
                    └──────────┬───────────┘
                               │
                       Tool selection
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Tool Registry    │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       ┌────────────┐   ┌────────────┐   ┌────────────┐
       │   Browser  │   │  YouTube   │   │   System   │
       │ Automation │   │   Tools    │   │   Tools    │
       └──────┬─────┘   └──────┬─────┘   └──────┬─────┘
              └────────────────┼────────────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │     Tool Results     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Final Response   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   IndicVoice + Audio │
                    │     Text-to-Speech   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Spoken Response  │
                    └──────────────────────┘
```

### How the agent works

1. **Input:** The user speaks a command or provides text.
2. **Recognition:** The speech input pipeline converts the command into text.
3. **Reasoning:** The language model interprets the request and determines whether a tool is needed.
4. **Action:** LangGraph orchestrates tool selection and execution.
5. **Observation:** The agent receives the tool result and uses it to continue processing the request.
6. **Response:** The assistant produces a final answer.
7. **Speech:** IndicVoice converts the answer into audio for playback.

This architecture separates the language model's reasoning from the code that performs actions. The model requests tools, while the corresponding Python functions carry them out.

## 📁 Project Structure

The following is a representative structure. Keep the names aligned with the actual files in your repository.

```text
SAKHA/
│
├── main-current.py       # Main assistant interaction loop
├── graph.py              # LangGraph agent and model orchestration
├── state.py              # Agent state definitions
│
├── listen.py             # Microphone input
├── speechr.py             # Speech recognition
├── bolo.py                # Text-to-speech and audio playback
├── ai.py                  # Additional or earlier AI implementation
├── browser.py             # Browser automation logic
│
├── tools/
│   ├── __init__.py        # Tool registration and exports
│   ├── browser_tools.py   # Browser-related actions
│   ├── youtube_tools.py   # YouTube actions
│   └── ...                # Other available tools
│
├── testgraph.py           # Agent testing
├── testbrowser.py         # Browser testing
├── testbolo.py            # Voice testing
│
├── requirements.txt       # Python dependencies
├── .env                   # Local environment configuration
├── .gitignore             # Files excluded from Git
└── README.md
```


## 🧠 Agent Orchestration

LangGraph provides the framework for coordinating the assistant's reasoning and actions.

The intended workflow is:

```text
User Request
     │
     ▼
Language Model
     │
     ├── Direct answer ───────────► Final Response
     │
     └── Tool call
             │
             ▼
        Tool Execution
             │
             ▼
         Tool Result
             │
             ▼
      Model processes result
             │
             ▼
       Final Response
```

The language model does not directly control the browser or operating system. It requests an available tool, and the Python implementation executes the operation.

LangGraph state and checkpointing can help maintain conversation context. The exact persistence behavior depends on how the graph and checkpointer are configured.

## 🔊 Voice Pipeline

SAKHA's voice interaction consists of three primary stages:

**1. Speech recognition**

The listening and recognition modules capture spoken input and convert it into text. The recognition service and its network requirements depend on the configured implementation.

**2. Agent processing**

The recognized text is passed to the agent. The model can answer directly or invoke tools to perform an action.

**3. Text-to-speech**

The generated response is passed to IndicVoice, and the resulting audio is played through the configured audio output device.

Speech generation, model inference, network requests, and audio playback can all affect response latency. Optimizing these components independently makes it easier to identify performance bottlenecks.

## 🌐 Browser Automation

SAKHA uses Playwright to interact with web pages.

The browser automation layer can manage a Chromium session, navigate to websites, locate page elements, and execute supported actions.

Browser behavior depends on the current page, loaded content, browser state, and available tool implementations.

### Browser lifecycle

Browser operations should be handled carefully:

- Start the browser only when a browser operation is required.
- Reuse the existing session when appropriate.
- Preserve browser state between requests when the user expects it.
- Close the browser only when explicitly requested or when cleanup is necessary.
- Handle timeouts and missing page elements gracefully.
- Clean up Playwright resources when the application shuts down.

Persistent browser profiles can preserve login sessions and cookies. Treat them as sensitive local data.

