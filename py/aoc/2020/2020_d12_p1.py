from aoc.helper import AOC

@AOC.puzzle(2020, 12, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """F10
# N3
# F7
# R90
# F11""".splitlines()

    x, y = 0, 0
    direction = 0

    directions = {0: (1, 0), 90: (0, -1), 180: (-1, 0), 270: (0, 1)}

    for line in data:
        action = line[0]
        value = int(line[1:])

        if action == 'N':
            y += value
        elif action == 'S':
            y -= value
        elif action == 'E':
            x += value
        elif action == 'W':
            x -= value
        elif action == 'L':
            direction = (direction - value) % 360
        elif action == 'R':
            direction = (direction + value) % 360
        elif action == 'F':
            dx, dy = directions[direction]
            x += dx * value
            y += dy * value

    answer = abs(x) + abs(y)

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
