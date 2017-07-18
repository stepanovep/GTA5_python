import pyautogui
from utils.common_commands import pause_before_start, exit_the_game
from utils.directKeys import *

# 500 475 - Войти на сайт
# 250 375 - Пополнить запас
# 500 580 - Купить сырье
# 570 470 - Подтвердить


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
    pause_before_start(5)
    press_key(W)

    for i in range(5):
        buy_bunker_supply()
        time.sleep(2*60*60 + 20*60)

    release_key(W)

    time.sleep(2)
    press_and_release_key(BACKSPACE, sleep_after=3)

    exit_the_game()


if __name__ == '__main__':
    main()
