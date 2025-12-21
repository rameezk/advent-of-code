from aoc.helper import AOC
from collections import deque


@AOC.puzzle(2024, 18, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """5,4
# 4,2
# 4,5
# 3,0
# 2,1
# 6,3
# 2,4
# 1,5
# 0,6
# 3,3
# 2,6
# 5,1
# 1,2
# 5,5
# 2,5
# 6,5
# 1,4
# 0,4
# 6,4
# 1,1
# 6,1
# 1,0
# 0,5
# 1,6
# 2,0""".strip().splitlines()

    grid_size = 70
    bytes_to_fall = 1024

#     grid_size = 6
#     bytes_to_fall = 12

    corrupted = set()
    for i, line in enumerate(data[:bytes_to_fall]):
        x, y = map(int, line.split(','))
        corrupted.add((x, y))

    start = (0, 0)
    end = (grid_size, grid_size)

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) == end:
            print(steps)
            AOC.submit_answer(steps)
            return

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx <= grid_size and 0 <= ny <= grid_size:
                if (nx, ny) not in corrupted and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), steps + 1))

    print("No path found")


if __name__ == "__main__":
    solve()
