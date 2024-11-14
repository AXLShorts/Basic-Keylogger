from pynput import keyboard
import time
from collections import defaultdict

key_press_times = defaultdict(float)
key_release_times = defaultdict(float)
key_durations = defaultdict(float)
key_press_count = defaultdict(int)

with open("keystrokes_log.txt", "a") as log_file:

    def on_press(key):
        try:
            key_str = key.char if key.char else str(key)
        except AttributeError:
            key_str = str(key)
        
        key_press_times[key_str] = time.time()
        key_press_count[key_str] += 1

        log_file.write(f"{key_str}\n")
        log_file.flush()

    def on_release(key):
        try:
            key_str = key.char if key.char else str(key)
        except AttributeError:
            key_str = str(key)

        key_release_times[key_str] = time.time()

        log_file.write(f"{key_str}\n")
        log_file.flush()

        print(f"{key_str}")

        if key == keyboard.Key.esc:
            return False

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
