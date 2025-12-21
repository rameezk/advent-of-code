from aoc.helper import AOC
from collections import deque


@AOC.puzzle(2022, 12, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi""".strip().splitlines()

    grid = [list(line) for line in data]
    rows = len(grid)
    cols = len(grid[0])

    end = None
    starts = []

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                starts.append((r, c))
                grid[r][c] = 'a'
            elif grid[r][c] == 'E':
                end = (r, c)
                grid[r][c] = 'z'
            elif grid[r][c] == 'a':
                starts.append((r, c))

    def get_height(char):
        return ord(char) - ord('a')

    def bfs_from(start):
        queue = deque([(start, 0)])
        visited = {start}

        while queue:
            (r, c), steps = queue.popleft()

            if (r, c) == end:
                return steps

            current_height = get_height(grid[r][c])

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    next_height = get_height(grid[nr][nc])

                    if next_height <= current_height + 1:
                        visited.add((nr, nc))
                        queue.append(((nr, nc), steps + 1))

        return float('inf')

    min_steps = min(bfs_from(start) for start in starts)

    print(min_steps)
    AOC.submit_answer(min_steps)


if __name__ == "__main__":
    solve()
