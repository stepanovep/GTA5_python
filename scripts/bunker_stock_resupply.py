import pyautogui
from utils.common_commands import *
from utils.directKeys import *
from logger import logger
import cv2
from grabscreen import grab_screen
from constants import *


CLICK_TO_ENTER = (400, 375)
RESUPPLY = (200, 300)
BY_SUPPLIES = (400, 460)
CONFIRM = (450, 375)

SUPPLY_REGION = (610, 540, 800, 620)
MONEY_REGION = (660, 30, 800, 82)


def buy_bunker_supply():
    press_and_release_key(ENTER, duration=3)
    pyautogui.moveTo(CLICK_TO_ENTER, duration=0.25)
    press_and_release_key(ENTER, duration=1.25)

    pyautogui.moveTo(RESUPPLY, duration=0.25)
    press_and_release_key(ENTER, duration=1.25)

    pyautogui.moveTo(BY_SUPPLIES, duration=0.25)
    press_and_release_key(ENTER, duration=1.25)

    pyautogui.moveTo(CONFIRM, duration=0.25)
    press_and_release_key(ENTER, duration=0.5)

    press_and_release_key(ESC, duration=1)
    press_and_release_key(ESC, duration=1)

    logger.info('bunker supply has been bought')


def main():
    pause_before_start(5)
    press_key(F)

    for i in range(4):
        # you should be a CEO and stand right after the laptop
        log_supply_screen(i)
        log_money_screen(i, 'before_resupply')
        press_and_release_key(E, sleep_after=5)
        buy_bunker_supply()
        time.sleep(2)
        press_and_release_key(R_SHIFT, sleep_after=2)
        log_money_screen(i, 'after_resupply')
        time.sleep(7.5)
        press_and_release_key(BACKSPACE)
        get_tired_of_ceo()
        time.sleep(2*HOURS + 15*MINUTES)
        press_and_release_key(BACKSPACE)
        become_ceo()
        time.sleep(5)

    release_key(F)

    time.sleep(2)
    press_and_release_key(R_SHIFT, sleep_after=3)

    exit_the_game()


def log_supply_screen(idx):
    img = grab_screen(region=SUPPLY_REGION)
    cv2.imwrite('supply{}.png'.format(idx), img)
    logger.debug('supply screen has been logged..')


def log_money_screen(idx, message):
    press_and_release_key(Z)
    img = grab_screen(region=MONEY_REGION)
    cv2.imwrite('money{}_{}.png'.format(idx, message), img)
    logger.debug('money screen has been logged.. [iter={}]'.format(idx))


if __name__ == '__main__':
    main()
