from aoc.helper import AOC
from collections import deque


@AOC.puzzle(2024, 20, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""

    grid = [list(line) for line in data.splitlines()]
    rows = len(grid)
    cols = len(grid[0])

    start = None
    end = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)

    def bfs(start_pos, end_pos):
        queue = deque([(start_pos, 0)])
        visited = {start_pos: 0}

        while queue:
            (r, c), dist = queue.popleft()

            if (r, c) == end_pos:
                return visited

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#':
                    if (nr, nc) not in visited:
                        visited[(nr, nc)] = dist + 1
                        queue.append(((nr, nc), dist + 1))

        return visited

    path_distances = bfs(start, end)
    normal_time = path_distances[end]

    cheats_count = 0

    for pos, dist_from_start in path_distances.items():
        r, c = pos

        for dr in range(-2, 3):
            for dc in range(-2, 3):
                cheat_dist = abs(dr) + abs(dc)
                if cheat_dist == 0 or cheat_dist > 2:
                    continue

                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    if (nr, nc) in path_distances:
                        dist_to_end_from_cheat = normal_time - path_distances[(nr, nc)]
                        total_with_cheat = dist_from_start + cheat_dist + dist_to_end_from_cheat
                        saved = normal_time - total_with_cheat

                        if saved >= 100:
                            cheats_count += 1

    print(cheats_count)
    AOC.submit_answer(cheats_count)


if __name__ == "__main__":
    solve()
