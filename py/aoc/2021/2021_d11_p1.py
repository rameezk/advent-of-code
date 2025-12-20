from aoc.helper import AOC

@AOC.puzzle(2021, 11, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """5483143223
# 2745854711
# 5264556173
# 6141336146
# 6357385478
# 4167524645
# 2176841721
# 6882881134
# 4846848554
# 5283751526""".splitlines()

    grid = []
    for line in data:
        grid.append([int(c) for c in line])

    rows = len(grid)
    cols = len(grid[0])

    total_flashes = 0

    for step in range(100):
        flashed = set()

        for r in range(rows):
            for c in range(cols):
                grid[r][c] += 1

        changed = True
        while changed:
            changed = False
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] > 9 and (r, c) not in flashed:
                        flashed.add((r, c))
                        changed = True

                        for dr in [-1, 0, 1]:
                            for dc in [-1, 0, 1]:
                                if dr == 0 and dc == 0:
                                    continue
                                nr, nc = r + dr, c + dc
                                if 0 <= nr < rows and 0 <= nc < cols:
                                    grid[nr][nc] += 1

        for r, c in flashed:
            grid[r][c] = 0

        total_flashes += len(flashed)

    answer = total_flashes
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
