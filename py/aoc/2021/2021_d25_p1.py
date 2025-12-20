from aoc.helper import AOC

@AOC.puzzle(2021, 25, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """v...>>.vv>
# .vv>>.vv..
# >>.>v>...v
# >>v>>.>.v.
# v>v.vv.v..
# >.>>..v...
# .vv..>.>v.
# v.v..>>v.v
# ....v..v.>""".splitlines()

    grid = {}
    height = len(data)
    width = len(data[0])

    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char in '>v':
                grid[(x, y)] = char

    step = 0
    while True:
        step += 1
        moved = False

        new_grid = {}
        for (x, y), char in grid.items():
            if char == '>':
                next_x = (x + 1) % width
                if (next_x, y) not in grid:
                    new_grid[(next_x, y)] = char
                    moved = True
                else:
                    new_grid[(x, y)] = char
            else:
                new_grid[(x, y)] = char

        grid = new_grid

        new_grid = {}
        for (x, y), char in grid.items():
            if char == 'v':
                next_y = (y + 1) % height
                if (x, next_y) not in grid:
                    new_grid[(x, next_y)] = char
                    moved = True
                else:
                    new_grid[(x, y)] = char
            else:
                new_grid[(x, y)] = char

        grid = new_grid

        if not moved:
            break

    answer = step
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
