from aoc.helper import AOC


@AOC.puzzle(2022, 14, 1)
def solve():
#     data = """498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9"""

    data = AOC.get_data().strip()

    rocks = set()

    for line in data.strip().splitlines():
        points = line.split(" -> ")
        for i in range(len(points) - 1):
            x1, y1 = map(int, points[i].split(","))
            x2, y2 = map(int, points[i + 1].split(","))

            if x1 == x2:
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    rocks.add((x1, y))
            else:
                for x in range(min(x1, x2), max(x1, x2) + 1):
                    rocks.add((x, y1))

    max_y = max(y for x, y in rocks)

    sand_count = 0
    occupied = rocks.copy()

    while True:
        sx, sy = 500, 0

        while True:
            if sy > max_y:
                print(sand_count)
                AOC.submit_answer(sand_count)
                return

            if (sx, sy + 1) not in occupied:
                sy += 1
            elif (sx - 1, sy + 1) not in occupied:
                sx -= 1
                sy += 1
            elif (sx + 1, sy + 1) not in occupied:
                sx += 1
                sy += 1
            else:
                occupied.add((sx, sy))
                sand_count += 1
                break


if __name__ == "__main__":
    solve()
