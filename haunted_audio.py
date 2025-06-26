import pygame
import time
import random

from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER

# --- Audio Configuration ---
CREEPY_SONG_FILE = "creepy_sound.mp3"
SONG_PLAY_DURATION_SECONDS = 20 # How long the song plays

# --- Volume Configs ---
VOLUME_RAMP_UP_START_PERCENTAGE = 0.75 # Start increasing volume at 75% of SONG_PLAY_DURATION_SECONDS
TARGET_END_VOLUME_SCALAR = 0.5     # The target volume level (0.0 to 1.0)
VOLUME_STEP_INTERVAL_SECONDS = 0.2 # How often to adjust volume during the ramp-up phase

# --- Initialize Pygame Mixer ---
try:
    pygame.mixer.init()
    print("[AUDIO] Pygame mixer initialized.")
except Exception as e:
    print(f"[AUDIO] Error initializing Pygame mixer: {e}. Audio haunting might not work.")

def play_creepy_song():
    try:
        if not pygame.mixer.get_init():
            pygame.mixer.init() 
        pygame.mixer.music.load(CREEPY_SONG_FILE)
        print(f"[AUDIO] Playing '{CREEPY_SONG_FILE}'...")
        pygame.mixer.music.play()
        return True
    except pygame.error as e:
        print(f"[AUDIO] Error playing song: {e}. Make sure '{CREEPY_SONG_FILE}' exists and is a valid audio file.")
        return False

def stop_creepy_song():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
        print("[AUDIO] Song stopped.")

def get_master_volume_control():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        return volume
    except Exception as e:
        print(f"[AUDIO] Could not get master volume control: {e}")
        return None

def set_master_volume_scalar(volume_control, level):
    """Sets the master volume to a scalar level (0.0 to 1.0)."""
    if volume_control:
        level = max(0.0, min(1.0, level)) # Clamp level between 0.0 and 1.0
        volume_control.SetMasterVolumeLevelScalar(level, None)


def perform_audio_haunting():
    """Plays a creepy song and increases volume towards the end."""
    volume_control = get_master_volume_control()
    if not volume_control:
        print("[AUDIO] Cannot perform audio haunting as volume control is unavailable.")
        return

    # Store original volume and mute state
    original_volume_scalar = volume_control.GetMasterVolumeLevelScalar()
    original_mute_state = volume_control.GetMute()
    print(f"[AUDIO] Original Volume: {original_volume_scalar:.2f}, Mute: {original_mute_state}")

    if not play_creepy_song():
        return # Exit if song couldn't be played

    # Ensure volume starts at its original level 
    # Maintain the original volume for a while before ramping up
    set_master_volume_scalar(volume_control, original_volume_scalar)
    volume_control.SetMute(original_mute_state, None) # Ensure mute state is restored if needed

    start_time = time.time()
    ramp_up_start_time = SONG_PLAY_DURATION_SECONDS * VOLUME_RAMP_UP_START_PERCENTAGE
    ramp_up_duration = SONG_PLAY_DURATION_SECONDS - ramp_up_start_time

    try:
        while (time.time() - start_time) < SONG_PLAY_DURATION_SECONDS:
            elapsed_time = time.time() - start_time

            if elapsed_time >= ramp_up_start_time:
                # Calculate progress through the ramp-up phase (0.0 to 1.0)
                progress_in_ramp_up = (elapsed_time - ramp_up_start_time) / ramp_up_duration

                # Interpolate volume from original to target end volume
                # The starting point for the ramp becomes whatever the volume was before the ramp started
                current_target_ramp_volume = original_volume_scalar + (TARGET_END_VOLUME_SCALAR - original_volume_scalar) * progress_in_ramp_up
                set_master_volume_scalar(volume_control, current_target_ramp_volume)

            time.sleep(VOLUME_STEP_INTERVAL_SECONDS) # Controls how smooth/frequent volume updates are

    except Exception as e:
        print(f"[AUDIO] Error during volume control: {e}")
    finally:
        stop_creepy_song()
        # Restore original volume settings and mute state
        if volume_control:
            set_master_volume_scalar(volume_control, original_volume_scalar)
            volume_control.SetMute(original_mute_state, None)
            print("[AUDIO] Restored original volume settings.")
        print("[AUDIO] Audio haunting finished.")

perform_audio_haunting()