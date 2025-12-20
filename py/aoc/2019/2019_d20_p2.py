from aoc.helper import AOC
from collections import deque, defaultdict


@AOC.puzzle(2019, 20, 2)
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

    def is_outer(r, c):
        return r <= 2 or c <= 2 or r >= height - 3 or c >= width - 3

    start = portal_positions['AA'][0]
    end = portal_positions['ZZ'][0]

    queue = deque([(start, 0, 0)])
    visited = {(start, 0)}

    while queue:
        pos, level, steps = queue.popleft()

        if pos == end and level == 0:
            answer = steps
            print(answer)
            AOC.submit_answer(answer)
            return

        r, c = pos
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < height and 0 <= nc < width and grid[nr][nc] == '.' and ((nr, nc), level) not in visited:
                visited.add(((nr, nc), level))
                queue.append(((nr, nc), level, steps + 1))

        if pos in portal_map:
            label = portals[pos]
            if label not in ['AA', 'ZZ']:
                portal_dest = portal_map[pos]
                outer = is_outer(r, c)

                if outer:
                    new_level = level - 1
                else:
                    new_level = level + 1

                if new_level >= 0 and (portal_dest, new_level) not in visited:
                    visited.add((portal_dest, new_level))
                    queue.append((portal_dest, new_level, steps + 1))


if __name__ == "__main__":
    solve()
