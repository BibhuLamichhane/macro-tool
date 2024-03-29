from pynput import mouse
from pynput import keyboard
import time
import threading
import datetime

end = False
date = f'{str(datetime.date.today().day)}-{str(datetime.date.today().month)}-{str(datetime.date.today().year)}'
f = open(f'logs/{date}.txt', 'a+')
g = open(f'logs/{date}(without pause).txt', 'a+')

class m:
    def on_move(self, x, y):
        global t
        t2 = time.time()
        f.write(f'pause {t2-t}\n')
        t = time.time()
        f.write(f'move,{x} {y}\n')
        g.write(f'move,{x} {y}\n')

    def on_click(self, x, y, button, pressed):
        global t, end
        t2 = time.time()
        f.write(f'pause {t2-t}\n')
        t = time.time()
        print(f'{button} at {x},{y}')
        if pressed:
            f.write(f"{button},{x} {y}\n")
            g.write(f"{button},{x} {y}\n")
        if end:
            # Stop listener
            return False

    def on_scroll(self, x, y, dx, dy):
        global t
        t2 = time.time()
        f.write(f'pause {t2-t}\n')
        t = time.time()
        f.write(f'scroll,{x} {y},{dx} {dy}\n')
        g.write(f'scroll,{x} {y},{dx} {dy}\n')

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

if __name__ == "__main__":
    time.sleep(5)
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
