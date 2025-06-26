import pyautogui
import time
import random
import subprocess

MOVE_DURATION_SECONDS = 0.8 # Time mouse will move
MAX_JUMP_PIXELS = 100 # For jerky movement

def perform_mouse_haunting(screen_width, screen_height):

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
