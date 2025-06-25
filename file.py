import pyautogui
import time
import random

pyautogui.PAUSE = 0.0
MIN_DELAY_SECONDS = 5 # Min seconds before mouse moves
MAX_DELAY_SECONDS = 15 #Max seconds before mouse moves
MOVE_DURATION_SECONDS = 1 # Will move for one second

screen_width, screen_height = pyautogui.size()
print(f"Screen Resolution: {screen_width}x{screen_height}")
print("Starting haunting. Press CTRL+C in terminal to terminate.")

try:
    while True:
        target_x = random.randint(0, screen_width - 1000)
        target_y = random.randint(0, screen_height - 800)

        # Move the mouse to the new random position

        pyautogui.moveTo(target_x, target_y, duration=MOVE_DURATION_SECONDS)

        # Calculate delay

        delay = random.uniform(MIN_DELAY_SECONDS, MAX_DELAY_SECONDS)
        time.sleep(delay)

except KeyboardInterrupt:
    print("\nHaunting stopped")
except Exception as e:
    print(f"An error occured: {e}")