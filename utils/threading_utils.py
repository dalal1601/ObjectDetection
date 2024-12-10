# utils/threading_utils.py
import threading

def threaded(func, *args):
    thread = threading.Thread(target=func, args=args)
    thread.start()
    return thread
