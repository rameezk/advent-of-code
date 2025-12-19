from aoc.helper import AOC

@AOC.puzzle(2017, 22, 1)
def solve():
    data = AOC.get_data().strip()
    # data = """..#
# #..
# ..."""

    lines = data.split('\n')
    infected = set()

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == '#':
                infected.add((row, col))

    size = len(lines)
    y, x = size // 2, size // 2

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction = 0

    infections = 0

    for _ in range(10000):
        if (y, x) in infected:
            direction = (direction + 1) % 4
            infected.remove((y, x))
        else:
            direction = (direction - 1) % 4
            infected.add((y, x))
            infections += 1

        dy, dx = directions[direction]
        y += dy
        x += dx

    answer = infections
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
