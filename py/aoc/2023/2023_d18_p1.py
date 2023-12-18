from aoc.helper import download_input, submit_answer
from aoc.util import benchmark

from collections import defaultdict


def area_by_shoelace(x, y):
    return (
        abs(
            sum(i * j for i, j in zip(x, y[1:] + y[:1]))
            - sum(i * j for i, j in zip(x[1:] + x[:1], y))
        )
        / 2
    )


@benchmark
def run():
    download_input(2023, 18)

    dig_plan = """
R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
    """.strip().splitlines()

    with open("./2023_d18.txt") as f:
        dig_plan = f.read().strip().splitlines()

    r, c = (0, 0)
    points = [(r, c)]
    perimeter = 0
    for instruction in dig_plan:
        direction, by, _ = instruction.split(" ")
        by = int(by)
        perimeter += by
        if direction == "R":
            c += by
        elif direction == "D":
            r += by
        elif direction == "L":
            c -= by
        elif direction == "U":
            r -= by
        else:
            raise RuntimeError("Unknown direction", direction)
        points.append((r, c))

    x, y = zip(*points)
    A = area_by_shoelace(x, y)

    R = A + perimeter // 2 + 1
    print(R)
    # submit_answer(2023, 18, 1, R)


if __name__ == "__main__":
    run()
