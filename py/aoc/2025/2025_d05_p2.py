from aoc.helper import AOC
from aoc.util import adj
from collections import defaultdict


@AOC.puzzle(2025, 5, 2)
def solve():
    data = AOC.get_data()

#     data = """3-5
# 10-14
# 16-20
# 12-18
#
# 1
# 5
# 8
# 11
# 17
# 32"""

    range_data, _ = data.strip().split("\n\n")

    R = []
    for line in range_data.splitlines():
        lower, upper = line.split("-")
        R.append((int(lower), int(upper)))

    R.sort()

    M = []
    for start, end in R:
        if M and start <= M[-1][1] + 1:
            M[-1] = (M[-1][0], max(M[-1][1], end))
        else:
            M.append((start, end))

    S = sum(end - start + 1 for start, end in M)
    print(S)

    AOC.submit_answer(S)

if __name__ == "__main__":
    solve()
