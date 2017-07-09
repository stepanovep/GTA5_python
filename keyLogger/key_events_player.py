import sched

from utils.common_commands import *


def read_record():
    actions = list()
    with open('records/xp_loop.txt', 'r') as f:
        for line in f:
            event = line.strip().split()
            event_starts_time = float(event[0][:5])
            key_raw = event[1]
            action = event[2]
            key = get_key_from_str(key_raw)

            if key_raw == 'Key.backspace':
                break

            actions.append((event_starts_time, key, action))
    return actions


events = read_record()
pause_before_start(5)


def wait_loading_stage():
    pass


def main():
    while True:
        press_and_release_key(BACKSPACE)
        time.sleep(2)
        s = sched.scheduler(time.time, time.sleep)
        for event in events:
            if event[2] == 'pressed':
                action = press_key
            else:
                action = release_key
            s.enter(event[0], 1, action, argument=(event[1],))

        s.run()
        time.sleep(45)
        # wait_loading_stage()  use OpenCV here instead of dumb time.sleep()

if __name__ == '__main__':
    main()
