from aoc.helper import AOC
from collections import defaultdict
import re


@AOC.puzzle(2018, 4, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """[1518-11-01 00:00] Guard #10 begins shift
# [1518-11-01 00:05] falls asleep
# [1518-11-01 00:25] wakes up
# [1518-11-01 00:30] falls asleep
# [1518-11-01 00:55] wakes up
# [1518-11-01 23:58] Guard #99 begins shift
# [1518-11-02 00:40] falls asleep
# [1518-11-02 00:50] wakes up
# [1518-11-03 00:05] Guard #10 begins shift
# [1518-11-03 00:24] falls asleep
# [1518-11-03 00:29] wakes up
# [1518-11-04 00:02] Guard #99 begins shift
# [1518-11-04 00:36] falls asleep
# [1518-11-04 00:46] wakes up
# [1518-11-05 00:03] Guard #99 begins shift
# [1518-11-05 00:45] falls asleep
# [1518-11-05 00:55] wakes up""".strip().splitlines()

    events = []
    for line in data:
        match = re.match(r'\[(.+)\] (.+)', line)
        timestamp = match.group(1)
        action = match.group(2)
        events.append((timestamp, action))

    events.sort()

    guard_sleep_minutes = defaultdict(lambda: defaultdict(int))
    current_guard = None
    sleep_start = None

    for timestamp, action in events:
        if 'Guard' in action:
            guard_id = int(re.search(r'#(\d+)', action).group(1))
            current_guard = guard_id
        elif 'falls asleep' in action:
            minute = int(timestamp.split(':')[1])
            sleep_start = minute
        elif 'wakes up' in action:
            minute = int(timestamp.split(':')[1])
            for m in range(sleep_start, minute):
                guard_sleep_minutes[current_guard][m] += 1

    max_count = 0
    best_guard = None
    best_minute = None

    for guard_id, minutes in guard_sleep_minutes.items():
        for minute, count in minutes.items():
            if count > max_count:
                max_count = count
                best_guard = guard_id
                best_minute = minute

    result = best_guard * best_minute
    print(f"Guard #{best_guard} is most frequently asleep at minute {best_minute} ({max_count} times)")
    print(f"Answer: {result}")
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
