from aoc.helper import AOC
from collections import Counter

@AOC.puzzle(2021, 6, 2)
def solve():
    data = AOC.get_data().strip()

#     data = """3,4,3,1,2"""

    fish = list(map(int, data.split(',')))

    counts = Counter(fish)
    timers = [counts.get(i, 0) for i in range(9)]

    for day in range(256):
        new_timers = [0] * 9
        new_timers[8] = timers[0]
        new_timers[6] = timers[0]
        for i in range(1, 9):
            new_timers[i-1] += timers[i]
        timers = new_timers

    answer = sum(timers)

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
