from aoc.helper import AOC

@AOC.puzzle(2017, 3, 2)
def solve():
    data = AOC.get_data().strip()
    target = int(data)

    grid = {(0, 0): 1}
    x, y = 0, 0
    dx, dy = 1, 0

    while True:
        x += dx
        y += dy

        value = 0
        for nx in range(x - 1, x + 2):
            for ny in range(y - 1, y + 2):
                if (nx, ny) != (x, y) and (nx, ny) in grid:
                    value += grid[(nx, ny)]

        grid[(x, y)] = value

        if value > target:
            AOC.submit_answer(value)
            return

        if dx == 1 and dy == 0 and (x, y + 1) not in grid:
            dx, dy = 0, 1
        elif dx == 0 and dy == 1 and (x - 1, y) not in grid:
            dx, dy = -1, 0
        elif dx == -1 and dy == 0 and (x, y - 1) not in grid:
            dx, dy = 0, -1
        elif dx == 0 and dy == -1 and (x + 1, y) not in grid:
            dx, dy = 1, 0

if __name__ == "__main__":
    solve()
