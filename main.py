import pyautogui    
import time         
import random     

from haunted_mouse import perform_mouse_haunting
from ghost_typer import perform_typing_haunting

# -- GLOBAL CONFIGS -- #

MIN_OVERALL_DELAY_SECONDS = 5   # Min seconds between ANY major haunting event
MAX_OVERALL_DELAY_SECONDS = 30  # Max seconds between ANY major haunting event

MOUSE_EVENT_PROBABILITY = 0.8  # 80% chance to perform a mouse event
TYPING_EVENT_PROBABILITY = 0.2 # 20% chance to perform a typing event (These probabilities should sum to 1.0)

screen_width, screen_height = pyautogui.size()
print(f"Screen Resolution: {screen_width}x{screen_height}")
print("\n--- Starting Haunting ---")
print("Press Ctrl+C in the terminal to terminate.")
print("------------------------------------------\n")

# -- MAIN LOOP -- #

time.sleep(10)

try:
    while True:
        if random.random() < MOUSE_EVENT_PROBABILITY:
            perform_mouse_haunting(screen_width, screen_height)
        else:
            perform_typing_haunting()
        delay_between_events = random.uniform(MIN_OVERALL_DELAY_SECONDS, MAX_OVERALL_DELAY_SECONDS)
        time.sleep(delay_between_events)
except KeyboardInterrupt:
    print("\n\Haunting ceased.")
except Exception as e:
    print(f"\n\nAn unexpected error occurred: {e}")
