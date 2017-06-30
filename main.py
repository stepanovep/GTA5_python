import time

from playUtils import pause_before_start
from skills.stealth import stealth_mode
from skills.stamina import run_mode


def main():
    pause_before_start(6)
    stealth_mode(10)
    time.sleep(3)
    run_mode(10)


if __name__ == '__main__':
    main()
