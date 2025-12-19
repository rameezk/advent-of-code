from aoc.helper import AOC


@AOC.puzzle(2015, 18, 1)
def solve():
    data = AOC.get_data().strip()

    grid = [list(line) for line in data.split('\n')]
    rows = len(grid)
    cols = len(grid[0])

    def count_neighbors_on(g, r, c):
        count = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if g[nr][nc] == '#':
                        count += 1
        return count

    def step(g):
        new_grid = [row[:] for row in g]
        for r in range(rows):
            for c in range(cols):
                neighbors = count_neighbors_on(g, r, c)
                if g[r][c] == '#':
                    if neighbors not in [2, 3]:
                        new_grid[r][c] = '.'
                else:
                    if neighbors == 3:
                        new_grid[r][c] = '#'
        return new_grid

    for _ in range(100):
        grid = step(grid)

    result = sum(row.count('#') for row in grid)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
