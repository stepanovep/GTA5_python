import pyautogui
from utils.common_commands import *
from utils.directKeys import *

# 500 475 - Войти на сайт
# 250 375 - Пополнить запас
# 500 580 - Купить сырье
# 570 470 - Подтвердить

MINUTES = 60
HOURS = MINUTES * 60


def buy_bunker_supply():
    press_and_release_key(ENTER, duration=3)
    pyautogui.moveTo(500, 475, duration=0.25)
    press_and_release_key(ENTER, duration=1.25)

    pyautogui.moveTo(250, 375, duration=0.25)
    press_and_release_key(ENTER, duration=1.25)

    pyautogui.moveTo(500, 580, duration=0.25)
    press_and_release_key(ENTER, duration=1.25)

    pyautogui.moveTo(570, 470, duration=0.25)
    press_and_release_key(ENTER, duration=0.5)

    press_and_release_key(ESC, duration=1)
    press_and_release_key(ESC, duration=1)

    print('bunker supply has been bought')


def main():
    pause_before_start(8)
    press_key(F)

    for i in range(5):
        # you should be a CEO and stand right after the laptop
        press_and_release_key(E, sleep_after=5)
        buy_bunker_supply()
        time.sleep(3)
        press_and_release_key(R_SHIFT, sleep_after=2)
        time.sleep(10)
        press_and_release_key(BACKSPACE)
        get_tired_of_ceo()
        time.sleep(2*HOURS + 20*MINUTES)
        press_and_release_key(BACKSPACE)
        become_ceo()
        time.sleep(5)

    release_key(F)

    time.sleep(2)
    press_and_release_key(R_SHIFT, sleep_after=3)

    exit_the_game()


if __name__ == '__main__':
    main()
