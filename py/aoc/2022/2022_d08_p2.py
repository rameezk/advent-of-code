from aoc.helper import AOC


@AOC.puzzle(2022, 8, 2)
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

    max_score = 0

    for r in range(rows):
        for c in range(cols):
            height = grid[r][c]

            up = 0
            for i in range(r - 1, -1, -1):
                up += 1
                if grid[i][c] >= height:
                    break

            down = 0
            for i in range(r + 1, rows):
                down += 1
                if grid[i][c] >= height:
                    break

            left = 0
            for i in range(c - 1, -1, -1):
                left += 1
                if grid[r][i] >= height:
                    break

            right = 0
            for i in range(c + 1, cols):
                right += 1
                if grid[r][i] >= height:
                    break

            score = up * down * left * right
            max_score = max(max_score, score)

    print(max_score)
    AOC.submit_answer(max_score)


if __name__ == "__main__":
    solve()
