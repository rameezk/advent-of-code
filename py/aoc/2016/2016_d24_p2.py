from aoc.helper import AOC
from collections import deque
from itertools import permutations


@AOC.puzzle(2016, 24, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """###########
# #0.1.....2#
# #.#######.#
# #4.......3#
# ###########""".splitlines()

    grid = [list(line) for line in data]
    height = len(grid)
    width = len(grid[0])

    locations = {}
    for r in range(height):
        for c in range(width):
            if grid[r][c].isdigit():
                locations[int(grid[r][c])] = (r, c)

    def bfs(start, end):
        queue = deque([(start, 0)])
        visited = {start}

        while queue:
            (r, c), dist = queue.popleft()

            if (r, c) == end:
                return dist

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < height and 0 <= nc < width and (nr, nc) not in visited and grid[nr][nc] != '#':
                    visited.add((nr, nc))
                    queue.append(((nr, nc), dist + 1))

        return float('inf')

    distances = {}
    for i in locations:
        for j in locations:
            if i != j:
                distances[(i, j)] = bfs(locations[i], locations[j])

    non_zero = [loc for loc in locations if loc != 0]
    min_distance = float('inf')

    for perm in permutations(non_zero):
        path = [0] + list(perm) + [0]
        total = sum(distances[(path[i], path[i+1])] for i in range(len(path) - 1))
        min_distance = min(min_distance, total)

    print(min_distance)
    AOC.submit_answer(min_distance)


if __name__ == "__main__":
    solve()
