from aoc.helper import AOC


@AOC.puzzle(2018, 18, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """.#.#...|#.
# .....#|##|
# .|..|...#.
# ..|#.....#
# #.#|||#|#|
# ...#.||...
# .|....|...
# ||...#|.#|
# |.||||..|.
# ...#.|..|."""

    grid = [list(row) for row in data.splitlines()]
    rows = len(grid)
    cols = len(grid[0])

    def get_neighbors(r, c):
        neighbors = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    neighbors.append(grid[nr][nc])
        return neighbors

    for minute in range(10):
        new_grid = [row[:] for row in grid]

        for r in range(rows):
            for c in range(cols):
                cell = grid[r][c]
                neighbors = get_neighbors(r, c)

                if cell == '.':
                    if neighbors.count('|') >= 3:
                        new_grid[r][c] = '|'
                elif cell == '|':
                    if neighbors.count('#') >= 3:
                        new_grid[r][c] = '#'
                elif cell == '#':
                    if neighbors.count('#') >= 1 and neighbors.count('|') >= 1:
                        new_grid[r][c] = '#'
                    else:
                        new_grid[r][c] = '.'

        grid = new_grid

    wooded = sum(row.count('|') for row in grid)
    lumberyards = sum(row.count('#') for row in grid)
    result = wooded * lumberyards

    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
