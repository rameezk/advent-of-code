from aoc.helper import download_input, submit_answer
from enum import Enum


class OutOfBoundsException(Exception):
    ...


class Direction(Enum):
    RIGHT = "RIGHT"
    LEFT = "LEFT"
    UP = "UP"
    DOWN = "DOWN"


def move_ahead(r, c, direction, max_c, max_r):
    if direction == Direction.RIGHT:
        if c == max_c:
            raise OutOfBoundsException()
        c += 1
    elif direction == Direction.LEFT:
        if c == 0:
            raise OutOfBoundsException()
        c -= 1
    elif direction == Direction.DOWN:
        if r == max_r:
            raise OutOfBoundsException()
        r += 1
    elif direction == Direction.UP:
        if r == 0:
            raise OutOfBoundsException()
        r -= 1
    else:
        raise RuntimeError("Unknown direction", direction)
    return r, c, direction


def energize(layout, start) -> int:
    max_c = len(layout[0]) - 1
    max_r = len(layout) - 1

    beams = [start]
    visited_tiles = set()
    checker = set()

    while beams:
        next_beams = []

        for beam in beams:
            r, c, direction = beam

            if (r, c, direction) in checker:
                continue

            visited_tiles.add((r, c))
            checker.add((r, c, direction))

            tile_is = layout[r][c]

            # print(r, c, tile_is, direction, len(visited_tiles))

            if (
                tile_is == "."
                or (
                    tile_is == "|"
                    and (direction == Direction.UP or direction == Direction.DOWN)
                )
                or (
                    tile_is == "-"
                    and (direction == Direction.LEFT or direction == Direction.RIGHT)
                )
            ):
                try:
                    r, c, direction = move_ahead(r, c, direction, max_c, max_r)
                    next_beams.append((r, c, direction))
                except OutOfBoundsException:
                    continue
            elif tile_is == "|":
                assert direction == Direction.RIGHT or direction == Direction.LEFT

                try:
                    r, c, direction = move_ahead(r, c, Direction.UP, max_c, max_r)
                    next_beams.append((r, c, direction))
                except OutOfBoundsException:
                    ...

                try:
                    r, c, direction = move_ahead(r, c, Direction.DOWN, max_c, max_r)
                    next_beams.append((r, c, direction))
                except OutOfBoundsException:
                    ...

            elif tile_is == "-":
                assert direction == Direction.UP or direction == Direction.DOWN

                try:
                    r, c, direction = move_ahead(r, c, Direction.LEFT, max_c, max_r)
                    next_beams.append((r, c, direction))
                except OutOfBoundsException:
                    ...

                try:
                    r, c, direction = move_ahead(r, c, Direction.RIGHT, max_c, max_r)
                    next_beams.append((r, c, direction))
                except OutOfBoundsException:
                    ...

            elif tile_is == "/":
                if direction == Direction.RIGHT:
                    new_direction = Direction.UP
                elif direction == Direction.LEFT:
                    new_direction = Direction.DOWN
                elif direction == Direction.UP:
                    new_direction = Direction.RIGHT
                elif direction == Direction.DOWN:
                    new_direction = Direction.LEFT
                else:
                    raise RuntimeError("Unknown direction", direction)

                try:
                    r, c, direction = move_ahead(r, c, new_direction, max_c, max_r)
                    next_beams.append((r, c, direction))
                except OutOfBoundsException:
                    ...

            elif tile_is == "\\":
                if direction == Direction.RIGHT:
                    new_direction = Direction.DOWN
                elif direction == Direction.LEFT:
                    new_direction = Direction.UP
                elif direction == Direction.UP:
                    new_direction = Direction.LEFT
                elif direction == Direction.DOWN:
                    new_direction = Direction.RIGHT
                else:
                    raise RuntimeError("Unknown direction", direction)

                try:
                    r, c, direction = move_ahead(r, c, new_direction, max_c, max_r)
                    next_beams.append((r, c, direction))
                except OutOfBoundsException:
                    ...

            else:
                raise RuntimeError("Unhandled case", r, c, tile_is, direction)

        beams = next_beams

    R = len(visited_tiles)
    return R


def run():
    download_input(2023, 16)

    layout = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
    """.strip().splitlines()

    with open("./2023_d16.txt") as f:
        layout = f.read().splitlines()

    M = 0

    # top row going down
    for c in range(len(layout[0])):
        e = energize(layout, (0, c, Direction.DOWN))
        M = max(M, e)

    # bottom row going up
    r = len(layout) - 1
    for c in range(len(layout[0])):
        e = energize(layout, (r, c, Direction.UP))
        M = max(M, e)

    # left row going right
    for r in range(len(layout)):
        e = energize(layout, (r, 0, Direction.RIGHT))
        M = max(M, e)

    # right row going left
    c = len(layout[0]) - 1
    for r in range(len(layout)):
        e = energize(layout, (r, c, Direction.RIGHT))
        M = max(M, e)

    print(M)
    submit_answer(2023, 16, 2, M)


if __name__ == "__main__":
    run()
