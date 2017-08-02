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


def become_ceo():
    # todo make sure it's active scene
    # todo make sure u are not CEO first
    press_and_release_key(M, sleep_after=1)
    press_and_release_key(ARROW_DOWN, times=6)
    press_and_release_key(ENTER, times=3, duration=1, sleep_after=2)
    print('You became CEO')


def get_tired_of_ceo():
    # todo make sure it's active scene
    # todo make sure u are CEO at first
    press_and_release_key(M, sleep_after=1)
    press_and_release_key(ENTER)
    press_and_release_key(ARROW_UP)
    press_and_release_key(ENTER, times=3, duration=1, sleep_after=2)
    print('You became a usual player')


def main():
    pause_before_start(5)
    walk_loop(60*69)


if __name__ == '__main__':
    main()
