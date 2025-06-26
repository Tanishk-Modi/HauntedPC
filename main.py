import pyautogui    
import time         
import random     

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

screen_width, screen_height = pyautogui.size()
print("\n--- Starting Haunting ---")
print("Press Ctrl+C in the terminal to terminate.")
print("------------------------------------------\n")

# -- MAIN LOOP -- #

time.sleep(10) # Calm before the storm

try:
    while True:

        choice = random.random()
        current_prob = 0.0

        current_prob += MOUSE_EVENT_PROBABILITY

        if choice < current_prob:
            # Perform mouse haunting
            perform_mouse_haunting(screen_width, screen_height)
        elif choice < (current_prob + TYPING_EVENT_PROBABILITY):
            # Perform typing haunting
            perform_typing_haunting()
        elif choice < (current_prob + VISUAL_GLITCH_PROBABILITY):
            # Perform visual haunting
            perform_visual_haunting()
        elif choice < (current_prob + ERROR_PROBABILITY):
            perform_haunted_error()
        else:
            perform_audio_haunting()
            
        delay_between_events = random.uniform(MIN_OVERALL_DELAY_SECONDS, MAX_OVERALL_DELAY_SECONDS)
        time.sleep(delay_between_events)

except KeyboardInterrupt:
    print("\n\Haunting Stopped.")
    # Ensure any playing music is stopped on exit
    try:
        import pygame
        if pygame.mixer.get_init():
            pygame.mixer.music.stop()
            pygame.mixer.quit() # Clean up mixer resources
    except:
        pass
except Exception as e:
    print(f"\n\nAn error occured: {e}")