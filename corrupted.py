import pyautogui    
import time         
import random     
import tkinter as tk
from tkinter import messagebox 
import threading 
import pythoncom

from haunted_mouse import perform_mouse_haunting
from ghost_typer import perform_typing_haunting
from haunted_visual import perform_visual_haunting
from haunted_error import perform_haunted_error
from haunted_audio import perform_audio_haunting

# -- GLOBAL CONFIGS -- #

MIN_OVERALL_DELAY_SECONDS = 40   # Min seconds between ANY major haunting event
MAX_OVERALL_DELAY_SECONDS = 130  # Max seconds between ANY major haunting event

# --- Overall Haunting Probability ---

MOUSE_EVENT_PROBABILITY = 0.55  
TYPING_EVENT_PROBABILITY = 0.10 
VISUAL_GLITCH_PROBABILITY = 0.15 
ERROR_PROBABILITY = 0.10 
AUDIO_PROBABILITY = 0.10

# --- GLOBAL CONTROL FLAG FOR HAUNTING ---

haunting_active = False 
haunting_thread = None # To hold haunting thread

screen_width, screen_height = pyautogui.size()

# -- MAIN LOOP -- #

def run_haunting_logic():
    global haunting_active 

    # Initialize COM for this thread
    try:
        pythoncom.CoInitialize()
        print("\n--- Haunting Logic Thread: COM Initialized ---")
    except Exception as e:
        print(f"\n--- Haunting Logic Thread: Error initializing COM: {e} ---")

    print("\n--- Haunting Logic Thread Started ---")
    while haunting_active:
        choice = random.random()
        current_prob = 0.0

        # Mouse Movement
        current_prob += MOUSE_EVENT_PROBABILITY
        if choice < current_prob:
            perform_mouse_haunting(screen_width, screen_height)
        # Typing
        elif choice < (current_prob + TYPING_EVENT_PROBABILITY):
            current_prob += TYPING_EVENT_PROBABILITY
            print("\nInitiating typing haunting sequence...")
            perform_typing_haunting()
        # Visual Glitch
        elif choice < (current_prob + VISUAL_GLITCH_PROBABILITY):
            current_prob += VISUAL_GLITCH_PROBABILITY
            print("\nInitiating visual glitch sequence...")
            perform_visual_haunting()
        # Pop-up
        elif choice < (current_prob + ERROR_PROBABILITY):
            current_prob += ERROR_PROBABILITY
            print("\nInitiating fake error pop-up sequence...")
            perform_haunted_error()
        # Audio Haunting
        else:
            print("\nInitiating audio haunting sequence...")
            perform_audio_haunting()

        # After an event, calculate random delay before the next major event
        delay_between_events = random.uniform(MIN_OVERALL_DELAY_SECONDS, MAX_OVERALL_DELAY_SECONDS)
        print(f"\nWaiting for {delay_between_events:.2f} seconds before next major haunting event...\n")
        
        # Check haunting_active frequently during sleep to allow quick stopping
        sleep_start_time = time.time()
        while (time.time() - sleep_start_time) < delay_between_events and haunting_active:
            time.sleep(0.1) # Check every 0.1 seconds

    print("--- Haunting Logic Thread Stopped ---")
    # Clean up audio mixer when haunting stops
    try:
        import pygame
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()
            pygame.mixer.quit() # Clean up mixer resources
    except Exception as e:
        print(f"Error during audio cleanup: {e}")
    
     # NEW: Uninitialize COM for this thread
        try:
            pythoncom.CoUninitialize()
            print("--- Haunting Logic Thread: COM Uninitialized ---")
        except Exception as e:
            print(f"--- Haunting Logic Thread: Error uninitializing COM: {e} ---")


# --- GUI FUNCTIONS ---
def start_haunting():
    global haunting_active, haunting_thread
    if not haunting_active:
        haunting_active = True
        # Start the haunting logic in a separate thread
        haunting_thread = threading.Thread(target=run_haunting_logic, daemon=True) # daemon=True means thread exits with main program
        haunting_thread.start()
        status_label.config(text="Status: HAUNTING ACTIVE...", fg="red")
        start_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)
        print("Haunting activated via GUI.")
    else:
        print("Haunting already active.")

def stop_haunting():
    global haunting_active
    if haunting_active:
        haunting_active = False
        # The while loop in run_haunting_logic will eventually detect this change
        status_label.config(text="Status: HAUNTING INACTIVE", fg="green")
        start_button.config(state=tk.NORMAL)
        stop_button.config(state=tk.DISABLED)
        print("Haunting deactivated via GUI. Waiting for current event to finish.")
    else:
        print("Haunting already inactive.")

def on_closing():
    global haunting_active
    if messagebox.askokcancel("Exit Haunting Control", "Are you sure you want to exit?"):
        stop_haunting() # Attempt to stop haunting logic gracefully
        # Give a moment for the thread to potentially finish its current sleep/action
        if haunting_thread and haunting_thread.is_alive():
            print("Waiting for haunting thread to join...")
            pass # The daemon thread will exit with the main program
        root.destroy()
        print("GUI application exited.")

# --- GUI SETUP ---
root = tk.Tk()
root.title("Spawn entity")
root.geometry("300x150") # Set initial window size
root.resizable(False, False) # Prevent resizing

# Status Label
status_label = tk.Label(root, text="Status: HAUNTING INACTIVE", fg="green", font=("Arial", 12))
status_label.pack(pady=10)

# Start Button
start_button = tk.Button(root, text="Start Haunting", command=start_haunting, width=20, height=2, bg="#c2f0c2")
start_button.pack(pady=5)

# Stop Button
stop_button = tk.Button(root, text="Stop Haunting", command=stop_haunting, width=20, height=2, bg="#ffc2c2", state=tk.DISABLED)
stop_button.pack(pady=5)

# Protocol for closing the window (e.g., clicking X)
root.protocol("WM_DELETE_WINDOW", on_closing)

print("GUI control loaded. Press 'Start Haunting' to begin.")
root.mainloop() # Start the Tkinter event loop