from utils.directKeys import *
from utils.common_commands import pause_before_start


def fly_around(seconds):
    press_keys([W, NP_8])
    time.sleep(4)
    press_key(A)

    for i in range(1, seconds):
        if i % 15 == 0:
            hold_key(NP_5, duration=1)
        time.sleep(1)

    release_keys([W, NP_8, A])


def main():
    pause_before_start(8)
    fly_around(60*60*12)


if __name__ == '__main__':
    main()
