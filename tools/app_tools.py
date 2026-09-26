import os
import subprocess


# =========================================================
# SUPPORTED APPLICATIONS
# =========================================================

APPLICATIONS = {
    "notepad": {
        "open": "notepad.exe",
        "close": "notepad.exe",
    },

    "calculator": {
        "open": "calc.exe",
        "close": "CalculatorApp.exe",
    },

    "paint": {
        "open": "mspaint.exe",
        "close": "mspaint.exe",
    },

    "file explorer": {
        "open": "explorer.exe",
        "close": "explorer.exe",
    },

    "explorer": {
        "open": "explorer.exe",
        "close": "explorer.exe",
    },

    "chrome": {
        "open": "chrome.exe",
        "close": "chrome.exe",
    },

    "edge": {
        "open": "msedge.exe",
        "close": "msedge.exe",
    },

    "vscode": {
        "open": "code",
        "close": "Code.exe",
    },
}


# =========================================================
# OPEN APPLICATION
# =========================================================

def open_application(application: str):
    """
    Open a supported Windows application.

    Use ONLY when the user explicitly asks SAAKHAA to:
    - open an application
    - launch an application
    - start an application

    Examples:
    "Open Notepad"
    "Launch Calculator"
    "Open VS Code"
    "Start Paint"

    Do NOT open an application merely because its name
    appears in the conversation.

    Supported applications include:
    Notepad, Calculator, Paint, File Explorer,
    Chrome, Edge, and VS Code.
    """

    application = application.lower().strip()

    app = APPLICATIONS.get(application)

    if app is None:
        supported = ", ".join(APPLICATIONS.keys())

        return (
            f"I don't have an action for {application}. "
            f"Supported applications are {supported}."
        )

    try:
        os.startfile(app["open"])

        return f"Opened {application}."

    except Exception as e:
        return f"I couldn't open {application}: {e}"


# =========================================================
# CLOSE APPLICATION
# =========================================================

def close_application(application: str):
    """
    Close a supported Windows application.

    Use ONLY when the user explicitly asks SAAKHAA to:
    - close an application
    - quit an application
    - exit an application
    - shut down an application

    Examples:
    "Close Notepad"
    "Quit Calculator"
    "Close VS Code"
    "Exit Paint"

    IMPORTANT:
    Do NOT use this tool for:
    - closing SAAKHAA
    - closing the browser managed by Playwright
    - pausing YouTube
    - stopping SAAKHAA

    The user must explicitly identify the application
    they want closed.
    """

    application = application.lower().strip()

    app = APPLICATIONS.get(application)

    if app is None:
        supported = ", ".join(APPLICATIONS.keys())

        return (
            f"I don't have an action for closing {application}. "
            f"Supported applications are {supported}."
        )

    process = app["close"]

    try:
        result = subprocess.run(
            ["taskkill", "/IM", process, "/F"],
            capture_output=True,
            text=True,
        )

        if result.returncode == 0:
            return f"Closed {application}."

        return f"{application} does not appear to be running."

    except Exception as e:
        return f"I couldn't close {application}: {e}"


# =========================================================
# APPLICATION TOOL REGISTRY
# =========================================================

APP_TOOLS = {
    "open_application": open_application,
    "close_application": close_application,
}