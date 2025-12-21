from aoc.helper import AOC
from collections import deque


@AOC.puzzle(2022, 24, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """#.######
# #>>.<^<#
# #.<..<<#
# #>v.><>#
# #<^v^^>#
# ######.#""".strip().splitlines()

    grid = [list(line) for line in data]
    rows = len(grid)
    cols = len(grid[0])

    start = (0, 1)
    goal = (rows - 1, cols - 2)

    inner_rows = rows - 2
    inner_cols = cols - 2

    blizzards = []
    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            if grid[r][c] in '^v<>':
                blizzards.append((r, c, grid[r][c]))

    def get_blizzard_positions(t):
        positions = set()
        for r, c, direction in blizzards:
            if direction == '^':
                new_r = ((r - 1 - t) % inner_rows) + 1
                new_c = c
            elif direction == 'v':
                new_r = ((r - 1 + t) % inner_rows) + 1
                new_c = c
            elif direction == '<':
                new_r = r
                new_c = ((c - 1 - t) % inner_cols) + 1
            elif direction == '>':
                new_r = r
                new_c = ((c - 1 + t) % inner_cols) + 1
            positions.add((new_r, new_c))
        return positions

    queue = deque([(0, start)])
    visited = {(0, start)}

    while queue:
        time, (r, c) = queue.popleft()

        if (r, c) == goal:
            print(time)
            AOC.submit_answer(time)
            return

        next_time = time + 1
        next_blizzards = get_blizzard_positions(next_time)

        for dr, dc in [(0, 0), (0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            if (nr, nc) == start or (nr, nc) == goal:
                if (next_time, (nr, nc)) not in visited:
                    visited.add((next_time, (nr, nc)))
                    queue.append((next_time, (nr, nc)))
            elif 1 <= nr < rows - 1 and 1 <= nc < cols - 1:
                if (nr, nc) not in next_blizzards:
                    if (next_time, (nr, nc)) not in visited:
                        visited.add((next_time, (nr, nc)))
                        queue.append((next_time, (nr, nc)))


if __name__ == "__main__":
    solve()
