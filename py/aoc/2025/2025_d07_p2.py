from aoc.helper import AOC
from collections import defaultdict


@AOC.puzzle(2025, 7, 2)
def solve():
    data = AOC.get_data()

#     data = """.......S.......
# ...............
# .......^.......
# ...............
# ......^.^......
# ...............
# .....^.^.^.....
# ...............
# ....^.^...^....
# ...............
# ...^.^...^.^...
# ...............
# ..^...^.....^..
# ...............
# .^.^.^.^.^...^.
# ..............."""

    splitters = set()
    start = None
    for r, row in enumerate(data.strip().splitlines()):
        for c, char in enumerate(row):
            if char == 'S':
                start = (c, r)

            if char == '^':
                splitters.add((c, r))

    max_depth = r

    timelines = defaultdict(int)
    timelines[start] = 1

    total_timelines = 0
    while timelines:
        next_timelines = defaultdict(int)
        for (c, r), count in timelines.items():
            next_pos = (c, r + 1)
            if next_pos in splitters:
                next_timelines[(c - 1, r + 1)] += count
                next_timelines[(c + 1, r + 1)] += count
            elif r + 1 <= max_depth:
                next_timelines[next_pos] += count
            else:
                total_timelines += count
        timelines = next_timelines

    total_timelines += sum(timelines.values())

    print(total_timelines)
    AOC.submit_answer(total_timelines)

if __name__ == "__main__":
    solve()
