import datetime
import platform
import psutil


# =========================================================
# CURRENT TIME
# =========================================================

def get_current_time():
    """
    Get the current local time.

    Use ONLY when the user explicitly asks:
    - What time is it?
    - Tell me the current time.
    - What's the time?

    Do NOT use this for unrelated questions.
    """

    current_time = datetime.datetime.now().strftime("%I:%M %p")

    return f"The current time is {current_time}."


# =========================================================
# CURRENT DATE
# =========================================================

def get_current_date():
    """
    Get today's local date.

    Use ONLY when the user explicitly asks:
    - What is today's date?
    - What day is it?
    - Tell me today's date.

    Do NOT use this for unrelated questions.
    """

    current_date = datetime.datetime.now().strftime(
        "%A, %d %B %Y"
    )

    return f"Today is {current_date}."


# =========================================================
# BATTERY
# =========================================================

def get_battery_status():
    """
    Get the computer's current battery percentage and
    charging status.

    Use when the user explicitly asks:
    - What's my battery?
    - How much battery do I have?
    - Is my laptop charging?
    - Check my battery.
    """

    battery = psutil.sensors_battery()

    if battery is None:
        return "I could not detect a battery on this computer."

    percentage = round(battery.percent)

    if battery.power_plugged:
        status = "and the computer is charging."
    else:
        status = "and the computer is running on battery."

    return f"The battery is at {percentage} percent {status}"


# =========================================================
# SYSTEM INFORMATION
# =========================================================

def get_system_info():
    """
    Get basic information about the computer.

    Use ONLY when the user explicitly asks about:
    - computer information
    - system information
    - operating system
    - processor/platform information

    Returns basic OS and processor information.
    """

    system = platform.system()
    release = platform.release()
    machine = platform.machine()
    processor = platform.processor()

    return (
        f"Operating system: {system} {release}. "
        f"Architecture: {machine}. "
        f"Processor: {processor}."
    )


# =========================================================
# CPU USAGE
# =========================================================

def get_cpu_usage():
    """
    Get the current CPU utilization.

    Use ONLY when the user explicitly asks:
    - How much CPU am I using?
    - Check CPU usage.
    - What is my CPU usage?
    """

    usage = psutil.cpu_percent(interval=1)

    return f"Current CPU usage is {usage} percent."


# =========================================================
# RAM / MEMORY USAGE
# =========================================================

def get_memory_usage():
    """
    Get current RAM usage.

    Use ONLY when the user explicitly asks:
    - How much RAM am I using?
    - Check memory usage.
    - How much memory is being used?
    """

    memory = psutil.virtual_memory()

    used_gb = memory.used / (1024 ** 3)
    total_gb = memory.total / (1024 ** 3)
    percentage = memory.percent

    return (
        f"You are using {used_gb:.1f} GB "
        f"out of {total_gb:.1f} GB of RAM, "
        f"which is {percentage} percent."
    )


# =========================================================
# DISK USAGE
# =========================================================

def get_disk_usage():
    """
    Get storage usage of the main Windows drive.

    Use ONLY when the user explicitly asks:
    - How much storage do I have?
    - Check disk space.
    - How much space is left?
    """

    disk = psutil.disk_usage("C:\\")

    total_gb = disk.total / (1024 ** 3)
    used_gb = disk.used / (1024 ** 3)
    free_gb = disk.free / (1024 ** 3)

    return (
        f"The C drive has {total_gb:.1f} GB total, "
        f"{used_gb:.1f} GB used, "
        f"and {free_gb:.1f} GB free."
    )


# =========================================================
# SYSTEM TOOL REGISTRY
# =========================================================

SYSTEM_TOOLS = {
    "get_current_time": get_current_time,
    "get_current_date": get_current_date,
    "get_battery_status": get_battery_status,
    "get_system_info": get_system_info,
    "get_cpu_usage": get_cpu_usage,
    "get_memory_usage": get_memory_usage,
    "get_disk_usage": get_disk_usage,
}