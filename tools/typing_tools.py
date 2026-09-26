import time
import pyautogui
import pyperclip


# =========================================================
# TYPE TEXT
# =========================================================

def type_text(text: str):
    """
    Type or paste the requested text into the application
    that currently has keyboard focus.

    Use ONLY when the user explicitly asks SAAKHAA to:
    - type something
    - write something into the current application
    - enter text
    - paste text
    - dictate text into the active cursor

    Examples:
    "Type hello world"
    "Write this in Notepad: Hello everyone"
    "Type my name"
    "Paste this text"

    The text is inserted at the currently active cursor.

    IMPORTANT:
    Do NOT use this tool merely because the user asks SAAKHAA
    to write an answer. Use it only when the user wants the
    text physically entered into the computer.
    """

    if not text:
        return "There is no text to type."

    try:
        # Copy text to Windows clipboard
        pyperclip.copy(text)

        # Small delay to make sure clipboard is ready
        time.sleep(0.1)

        # Paste into currently focused application
        pyautogui.hotkey("ctrl", "v")

        return "Typed the requested text."

    except Exception as e:
        return f"I couldn't type the text: {e}"


# =========================================================
# PRESS ENTER
# =========================================================

def press_enter():
    """
    Press the Enter key in the currently focused application.

    Use ONLY when the user explicitly asks:
    - press Enter
    - hit Enter
    - submit
    - enter
    """

    try:
        pyautogui.press("enter")
        return "Pressed Enter."

    except Exception as e:
        return f"I couldn't press Enter: {e}"


# =========================================================
# BACKSPACE
# =========================================================

def press_backspace():
    """
    Press Backspace in the currently focused application.

    Use ONLY when the user explicitly asks to:
    - press Backspace
    - delete the previous character
    - backspace
    """

    try:
        pyautogui.press("backspace")
        return "Pressed Backspace."

    except Exception as e:
        return f"I couldn't press Backspace: {e}"


# =========================================================
# SELECT ALL
# =========================================================

def select_all():
    """
    Select all text in the currently focused application.

    Use ONLY when the user explicitly asks:
    - select all
    - select everything
    """

    try:
        pyautogui.hotkey("ctrl", "a")
        return "Selected all."

    except Exception as e:
        return f"I couldn't select all: {e}"


# =========================================================
# COPY
# =========================================================

def copy_selection():
    """
    Copy the currently selected text to the clipboard.

    Use ONLY when the user explicitly asks:
    - copy
    - copy this
    - copy the selection
    """

    try:
        pyautogui.hotkey("ctrl", "c")
        return "Copied the selection."

    except Exception as e:
        return f"I couldn't copy the selection: {e}"


# =========================================================
# PASTE
# =========================================================

def paste_clipboard():
    """
    Paste the current clipboard contents into the focused
    application.

    Use ONLY when the user explicitly asks:
    - paste
    - paste it
    - paste the clipboard
    """

    try:
        pyautogui.hotkey("ctrl", "v")
        return "Pasted the clipboard contents."

    except Exception as e:
        return f"I couldn't paste: {e}"


# =========================================================
# NEW LINE
# =========================================================

def press_newline():
    """
    Insert a new line by pressing Enter.

    Use ONLY when the user explicitly asks for:
    - a new line
    - next line
    - line break
    """

    try:
        pyautogui.press("enter")
        return "Created a new line."

    except Exception as e:
        return f"I couldn't create a new line: {e}"


# =========================================================
# TYPING TOOL REGISTRY
# =========================================================

TYPING_TOOLS = {
    "type_text": type_text,
    "press_enter": press_enter,
    "press_backspace": press_backspace,
    "select_all": select_all,
    "copy_selection": copy_selection,
    "paste_clipboard": paste_clipboard,
    "press_newline": press_newline,
}