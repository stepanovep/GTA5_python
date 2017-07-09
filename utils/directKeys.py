# direct inputs
# source to this solution and code:
# http://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game
# http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

import ctypes
import time

SendInput = ctypes.windll.user32.SendInput


W = 0x11
A = 0x1E
S = 0x1F
D = 0x20
E = 0x12
F = 0x21

NP_4 = 0x4B
NP_5 = 0x4C
NP_6 = 0x4D
NP_8 = 0x48

L_CTRL = 0x1D
L_SHIFT = 0x2A
R_SHIFT = 0x36
SPACE = 0x39
ESC = 0x01
ENTER = 0x1C
BACKSPACE = 0x0E

ARROW_UP = 0xC8
ARROW_LEFT = 0xCB
ARROW_RIGHT = 0xCD
ARROW_DOWN = 0xD0


PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]


class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]


class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                ("mi", MouseInput),
                ("hi", HardwareInput)]


class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]


def press_key(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def press_keys(keys):
    for key in keys:
        press_key(key)


def release_keys(keys):
    for key in keys:
        release_key(key)


def press_and_release_key(hexKeyCode, duration=0.1, sleep_after=0.25):
    press_key(hexKeyCode)
    time.sleep(duration)
    release_key(hexKeyCode)
    time.sleep(sleep_after)


def release_key(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput(0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def get_key_from_str(key_str):
    if key_str in ('w', 'W', 'Ц', 'ц'):
        return W
    if key_str in ('a', 'A', 'ф', 'Ф'):
        return A
    if key_str in ('s', 'S', 'ы', 'Ы'):
        return S
    if key_str in ('d', 'D', 'в', 'В'):
        return D
    if key_str in ('e', 'E', 'у', 'У'):
        return E
    if key_str in ('f', 'F', 'а', 'А'):
        return F

    if key_str == 'Key.space':
        return SPACE
    if key_str == 'Key.esc':
        return ESC
    if key_str == 'Key.enter':
        return ENTER
    if key_str == 'Key.shift':
        return L_SHIFT

    if key_str == 'Key.up':
        return ARROW_UP
    if key_str == 'Key.down':
        return ARROW_DOWN
    if key_str == 'Key.left':
        return ARROW_LEFT
    if key_str == 'Key.right':
        return ARROW_RIGHT

    if key_str == '5':
        return NP_5
    if key_str == '8':
        return NP_8
