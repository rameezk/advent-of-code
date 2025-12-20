from aoc.helper import AOC
from collections import deque

@AOC.puzzle(2021, 9, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

    grid = [[int(c) for c in line] for line in data]
    rows = len(grid)
    cols = len(grid[0])

    low_points = []

    for r in range(rows):
        for c in range(cols):
            current = grid[r][c]
            is_low_point = True

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] <= current:
                        is_low_point = False
                        break

            if is_low_point:
                low_points.append((r, c))

    def find_basin_size(start_r, start_c):
        visited = set()
        queue = deque([(start_r, start_c)])
        visited.add((start_r, start_c))
        size = 0

        while queue:
            r, c = queue.popleft()
            size += 1

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if (nr, nc) not in visited and grid[nr][nc] != 9:
                        visited.add((nr, nc))
                        queue.append((nr, nc))

        return size

    basin_sizes = []
    for r, c in low_points:
        basin_sizes.append(find_basin_size(r, c))

    basin_sizes.sort(reverse=True)
    answer = basin_sizes[0] * basin_sizes[1] * basin_sizes[2]

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
