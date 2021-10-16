from pynput import keyboard, mouse
import time

kC = keyboard.Controller()
mC = mouse.Controller()


def launch(app):
    time.sleep(0.5)
    kC.press(keyboard.Key.cmd)
    kC.release(keyboard.Key.cmd)
    time.sleep(0.5)
    kC.type(app)
    time.sleep(0.5)
    kC.press(keyboard.Key.enter)
    kC.release(keyboard.Key.enter)


def button_pressed(t):
    with mouse.Events() as events:
        return events.get(t)


def key_pressed(t):
    with keyboard.Events() as events:
        return events.get(t)


def not_pressed(key):
    with keyboard.Events() as events:
        for event in events:
            if str(event.key) == key:
                return False
            else:
                return True


def macros(command):
    match command:
        case "'v'":
            launch('valorant')
        case "'c'":
            print('auto clicker start')
            while not_pressed("'s'"):
                mC.press(mouse.Button.left)
                mC.release(mouse.Button.left)
            print('auto cliker stopped')
        case "'u'":
            launch("utorrent")
        case "'p'":
            launch("photoshop")
            

# The event listener will be running in this block
with keyboard.Events() as events:
    for event in events:
        if event.key == keyboard.Key.end:
            break
        elif event.key == keyboard.Key.f10:
            with keyboard.Events() as _events:
                # Block at most one second
                _event = key_pressed(2)
                if _event is None:
                    print('no command assigned')
                else:
                    macros(str(_event.key))
        else:
            pass     
