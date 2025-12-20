from aoc.helper import AOC
from collections import defaultdict


@AOC.puzzle(2018, 6, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """1, 1
# 1, 6
# 8, 3
# 3, 4
# 5, 5
# 8, 9"""

    lines = data.strip().splitlines()
    coords = []
    for line in lines:
        x, y = line.split(", ")
        coords.append((int(x), int(y)))

    min_x = min(c[0] for c in coords)
    max_x = max(c[0] for c in coords)
    min_y = min(c[1] for c in coords)
    max_y = max(c[1] for c in coords)

    closest = {}
    infinite = set()

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            distances = []
            for i, (cx, cy) in enumerate(coords):
                dist = abs(x - cx) + abs(y - cy)
                distances.append((dist, i))

            distances.sort()
            if distances[0][0] < distances[1][0]:
                closest[(x, y)] = distances[0][1]

                if x == min_x or x == max_x or y == min_y or y == max_y:
                    infinite.add(distances[0][1])

    areas = defaultdict(int)
    for coord_idx in closest.values():
        if coord_idx not in infinite:
            areas[coord_idx] += 1

    result = max(areas.values())
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
