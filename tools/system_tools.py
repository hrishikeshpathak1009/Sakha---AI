import datetime
import os


def get_current_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")

    return f"Sir, The current time is {current_time}."


def get_current_date():
    current_date = datetime.datetime.now().strftime("%A, %d %B %Y")

    return f"Sir, Today is {current_date}."


def open_application(application):
    applications = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
    }

    program = applications.get(application.lower())

    if program is None:
        return f"I don't know how to open {application}."

    os.startfile(program)

    return f"Opened {application}."