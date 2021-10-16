from pynput import mouse
from pynput import keyboard
import time
import threading
import datetime
date = f'{str(datetime.date.today().day)}-{str(datetime.date.today().month)}-{str(datetime.date.today().year)}'
f = open(f'logs/{date}.txt', 'a+')
g = open(f'logs/{date}(without pause).txt', 'a+')
end = False


class m:
    def on_move(self, x, y):
        f.write(f'move,{x} {y}')

    def on_click(self, x, y, button, pressed):
        global t
        t2 = time.time()
        f.write(f'pause {t2-t}\n')
        t = time.time()
        print(f'{button} at {x},{y}')
        f.write(f"{button},{x} {y}\n")
        g.write(f"{button},{x} {y}\n")
        if end:
            # Stop listener
            return False

    def on_scroll(self, x, y, dx, dy):
        f.write(f'scroll,{x} {y},{dx} {dy}')

    def start(self):
        # Collect events until released
        with mouse.Listener(
                on_move=self.on_move,
                on_click=self.on_click,
                on_scroll=self.on_scroll) as listener:
            listener.join()


class k:
    def on_press(self, key): #only store this
        global t
        t2 = time.time()
        f.write(f'pause {t2-t}\n')
        t = time.time()
        try:
            print(key)
            f.write(str(key) + '\n')

        except AttributeError:
            print(key)
            f.write(str(key) + '\n')

    def on_release(self, key): #not imp
        # print('{0} released'.format(
        #     key))
        global end
        c = mouse.Controller()
        if key == keyboard.Key.end:
            # Stop listener
            end = True
            c.press(mouse.Button.left)
            c.release(mouse.Button.left)
            return False
    def start(self):
        with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
            listener.join()


# time.sleep(10)
t = time.time()
print('start')
a = k()
b = m()
thread1 = threading.Thread(target=a.start)
thread2 = threading.Thread(target=b.start)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
