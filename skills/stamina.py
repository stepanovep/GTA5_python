from utils.directKeys import *
from utils.common_commands import pause_before_start, walk_loop


def run_mode(seconds):
    press_key(L_SHIFT)
    walk_loop(seconds)
    release_key(L_SHIFT)


def main():
    pause_before_start(5)
    run_mode(10)


if __name__ == '__main__':
    main()
