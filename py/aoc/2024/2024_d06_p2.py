import multiprocessing
from functools import partial

from aoc.helper import AOC
from aoc.util import benchmark

DIRECTION_MOVEMENT = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}


@benchmark
@AOC.puzzle(year=2024, day=6, part=2)
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

    positions_to_check = []
    for row_i, row in enumerate(map_):
        for col_i, col in enumerate(row):
            if (row_i, col_i) == guard_position:
                continue
            if col == "#":
                continue
            positions_to_check.append((row_i, col_i))

    fixed_detect_loop = partial(detect_loop, map_, guard_position, guard_facing)

    with multiprocessing.Pool() as pool:
        results = pool.map(fixed_detect_loop, positions_to_check)
        loop_count = sum(results)
        print(loop_count)
        AOC.submit_answer(loop_count)


def get_starting_position(map_):
    for row_i, row in enumerate(map_):
        for col_i, col in enumerate(row):
            if col == "^":
                return row_i, col_i
    else:
        raise Exception("Cannot find starting position")


def detect_loop(map_, position, direction, obstacle_position):
    path = set()

    while True:
        if (position, direction) in path:
            return True

        path.add((position, direction))

        ahead = (
            position[0] + DIRECTION_MOVEMENT[direction][0],
            position[1] + DIRECTION_MOVEMENT[direction][1],
        )

        if is_out_of_bounds(map_, ahead):
            return False

        if obstacle_position == ahead or is_obstacle(map_, ahead):
            direction = turn_right(direction)
            continue

        position = ahead


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
    return (
        map_[position[0]][position[1]] == "#" or map_[position[0]][position[1]] == "O"
    )


def is_out_of_bounds(map_, guard_position):
    return (
        guard_position[0] < 0
        or guard_position[0] >= len(map_)
        or guard_position[1] < 0
        or guard_position[1] >= len(map_[0])
    )


if __name__ == "__main__":
    solve()
