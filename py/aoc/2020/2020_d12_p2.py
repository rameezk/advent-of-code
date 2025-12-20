from aoc.helper import AOC

@AOC.puzzle(2020, 12, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """F10
# N3
# F7
# R90
# F11""".splitlines()

    ship_x, ship_y = 0, 0
    waypoint_x, waypoint_y = 10, 1

    for line in data:
        action = line[0]
        value = int(line[1:])

        if action == 'N':
            waypoint_y += value
        elif action == 'S':
            waypoint_y -= value
        elif action == 'E':
            waypoint_x += value
        elif action == 'W':
            waypoint_x -= value
        elif action == 'L':
            for _ in range(value // 90):
                waypoint_x, waypoint_y = -waypoint_y, waypoint_x
        elif action == 'R':
            for _ in range(value // 90):
                waypoint_x, waypoint_y = waypoint_y, -waypoint_x
        elif action == 'F':
            ship_x += waypoint_x * value
            ship_y += waypoint_y * value

    answer = abs(ship_x) + abs(ship_y)

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
