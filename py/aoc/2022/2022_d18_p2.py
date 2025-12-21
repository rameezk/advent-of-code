from aoc.helper import AOC
from collections import deque


@AOC.puzzle(2022, 18, 2)
def solve():
    data = AOC.get_data()

#     data = """2,2,2
# 1,2,2
# 3,2,2
# 2,1,2
# 2,3,2
# 2,2,1
# 2,2,3
# 2,2,4
# 2,2,6
# 1,2,5
# 3,2,5
# 2,1,5
# 2,3,5"""

    cubes = set()
    for line in data.strip().splitlines():
        x, y, z = map(int, line.split(','))
        cubes.add((x, y, z))

    min_x = min(x for x, y, z in cubes) - 1
    max_x = max(x for x, y, z in cubes) + 1
    min_y = min(y for x, y, z in cubes) - 1
    max_y = max(y for x, y, z in cubes) + 1
    min_z = min(z for x, y, z in cubes) - 1
    max_z = max(z for x, y, z in cubes) + 1

    visited = set()
    queue = deque([(min_x, min_y, min_z)])
    visited.add((min_x, min_y, min_z))

    exterior_surface = 0

    while queue:
        x, y, z = queue.popleft()

        neighbors = [
            (x + 1, y, z),
            (x - 1, y, z),
            (x, y + 1, z),
            (x, y - 1, z),
            (x, y, z + 1),
            (x, y, z - 1),
        ]

        for nx, ny, nz in neighbors:
            if nx < min_x or nx > max_x or ny < min_y or ny > max_y or nz < min_z or nz > max_z:
                continue

            if (nx, ny, nz) in cubes:
                exterior_surface += 1
            elif (nx, ny, nz) not in visited:
                visited.add((nx, ny, nz))
                queue.append((nx, ny, nz))

    print(exterior_surface)
    AOC.submit_answer(exterior_surface)


if __name__ == "__main__":
    solve()
