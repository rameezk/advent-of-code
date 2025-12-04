from aoc.helper import AOC
from aoc.util import adj
from collections import defaultdict


@AOC.puzzle(2025, 4, 1)
def solve():
    data = AOC.get_data()

#     data = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@."""

    M = defaultdict(lambda: ".")
    R = []

    for row, line in enumerate(data.strip().splitlines()):
        for col, char in enumerate(line.strip()):
            M[(col, row)] = char
            if char == "@":
                R.append((col, row))

    S = 0
    for pos in R:
        count_adj = 0
        for around in adj(pos, diagonal=True):
            if M[around] == "@":
                count_adj += 1

        if count_adj < 4:
            S += 1

    print(S)
    AOC.submit_answer(S)

if __name__ == "__main__":
    solve()
