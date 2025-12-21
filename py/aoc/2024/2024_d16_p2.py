from aoc.helper import AOC
import heapq
from collections import defaultdict


@AOC.puzzle(2024, 16, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############""".strip().splitlines()

    grid = [list(line) for line in data]
    rows, cols = len(grid), len(grid[0])

    start = end = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    start_dir = 0

    pq = [(0, start[0], start[1], start_dir, [start])]
    visited = {}
    min_cost = float('inf')
    all_paths = []

    while pq:
        cost, r, c, d, path = heapq.heappop(pq)

        if cost > min_cost:
            break

        if (r, c) == end:
            if cost < min_cost:
                min_cost = cost
                all_paths = [path]
            elif cost == min_cost:
                all_paths.append(path)
            continue

        state = (r, c, d)
        if state in visited and visited[state] < cost:
            continue
        visited[state] = cost

        dr, dc = directions[d]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
            heapq.heappush(pq, (cost + 1, nr, nc, d, path + [(nr, nc)]))

        heapq.heappush(pq, (cost + 1000, r, c, (d + 1) % 4, path))
        heapq.heappush(pq, (cost + 1000, r, c, (d - 1) % 4, path))

    tiles = set()
    for path in all_paths:
        for tile in path:
            tiles.add(tile)

    print(len(tiles))
    AOC.submit_answer(len(tiles))


if __name__ == "__main__":
    solve()
