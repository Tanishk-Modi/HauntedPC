import subprocess
import time
import pyautogui
import random

spooky_messages = [
    "GET OUT",
    "YOU ARE NEXT",
    "CAN YOU HEAR ME",
    "ITS BEHIND YOU",
    "I AM WATCHING",
    "HELP ME"
]

def open_notepad():
    subprocess.Popen(['notepad.exe'])
    time.sleep(2) # Give notepad time to open

def focus_notepad():
    notepad_window = None
    # Loop to give time for Notepad to appear in window list
    for _ in range(5):
        windows = pyautogui.getWindowsWithTitle("Untitled")
        if windows:
            notepad_window = windows[0] # Get the matching window
            break
        time.sleep(0.5)
    
    if notepad_window:
        notepad_window.activate()
        time.sleep(0.2)
        return True
    else:
        print("Couldn't find window")
        return False
    
def type_spooky_message():
    chosen_message = random.choice(spooky_messages)
    pyautogui.typewrite(chosen_message, interval=0.3) # Interval calculates typing speed
    time.sleep(1)

def perform_typing_haunting():
    open_notepad()
    if focus_notepad(): # Only proceed if Notepad was found and focused
        type_spooky_message()
    else:
        print("Skip typing sequence")
