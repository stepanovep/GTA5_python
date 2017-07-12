import cv2
import numpy as np
import matplotlib.pyplot as plt
from grabscreen import grab_screen
from utils .common_commands import pause_before_start
from getKeys import key_check
import time

GAME_WIDTH = 1024
GAME_HEIGHT = 768

pause_before_start(5)

last_time = time.time()
while True:

    img = grab_screen(region=(0, 40, GAME_WIDTH, GAME_HEIGHT+40))
    cv2.imshow('image', img)

    print('grab_screen took {} seconds'.format(time.time() - last_time))
    last_time = time.time()
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

