import pyautogui    
import time         

from haunted_mouse import perform_mouse_haunting
from ghost_typer import perform_typing_haunting
from haunted_visual import perform_visual_haunting
from haunted_error import perform_haunted_error
from haunted_audio import perform_audio_haunting

MIN_OVERALL_DELAY_SECONDS = 5  
MAX_OVERALL_DELAY_SECONDS = 30  

screen_width, screen_height = pyautogui.size()
print("\n--- Starting Haunting ---")
print("Press Ctrl+C in the terminal to terminate.")
print("------------------------------------------\n")

perform_mouse_haunting(screen_width, screen_height)

time.sleep(10)

perform_typing_haunting()

time.sleep(10)

perform_visual_haunting()

time.sleep(10)

perform_haunted_error()

time.sleep(10)

perform_audio_haunting()

time.sleep(10)

# End of program execution