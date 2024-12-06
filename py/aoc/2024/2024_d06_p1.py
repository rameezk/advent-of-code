from aoc.helper import AOC

DIRECTION_MOVEMENT = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}


@AOC.puzzle(year=2024, day=6, part=1)
def solve():
    data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

    data = AOC.get_data()
    map_ = [line for line in data.strip().splitlines()]

    guard_facing = "N"
    guard_position = get_starting_position(map_)

    path = walk(map_, guard_position, guard_facing)
    result = len(path)
    print(result)
    AOC.submit_answer(result)


def get_starting_position(map_):
    for row_i, row in enumerate(map_):
        for col_i, col in enumerate(row):
            if col == "^":
                return row_i, col_i
    else:
        raise Exception("Cannot find starting position")


def walk(map_, position, direction):
    path = set()

    while True:
        path.add(position)
        ahead = (
            position[0] + DIRECTION_MOVEMENT[direction][0],
            position[1] + DIRECTION_MOVEMENT[direction][1],
        )

        if is_out_of_bounds(map_, ahead):
            break

        if is_obstacle(map_, ahead):
            direction = turn_right(direction)
            continue

        position = ahead

    return path


def turn_right(direction):
    if direction == "N":
        return "E"
    if direction == "E":
        return "S"
    if direction == "S":
        return "W"
    if direction == "W":
        return "N"


def is_obstacle(map_, position):
    return map_[position[0]][position[1]] == "#"


def is_out_of_bounds(map_, guard_position):
    return (
        guard_position[0] < 0
        or guard_position[0] >= len(map_)
        or guard_position[1] < 0
        or guard_position[1] >= len(map_[0])
    )


if __name__ == "__main__":
    solve()
