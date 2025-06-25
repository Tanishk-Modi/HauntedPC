import pyautogui
import time
import random

pyautogui.PAUSE = 0.0
MIN_DELAY_SECONDS = 5 # Min seconds before mouse moves
MAX_DELAY_SECONDS = 15 #Max seconds before mouse moves
MOVE_DURATION_SECONDS = 0.8 # Time mouse will move
MAX_JUMP_PIXELS = 100 # For jerky movement

screen_width, screen_height = pyautogui.size()
print(f"Screen Resolution: {screen_width}x{screen_height}")
print("Starting haunting. Press CTRL+C in terminal to terminate.")

try:
    while True:

        current_x, current_y = pyautogui.position()

        delta_x = random.randint(-MAX_JUMP_PIXELS, MAX_JUMP_PIXELS)
        delta_y = random.randint(-MAX_JUMP_PIXELS, MAX_JUMP_PIXELS)

        target_x = current_x + delta_x
        target_y = current_y + delta_y

        # Ensure mouse stays within screen bounds

        target_x = max(0, min(target_x, screen_width - 1))
        target_y = max(0, min(target_y, screen_height - 1))

        # Move the mouse to the new random position

        pyautogui.moveTo(target_x, target_y, duration=MOVE_DURATION_SECONDS)

        if random.random() < 0.2: # 20% chance of a click
            pyautogui.click()

        # Calculate delay

        delay = random.uniform(MIN_DELAY_SECONDS, MAX_DELAY_SECONDS)
        time.sleep(delay)

except KeyboardInterrupt:
    print("\nHaunting stopped")
except Exception as e:
    print(f"An error occured: {e}")