from aoc.helper import AOC

@AOC.puzzle(2020, 11, 2)
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

    def get_visible_seats(grid, row, col):
        visible = []
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < rows and 0 <= c < cols:
                if grid[r][c] != '.':
                    visible.append(grid[r][c])
                    break
                r += dr
                c += dc

        return visible

    def simulate_round(grid):
        rows, cols = len(grid), len(grid[0])
        new_grid = [list(row) for row in grid]
        changed = False

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '.':
                    continue

                visible = get_visible_seats(grid, r, c)
                occupied_count = visible.count('#')

                if grid[r][c] == 'L' and occupied_count == 0:
                    new_grid[r][c] = '#'
                    changed = True
                elif grid[r][c] == '#' and occupied_count >= 5:
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
