from directKeys import *
from playUtils import pause_before_start


def do_plunges(count):
    plunge_time = 19

    for i in range(1, count+1):
        plunge(plunge_time)
        if i % 15 == 0:
            plunge_time += 0.75
            hold_key(D, duration=1)
        time.sleep(2)


def plunge(duration):
    hold_key(SPACE)
    time.sleep(duration)
    press_keys([S, L_SHIFT])
    time.sleep(2.5)
    release_keys([S, L_SHIFT])


def main():
    pause_before_start(5)
    do_plunges(7)


if __name__ == '__main__':
    main()
