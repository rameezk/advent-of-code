from aoc.helper import AOC
from aoc.util import adj
from collections import defaultdict


@AOC.puzzle(2025, 4, 2)
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
    R = set()

    for row, line in enumerate(data.strip().splitlines()):
        for col, char in enumerate(line.strip()):
            M[(col, row)] = char
            if char == "@":
                R.add((col, row))

    S = 0
    D = set()
    while True:
        R = R - D
        D = get_rolls_to_remove(M, R)
        M = remove_rolls(M, D)
        S += len(D)

        if len(D) == 0:
            break


    print(S)
    AOC.submit_answer(S)

def get_rolls_to_remove(M, R):
    D = set()

    for pos in R:
        count_adj = 0

        for around in adj(pos, diagonal=True):
            if M[around] == "@":
                count_adj += 1

        if count_adj < 4:
            D.add(pos)

    return D

def remove_rolls(M, D):
    for pos in D:
        M[pos] = "."
    return M

if __name__ == "__main__":
    solve()
