# Board detection logic
import platform

def detect_board():
    system = platform.system()
    if system == "Linux":
        return "Raspberry Pi"
    elif system == "Darwin":
        return "MacBook"
    else:
        return "Unknown"