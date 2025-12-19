from aoc.helper import AOC

@AOC.puzzle(2017, 22, 2)
def solve():
    data = AOC.get_data().strip()
    # data = """..#
# #..
# ..."""

    lines = data.split('\n')
    state = {}

    CLEAN = 0
    WEAKENED = 1
    INFECTED = 2
    FLAGGED = 3

    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            if char == '#':
                state[(row, col)] = INFECTED
            else:
                state[(row, col)] = CLEAN

    size = len(lines)
    y, x = size // 2, size // 2

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction = 0

    infections = 0

    for _ in range(10000000):
        current_state = state.get((y, x), CLEAN)

        if current_state == CLEAN:
            direction = (direction - 1) % 4
        elif current_state == WEAKENED:
            pass
        elif current_state == INFECTED:
            direction = (direction + 1) % 4
        elif current_state == FLAGGED:
            direction = (direction + 2) % 4

        if current_state == CLEAN:
            state[(y, x)] = WEAKENED
        elif current_state == WEAKENED:
            state[(y, x)] = INFECTED
            infections += 1
        elif current_state == INFECTED:
            state[(y, x)] = FLAGGED
        elif current_state == FLAGGED:
            state[(y, x)] = CLEAN

        dy, dx = directions[direction]
        y += dy
        x += dx

    answer = infections
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
