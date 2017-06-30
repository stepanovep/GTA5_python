import time

from playUtils import pause_before_start
from skills.stealth import stealth_mode
from skills.stamina import run_mode
from skills.swimming import do_plunges


def main():
    pause_before_start(8)
    do_plunges(7)


if __name__ == '__main__':
    main()
