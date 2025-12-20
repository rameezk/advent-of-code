from aoc.helper import AOC


@AOC.puzzle(2019, 24, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

    grid = [list(row) for row in data]
    h, w = len(grid), len(grid[0])

    seen = set()

    while True:
        state = tuple(tuple(row) for row in grid)
        if state in seen:
            break
        seen.add(state)

        new_grid = [['.'] * w for _ in range(h)]

        for r in range(h):
            for c in range(w):
                adjacent_bugs = 0
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == '#':
                        adjacent_bugs += 1

                if grid[r][c] == '#':
                    if adjacent_bugs == 1:
                        new_grid[r][c] = '#'
                else:
                    if adjacent_bugs in [1, 2]:
                        new_grid[r][c] = '#'

        grid = new_grid

    biodiversity = 0
    power = 1
    for r in range(h):
        for c in range(w):
            if grid[r][c] == '#':
                biodiversity += power
            power *= 2

    answer = biodiversity
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
