from aoc.helper import AOC
from aoc.util import adj
from collections import defaultdict


@AOC.puzzle(2025, 5, 1)
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

    range_data, ingredients_data = data.strip().split("\n\n")

    R = []
    for line in range_data.splitlines():
        lower, upper = line.split("-")
        R.append((int(lower), int(upper)))


    S = 0
    for ingredient in ingredients_data.splitlines():
        for lower, upper in R:
            if lower <= int(ingredient) <= upper:
                S += 1
                break

    print(S)

    AOC.submit_answer(S)

if __name__ == "__main__":
    solve()
