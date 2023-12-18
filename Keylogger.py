from threading import Timer
from pynput import keyboard

f = open('nt.txt','w')

def on_press(key):
    global x
    if key != keyboard.Key.shift:
        f.write(f'pressed {key}\n')   
    
with keyboard.Listener(on_press=on_press) as l:
    Timer(10, l.stop).start()
    l.join()
    print('10 seconds passed')

f.close()