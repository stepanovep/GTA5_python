import cv2
from grabscreen import grab_screen
from utils .common_commands import pause_before_start
import time

GAME_WIDTH = 1024
GAME_HEIGHT = 768

pause_before_start(3)

game_region = (0, 30, GAME_WIDTH, GAME_HEIGHT+25)
radar_region = (17, 647, 210, 769)
health_region = (17, 771, 113, 779)
armor_region = (114, 771, 210, 779)

last_time = time.time()
while True:
    img = grab_screen(region=radar_region)
    cv2.namedWindow("image")
    cv2.moveWindow("image", -1920, 0)
    cv2.imshow('image', img)

    #print('grab_screen took {} seconds'.format(time.time() - last_time))
    #last_time = time.time()
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

    time.sleep(1)
