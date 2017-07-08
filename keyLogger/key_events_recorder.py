import time
from pynput import keyboard
from utils.common_commands import pause_before_start


def on_press(key):
    if key not in pressed_keys:
        pressed_keys.add(key)
        events.append(((time.time() - start_time), key, 'pressed'))


def on_release(key):
    pressed_keys.discard(key)
    events.append(((time.time() - start_time), key, 'released'))
    if key == keyboard.Key.backspace:
        return False


pressed_keys = set()
events = list()

pause_before_start(5)
start_time = time.time()

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

print('keys are pressing : {}'.format(pressed_keys))
print(*events, sep='\n', end='\n')


with open('chapter_1_1.txt', 'w') as f:
    for event in events:
        f.write(str(event[0]) + ' ')
        f.write(str(event[1]).strip('\'') + ' ')
        f.write(event[2] + '\n')
