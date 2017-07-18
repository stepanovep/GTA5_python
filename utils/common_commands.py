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


def exit_the_game():
    # todo make sure it's active scene
    press_and_release_key(ESC, sleep_after=1.5)
    press_and_release_key(ARROW_RIGHT, sleep_after=1.5)
    press_and_release_key(ENTER, sleep_after=1)
    press_and_release_key(ARROW_UP, sleep_after=1)
    press_and_release_key(ENTER, sleep_after=10)
    press_and_release_key(ENTER)

    print('the game was closed')

def main():
    pause_before_start(5)
    walk_loop(2*60*60)

if __name__ == '__main__':
    main()
