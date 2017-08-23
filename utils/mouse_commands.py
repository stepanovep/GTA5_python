import win32api
import time

while True:
    print(win32api.GetCursorPos())
    time.sleep(0.5)
