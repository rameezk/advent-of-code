from aoc.helper import AOC
from collections import defaultdict

@AOC.puzzle(2021, 5, 2)
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

        dx = 0 if x1 == x2 else (1 if x2 > x1 else -1)
        dy = 0 if y1 == y2 else (1 if y2 > y1 else -1)

        x, y = x1, y1
        while True:
            grid[(x, y)] += 1
            if x == x2 and y == y2:
                break
            x += dx
            y += dy

    answer = sum(1 for count in grid.values() if count >= 2)

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
