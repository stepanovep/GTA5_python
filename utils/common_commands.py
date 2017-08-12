from utils.directKeys import *
from grabscreen import grab_screen


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


def is_game_active():
    health_region = (17, 771, 113, 779)
    armor_region = (114, 771, 210, 779)
    health = grab_screen(region=health_region)
    armor = grab_screen(region=armor_region)

    h_reds, h_greens, h_blues = [], [], []
    a_reds, a_greens, a_blues = [], [], []

    for x in range(1, 8):
        for y in range(1, 95):
            health_color = health[x, y]
            h_reds.append(health_color[0])
            h_greens.append(health_color[1])
            h_blues.append(health_color[2])

            armor_color = armor[x, y]
            a_reds.append(armor_color[0])
            a_greens.append(armor_color[1])
            a_blues.append(armor_color[2])

    h_greens.sort(); h_reds.sort(); h_blues.sort()
    a_reds.sort();a_greens.sort(); a_blues.sort()

    median_id = len(h_greens) // 2

    h_red = h_reds[median_id]
    h_green = h_greens[median_id]
    h_blue = h_blues[median_id]

    a_red = a_reds[median_id]
    a_green = a_greens[median_id]
    a_blue = a_blues[median_id]

    health_bar_greenish = h_green > h_blue+5 and h_green > h_red+5
    armor_bar_blueish = a_blue > a_red + 5 and a_blue > a_green + 5
    return health_bar_greenish and armor_bar_blueish


def main():
    pause_before_start(3)
    while True:
        print(is_game_active())
        time.sleep(2)


if __name__ == '__main__':
    main()
