from typing import Tuple, LiteralString, Any

from aoc.helper import download_input, submit_answer
from aoc.util import benchmark

from functools import cache


@cache
def move_rocks(path: str, reverse: bool = False) -> str:
    if reverse:
        path = path[::-1]
    while ".O" in path:
        path = path.replace(".O", "O.")
    return path


@cache
def tilt_north(dish):
    cw_dish = zip(*dish)
    cw_dish = ["".join(r) for r in cw_dish]

    n_cw_dish = []
    for col in cw_dish:
        n_cw_dish.append(move_rocks(col))

    moved_dish = zip(*n_cw_dish)
    moved_dish = tuple("".join(r) for r in moved_dish)
    return moved_dish


@cache
def tilt_west(dish):
    n_dish = []
    for row in dish:
        n_dish.append(move_rocks(row))
    return tuple(n_dish)


@cache
def tilt_south(dish):
    cw_dish = zip(*dish)
    cw_dish = ["".join(r) for r in cw_dish]

    n_cw_dish = []
    for col in cw_dish:
        n_cw_dish.append(move_rocks(col, reverse=True)[::-1])

    moved_dish = zip(*n_cw_dish)
    moved_dish = tuple("".join(r) for r in moved_dish)
    return moved_dish


@cache
def tilt_east(dish):
    n_dish = []
    for row in dish:
        n_dish.append(move_rocks(row, reverse=True)[::-1])
    return tuple(n_dish)


@cache
def cycle_dish(dish):
    dish = tilt_north(dish)
    dish = tilt_west(dish)
    dish = tilt_south(dish)
    dish = tilt_east(dish)
    return dish


def print_dish(dish: list[list[str]]):
    for row in dish:
        print("".join(row))


@benchmark
def run():
    download_input(2023, 14)

    raw_dish = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
    """.strip().splitlines()

    with open("./2023_d14.txt") as f:
        raw_dish = f.read().strip().splitlines()

    dish = ()
    for row in raw_dish:
        dish = dish + (row,)

    cycles = 1000000000
    for c in range(1, cycles + 1):
        if c % 1000 == 0:
            print("cycle", c, "left", cycles - c)
        dish = cycle_dish(dish)

    T = 0
    for r, mv in enumerate(dish[::-1], start=1):
        rocks = list(mv).count("O")
        T += rocks * r

    print(T)
    # submit_answer(2023, 14, 2, T)


if __name__ == "__main__":
    run()
