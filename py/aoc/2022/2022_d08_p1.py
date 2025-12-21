from aoc.helper import AOC


@AOC.puzzle(2022, 8, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """30373
# 25512
# 65332
# 33549
# 35390"""

    lines = data.splitlines()
    grid = [[int(c) for c in line] for line in lines]
    rows = len(grid)
    cols = len(grid[0])

    visible = set()

    for r in range(rows):
        for c in range(cols):
            if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                visible.add((r, c))
                continue

            height = grid[r][c]

            visible_from_left = all(grid[r][i] < height for i in range(c))
            visible_from_right = all(grid[r][i] < height for i in range(c + 1, cols))
            visible_from_top = all(grid[i][c] < height for i in range(r))
            visible_from_bottom = all(grid[i][c] < height for i in range(r + 1, rows))

            if visible_from_left or visible_from_right or visible_from_top or visible_from_bottom:
                visible.add((r, c))

    answer = len(visible)
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
