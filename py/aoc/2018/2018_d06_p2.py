from aoc.helper import AOC


@AOC.puzzle(2018, 6, 2)
def solve():
    data = AOC.get_data().strip()

#     data = """1, 1
# 1, 6
# 8, 3
# 3, 4
# 5, 5
# 8, 9"""

    max_distance = 10000

    lines = data.strip().splitlines()
    coords = []
    for line in lines:
        x, y = line.split(", ")
        coords.append((int(x), int(y)))

    min_x = min(c[0] for c in coords)
    max_x = max(c[0] for c in coords)
    min_y = min(c[1] for c in coords)
    max_y = max(c[1] for c in coords)

    region_size = 0

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            total_distance = 0
            for cx, cy in coords:
                total_distance += abs(x - cx) + abs(y - cy)

            if total_distance < max_distance:
                region_size += 1

    print(region_size)
    AOC.submit_answer(region_size)


if __name__ == "__main__":
    solve()
