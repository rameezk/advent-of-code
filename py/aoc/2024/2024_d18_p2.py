from aoc.helper import AOC
from collections import deque


@AOC.puzzle(2024, 18, 2)
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
#     grid_size = 6

    def has_path(num_bytes):
        corrupted = set()
        for i in range(num_bytes):
            x, y = map(int, data[i].split(','))
            corrupted.add((x, y))

        start = (0, 0)
        end = (grid_size, grid_size)

        queue = deque([start])
        visited = {start}

        while queue:
            x, y = queue.popleft()

            if (x, y) == end:
                return True

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = x + dx, y + dy

                if 0 <= nx <= grid_size and 0 <= ny <= grid_size:
                    if (nx, ny) not in corrupted and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))

        return False

    left = 0
    right = len(data)

    while left < right:
        mid = (left + right) // 2
        if has_path(mid):
            left = mid + 1
        else:
            right = mid

    blocking_byte_idx = left - 1
    result = data[blocking_byte_idx]
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
