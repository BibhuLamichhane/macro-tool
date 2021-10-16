from pynput import mouse
from pynput import keyboard
import time

kC = keyboard.Controller()
mC = mouse.Controller()

f = open(f'logs/{input("enter date")}.txt', 'r')
d = f.readlines()

buttons = {
    'Button.left' : mouse.Button.left,
    'Button.right' : mouse.Button.right
}
keys = {
    'Key.esc' : keyboard.Key.esc,
    'Key.space' : keyboard.Key.space
}

# time.sleep(4)
print('start')
for i in range(len(d)):
    curr = d[i].strip()
    if 'pause' in curr:
        v = float(curr.split()[-1])
        time.sleep(v)
    elif 'Button' in curr:
        button, pos = curr.split(',')
        x, y = pos.split()
        mC.position = (int(x), int(y))
        mC.press(buttons[button])
        mC.release(buttons[button])
    elif 'Key' in curr:
        kC.press(keys[curr])
        kC.release(keys[curr])
    elif 'move' in curr:
        x, y = curr.split(',')[-1].split()
        print(x, y)
        mC.position = (int(x), int(y)) 
        time.sleep(0.02)
    elif 'scroll' in curr:
        x, y = curr.split(',')[1].split()
        dx, dy = curr.split(',')[-1].split()
        mC.position = (int(x), int(y))
        mC.scroll = (dx, dy)
    else:
        kC.press(curr[1:-1])
        kC.release(curr[1:-1])
