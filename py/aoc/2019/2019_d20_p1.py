from aoc.helper import AOC
from collections import deque, defaultdict


@AOC.puzzle(2019, 20, 1)
def solve():
    data = AOC.get_data().splitlines()

    grid = [list(line) for line in data]
    height = len(grid)
    width = max(len(row) for row in grid)

    for row in grid:
        while len(row) < width:
            row.append(' ')

    portals = {}
    portal_positions = defaultdict(list)

    for r in range(height):
        for c in range(width):
            if grid[r][c].isalpha():
                label = None
                pos = None

                if r + 1 < height and grid[r+1][c].isalpha():
                    label = grid[r][c] + grid[r+1][c]
                    if r > 0 and grid[r-1][c] == '.':
                        pos = (r-1, c)
                    elif r + 2 < height and grid[r+2][c] == '.':
                        pos = (r+2, c)

                elif c + 1 < width and grid[r][c+1].isalpha():
                    label = grid[r][c] + grid[r][c+1]
                    if c > 0 and grid[r][c-1] == '.':
                        pos = (r, c-1)
                    elif c + 2 < width and grid[r][c+2] == '.':
                        pos = (r, c+2)

                if label and pos:
                    portal_positions[label].append(pos)
                    portals[pos] = label

    portal_map = {}
    for label, positions in portal_positions.items():
        if len(positions) == 2:
            portal_map[positions[0]] = positions[1]
            portal_map[positions[1]] = positions[0]

    start = portal_positions['AA'][0]
    end = portal_positions['ZZ'][0]

    queue = deque([(start, 0)])
    visited = {start}

    while queue:
        pos, steps = queue.popleft()

        if pos == end:
            answer = steps
            print(answer)
            AOC.submit_answer(answer)
            return

        r, c = pos
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < height and 0 <= nc < width and grid[nr][nc] == '.' and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), steps + 1))

        if pos in portal_map:
            portal_dest = portal_map[pos]
            if portal_dest not in visited:
                visited.add(portal_dest)
                queue.append((portal_dest, steps + 1))


if __name__ == "__main__":
    solve()
