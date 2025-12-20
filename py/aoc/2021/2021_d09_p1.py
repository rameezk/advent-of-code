from aoc.helper import AOC

@AOC.puzzle(2021, 9, 1)
def solve():
    data = AOC.get_data().strip().splitlines()



    grid = [[int(c) for c in line] for line in data]
    rows = len(grid)
    cols = len(grid[0])

    low_points = []

    for r in range(rows):
        for c in range(cols):
            current = grid[r][c]
            is_low_point = True

            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] <= current:
                        is_low_point = False
                        break

            if is_low_point:
                low_points.append(current)

    answer = sum(1 + height for height in low_points)

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
