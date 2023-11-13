from aoc.helper import download_input, submit_answer

import itertools

from typing import Tuple


def move(coord: Tuple[int, int]) -> Tuple[int, int]:
    dx, dy = coord

    if d == ">":
        dx += 1
    elif d == "<":
        dx -= 1
    elif d == "^":
        dy += 1
    else:
        dy -= 1

    return dx, dy


if __name__ == "__main__":
    # download_input(2015, 3)

    with open("./2015_d03.txt") as f:
        data = f.read().strip()

    # data = "^v^v^v^v^v"

    c1 = (0, 0)
    c2 = (0, 0)

    v = {(0, 0)}
    p = 1
    for d in data:
        if p == 1:
            c1 = move(c1)
            v.add(c1)
        else:
            c2 = move(c2)
            v.add(c2)

        p = 2 if p == 1 else 1

    h = len(v)
    print(h)
    # submit_answer(2015, 3, 2, h)
