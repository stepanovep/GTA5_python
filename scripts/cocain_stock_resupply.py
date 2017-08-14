import pyautogui
from utils.common_commands import *
from utils.directKeys import *
from logger import logger
from constants import *
from grabscreen import grab_screen
import cv2

LOG_IN = (425, 425)
RESUPPLY = (200, 240)
BY_SUPPLIES = (470, 320)
CONFIRM = (460, 420)

SUPPLY_REGION = (610, 550, 800, 622)
MONEY_REGION = (660, 30, 800, 80)


def cocaine_resupply():
    pyautogui.moveTo(LOG_IN, duration=0.25)
    press_and_release_key(ENTER, duration=1.25)

    pyautogui.moveTo(RESUPPLY, duration=0.25)
    press_and_release_key(ENTER, duration=1.25)

    pyautogui.moveTo(BY_SUPPLIES, duration=0.25)
    press_and_release_key(ENTER, duration=1.25)

    pyautogui.moveTo(CONFIRM, duration=0.25)
    press_and_release_key(ENTER, duration=0.5)

    press_and_release_key(ESC, duration=0.5)
    press_and_release_key(ESC, duration=0.5)
    press_and_release_key(ESC, duration=0.5)

    logger.info('cocaine supply has been bought')


def main():
    pause_before_start(5)
    press_key(F)

    for i in range(3):
        log_supply_screen(i)
        log_money_screen(i)
        press_and_release_key(E, sleep_after=5)
        cocaine_resupply()
        time.sleep(2)
        press_and_release_key(BACKSPACE)
        get_tired_of_ceo()
        time.sleep(2*HOURS + 20*MINUTES)

    release_key(F)
    time.sleep(1)
    press_and_release_key(R_SHIFT, sleep_after=2)

    exit_the_game()


def log_supply_screen(idx):
    img = grab_screen(region=SUPPLY_REGION)
    cv2.imwrite('supply{}.png'.format(idx), img)
    logger.debug('supply screen has been logged..')


def log_money_screen(idx):
    press_and_release_key(Z)
    img = grab_screen(region=MONEY_REGION)
    cv2.imwrite('money{}.png'.format(idx), img)
    logger.debug('money screen has been logged.. [iter={}]'.format(idx))

if __name__ == '__main__':
    main()
