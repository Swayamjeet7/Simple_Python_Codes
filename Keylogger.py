from threading import Timer
from pynput.keyboard import Listener

def on_press(key):
    print(key)

with Listener(on_press=on_press) as l:
    Timer(5, l.stop).start()
    l.join()
    print('5 seconds passed')