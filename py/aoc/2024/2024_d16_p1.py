from aoc.helper import AOC
import heapq


@AOC.puzzle(2024, 16, 1)
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
    dir_names = ['E', 'S', 'W', 'N']

    start_dir = 0

    pq = [(0, start[0], start[1], start_dir)]
    visited = set()

    while pq:
        cost, r, c, d = heapq.heappop(pq)

        if (r, c) == end:
            print(cost)
            AOC.submit_answer(cost)
            return

        if (r, c, d) in visited:
            continue
        visited.add((r, c, d))

        dr, dc = directions[d]
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
            heapq.heappush(pq, (cost + 1, nr, nc, d))

        heapq.heappush(pq, (cost + 1000, r, c, (d + 1) % 4))
        heapq.heappush(pq, (cost + 1000, r, c, (d - 1) % 4))


if __name__ == "__main__":
    solve()
