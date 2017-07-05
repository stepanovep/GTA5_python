import sched

from utils.common_commands import *


def read_record():
    with open('xp_loop.txt', 'r') as f:
        for line in f:
            event = line.strip().split()
            event_starts_time = float(event[0][:5])
            key_raw = event[1]
            action = event[2]
            key = get_key_from_str(key_raw)

            if key_raw == 'Key.backspace':
                break

            events.append((event_starts_time, key, action))


events = list()
read_record()
pause_before_start(5)


def main():
    while True:
        press_and_release_key(BACKSPACE)
        time.sleep(2)
        s = sched.scheduler(time.time, time.sleep)
        for event in events:
            if event[2] == 'pressed':
                s.enter(event[0], 1, press_key, argument=(event[1],))
            else:
                s.enter(event[0], 1, release_key, argument=(event[1],))

        s.run()
        time.sleep(55)


if __name__ == '__main__':
    main()

