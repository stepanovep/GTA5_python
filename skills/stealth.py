import time

from directKeys import *
from playUtils import pause_before_start, walk_loop


def stealth_mode(seconds):
    press_and_release_key(L_CTRL)
    walk_loop(seconds)
    press_and_release_key(L_CTRL)


def main():
    pause_before_start(5)
    stealth_mode(10)


if __name__ == '__main__':
    main()
