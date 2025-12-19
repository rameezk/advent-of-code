from aoc.helper import AOC
from collections import deque


@AOC.puzzle(2016, 13, 2)
def solve():
    favorite_number = int(AOC.get_data().strip())

#     favorite_number = 10

    def is_open(x, y):
        if x < 0 or y < 0:
            return False
        value = x*x + 3*x + 2*x*y + y + y*y + favorite_number
        bits = bin(value).count('1')
        return bits % 2 == 0

    start = (1, 1)
    max_steps = 50

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        (x, y), steps = queue.popleft()

        if steps >= max_steps:
            continue

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and is_open(nx, ny):
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))

    print(len(visited))
    AOC.submit_answer(len(visited))


if __name__ == "__main__":
    solve()
