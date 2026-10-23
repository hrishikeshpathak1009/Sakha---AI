# SAAKHAA — A Personal Agentic AI Assistant

<p align="center">
  <strong>Building intelligence beyond conversation.</strong>
</p>

<p align="center">
  A personal AI assistant that listens, reasons, selects tools, and performs tasks in the digital environment.
</p>

---

## Overview

**SAAKHAA** is a personal agentic AI assistant built with Python that aims to go beyond traditional conversational AI. Instead of simply generating text in response to a prompt, SAAKHAA can understand user requests, reason about tasks, select appropriate tools, and execute actions through an integrated agent workflow.

Powered by **Ollama, LangGraph, Playwright, and IndicVoice**, SAAKHAA combines local language-model inference, tool orchestration, browser automation, speech recognition, and text-to-speech into a unified assistant.

The goal is to build an assistant that can interact with the digital world, automate repetitive activities, and provide a natural voice-driven interface.

> **SAAKHAA is an evolving personal AI project** focused on agentic reasoning, tool use, voice interaction, and autonomous task execution.

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

SAAKHAA connects voice input, agent reasoning, tools, and spoken output in a single workflow.

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
SAAKHAA/
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

Some filenames and modules may change as development progresses. The actual entry point should be the file configured for the current version of SAAKHAA.

## ⚙️ Prerequisites

Before running SAAKHAA, make sure you have:

- Python installed, preferably a version compatible with all the project's dependencies.
- [Ollama](https://ollama.com/) installed and running.
- A compatible language model downloaded through Ollama.
- A working microphone and audio output device.
- Internet access for online speech recognition and browser-based services, where required.
- Playwright's browser dependencies installed.

**Note:** IndicVoice and audio dependencies may require additional operating-system packages or configuration. Follow the installation instructions for the versions used by your environment.

## 🚀 Installation and Setup

### 1. Clone the repository

Replace the placeholder with the URL of your GitHub repository.

```bash
git clone https://github.com/YOUR_USERNAME/SAAKHAA.git
cd SAAKHAA
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install Python dependencies

If the repository includes `requirements.txt`:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If the dependency file is not yet complete, install the packages required by the current implementation. These may include:

```bash
pip install langgraph langchain-ollama ollama playwright SpeechRecognition sounddevice numpy python-dotenv
```

IndicVoice should be installed according to its official package or repository instructions. Package names and installation methods can vary between releases.

### 4. Install the browser runtime

Install Playwright's Chromium browser:

```bash
python -m playwright install chromium
```

If Playwright reports missing operating-system dependencies, install those according to its documentation.

### 5. Set up Ollama

Start Ollama and download the model configured in the project.

For example, if the current code uses `qwen3.5:4b`:

```bash
ollama pull qwen3.5:4b
```

Check that the model is available:

```bash
ollama list
```

Make sure the model name in `graph.py` matches the model you downloaded. The example above is not a requirement to use a particular model.

### 6. Configure environment variables

If your code uses environment variables, create a local `.env` file using the variable names expected by the application.

For example:

```env
OLLAMA_MODEL=qwen3.5:4b
```

Only add variables that your code actually reads. If the model name is hardcoded in the source, either update it there or modify the application to read the environment variable.

Never commit API keys, passwords, tokens, or other private credentials.

### 7. Run SAAKHAA

Run the main entry point used by your current version. For example:

```bash
python main-current.py
```

If your repository uses `main.py` instead, run:

```bash
python main.py
```

Ensure Ollama is running, the model is available, and the microphone and audio devices are configured correctly before starting a voice session.

## 🎙️ Example Commands

Once the assistant is running, you can try natural-language requests such as:

| Category | Example command |
|---|---|
| Website navigation | "Open Google." |
| Web search | "Search Google for photos of a lion." |
| YouTube search | "Open YouTube and search for Bollywood songs." |
| Video playback | "Play the first video." |
| Browser control | "Close the browser." |
| General conversation | "Explain how neural networks work." |

The commands available to the assistant depend on the tools registered in the current version.

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

SAAKHAA's voice interaction consists of three primary stages:

**1. Speech recognition**

The listening and recognition modules capture spoken input and convert it into text. The recognition service and its network requirements depend on the configured implementation.

**2. Agent processing**

The recognized text is passed to the agent. The model can answer directly or invoke tools to perform an action.

**3. Text-to-speech**

The generated response is passed to IndicVoice, and the resulting audio is played through the configured audio output device.

Speech generation, model inference, network requests, and audio playback can all affect response latency. Optimizing these components independently makes it easier to identify performance bottlenecks.

## 🌐 Browser Automation

SAAKHAA uses Playwright to interact with web pages.

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

## 🔐 Security and Privacy

SAAKHAA can interact with websites, process voice input, and perform actions through registered tools. These capabilities should be used responsibly.

- Keep `.env` files and private credentials out of version control.
- Exclude virtual environments, caches, logs, and browser profiles from the repository.
- Review tool implementations before allowing sensitive operations.
- Require confirmation for destructive or security-sensitive actions.
- Use timeouts and error handling for browser and system operations.
- Avoid logging private voice transcripts, credentials, or sensitive browser content unnecessarily.
- Be aware that speech recognition and online websites may send data to external services.
- Local language-model inference does not automatically make the entire assistant fully offline.

SAAKHAA should not execute arbitrary commands or perform consequential actions without appropriate safeguards.

## 🛠️ Troubleshooting

### Ollama connection errors

- Ensure Ollama is installed and running.
- Confirm that the configured model exists using `ollama list`.
- Verify that the model name in the code matches the downloaded model.
- Check the local Ollama service configuration.

### Playwright browser does not launch

Run:

```bash
python -m playwright install chromium
```

Check the terminal output for missing dependencies, profile-lock errors, or browser installation problems.

### Browser tools time out

- Confirm that the intended page is open.
- Verify that the target element exists on the current page.
- Add appropriate locator timeouts.
- Handle missing search results and navigation failures.
- Avoid assuming that every website uses the same page structure.

### Speech recognition fails

- Verify that a microphone is connected and accessible.
- Check microphone permissions.
- Confirm network access if using online speech recognition.
- Handle silence, background noise, and recognition timeouts.

### Text-to-speech fails or playback is choppy

- Confirm that IndicVoice and its model dependencies are installed.
- Verify that the output audio device is available.
- Check the generated audio's sample rate, shape, and data type.
- Avoid unnecessary audio-stream initialization and playback gaps.

### Agent repeats tool calls

- Check the tool descriptions and schemas.
- Ensure tool results are returned in a format the model can understand.
- Add a maximum number of tool-call iterations.
- Make error responses explicit.
- Ensure that the model produces a final answer after successful tool execution.

## 🗺️ Future Development

SAAKHAA is an evolving project. Areas that may be explored include:

- Improved multi-tab browser management.
- More reliable browser lifecycle and cleanup.
- Faster and more natural speech generation.
- Better handling of tool errors and timeouts.
- More robust agent iteration limits and tool-result processing.
- Improved conversational memory and state management.
- Additional system and application integrations.
- Better observability, testing, and performance profiling.
- More explicit confirmation and permission controls for sensitive actions.

These are development directions, not a claim that every capability is already implemented.

---

<p align="center">
  <strong>SAAKHAA</strong><br/>
  A personal agentic AI assistant.
</p>
