from utils.directKeys import *


def pause_before_start(sec):
    for i in list(range(sec))[::-1]:
        print(i+1)
        time.sleep(1)
    print('start!')


def walk_loop(seconds):
    press_keys([A, S, W])
    time.sleep(seconds)
    release_keys([A, S, W])


def main():
    pause_before_start(5)
    walk_loop(10)


if __name__ == '__main__':
    main()
