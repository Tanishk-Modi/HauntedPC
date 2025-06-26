import pyautogui
import time
import random

INVERSION_FLASH_DURATION = 0.3

time.sleep(3)

def perform_visual_haunting():
    try:
        pyautogui.hotkey('win', 'ctrl', 'c')
        time.sleep(INVERSION_FLASH_DURATION)

        pyautogui.hotkey('win', 'ctrl', 'c')
        time.sleep(0.5)
    except Exception as e:
        try:
            pyautogui.hotkey('win', 'ctrl', 'c')
        except:
            pass