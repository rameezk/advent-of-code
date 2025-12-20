from aoc.helper import AOC
from collections import defaultdict

@AOC.puzzle(2021, 5, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """0,9 -> 5,9
# 8,0 -> 0,8
# 9,4 -> 3,4
# 2,2 -> 2,1
# 7,0 -> 7,4
# 6,4 -> 2,0
# 0,9 -> 2,9
# 3,4 -> 1,4
# 0,0 -> 8,8
# 5,5 -> 8,2""".splitlines()

    grid = defaultdict(int)

    for line in data:
        start, end = line.split(' -> ')
        x1, y1 = map(int, start.split(','))
        x2, y2 = map(int, end.split(','))

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2) + 1):
                grid[(x, y1)] += 1

    answer = sum(1 for count in grid.values() if count >= 2)

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
