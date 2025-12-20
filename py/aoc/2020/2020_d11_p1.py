from aoc.helper import AOC

@AOC.puzzle(2020, 11, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """L.LL.LL.LL
# LLLLLLL.LL
# L.L.L..L..
# LLLL.LL.LL
# L.LL.LL.LL
# L.LLLLL.LL
# ..L.L.....
# LLLLLLLLLL
# L.LLLLLL.L
# L.LLLLL.LL""".splitlines()

    def get_adjacent_seats(grid, row, col):
        adjacent = []
        rows, cols = len(grid), len(grid[0])
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                r, c = row + dr, col + dc
                if 0 <= r < rows and 0 <= c < cols:
                    adjacent.append(grid[r][c])
        return adjacent

    def simulate_round(grid):
        rows, cols = len(grid), len(grid[0])
        new_grid = [list(row) for row in grid]
        changed = False

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '.':
                    continue

                adjacent = get_adjacent_seats(grid, r, c)
                occupied_count = adjacent.count('#')

                if grid[r][c] == 'L' and occupied_count == 0:
                    new_grid[r][c] = '#'
                    changed = True
                elif grid[r][c] == '#' and occupied_count >= 4:
                    new_grid[r][c] = 'L'
                    changed = True

        return [''.join(row) for row in new_grid], changed

    grid = data
    while True:
        grid, changed = simulate_round(grid)
        if not changed:
            break

    answer = sum(row.count('#') for row in grid)

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
