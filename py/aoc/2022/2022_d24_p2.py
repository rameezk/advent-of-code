from aoc.helper import AOC
from collections import deque


@AOC.puzzle(2022, 24, 2)
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

    def find_path(start_time, from_pos, to_pos):
        queue = deque([(start_time, from_pos)])
        visited = {(start_time, from_pos)}

        while queue:
            time, (r, c) = queue.popleft()

            if (r, c) == to_pos:
                return time

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

        return -1

    time1 = find_path(0, start, goal)
    print(f"Trip 1 (start to goal): {time1}")

    time2 = find_path(time1, goal, start)
    print(f"Trip 2 (goal to start): {time2}")

    time3 = find_path(time2, start, goal)
    print(f"Trip 3 (start to goal): {time3}")

    total = time3
    print(f"Total time: {total}")
    AOC.submit_answer(total)


if __name__ == "__main__":
    solve()
