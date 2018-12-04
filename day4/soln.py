import re
from datetime import datetime

def main():
    with open('input.txt', 'r+') as datafile:
        data = datafile.readlines()

    sleep_str = r'\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] (?:Guard #(\d+) begins shift|(wakes up)|(falls asleep))'
    sleep_info = sorted([re.findall(sleep_str, item)[0] for item in data], key=lambda s: s[0])
    sleep_info = list(map(lambda s: (datetime.strptime(s[0], '%Y-%m-%d %H:%M'), s[1], s[2], s[3]), sleep_info))

    sleep_dict = {}
    last_state = 0 # awake
    last_change = 0
    last_guard = 0
    for dtg, guard_id, awake, asleep in sleep_info:
        if guard_id:
            if last_state == 1:
                for i in range(last_change, 60):
                    sleep_dict[last_guard][i] += 1
            if guard_id not in sleep_dict:
                sleep_dict[guard_id] = [0]*60
            last_state = 0
            last_change = 0
            last_guard = guard_id
        elif awake:
            minute = dtg.minute
            for i in range(last_change, minute):
                sleep_dict[last_guard][i] += 1
            last_state = 0
            last_change = minute
        elif asleep:
            minute = dtg.minute
            last_state = 1
            last_change = minute

    most_asleep = {k: sum(v) for k, v in sleep_dict.items()}
    most_asleep_guard = max(list(most_asleep.keys()), key=(lambda key: most_asleep[key]))

    max_idx = 0
    max_item = 0
    for idx, item in enumerate(sleep_dict[most_asleep_guard]):
        if item > max_item:
            max_idx = idx
            max_item = item

    # Part 1
    print(int(most_asleep_guard)*max_idx)

    most_freq_asleep = {k: max(v) for k, v in sleep_dict.items()}
    most_freq_guard = max(list(most_asleep.keys()), key=(lambda key: most_freq_asleep[key]))

    max_idx = 0
    max_item = 0
    for idx, item in enumerate(sleep_dict[most_freq_guard]):
        if item > max_item:
            max_idx = idx
            max_item = item

    print(int(most_freq_guard)*max_idx)

if __name__ == "__main__":
    main()
