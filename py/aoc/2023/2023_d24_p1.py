from aoc.helper import download_input, submit_answer
from aoc.util import benchmark
import re


@benchmark
def run():
    download_input(2023, 24)

    wind_data = """
Hailstone A: 19, 13, 30 @ -2, 1, -2
Hailstone B: 18, 19, 22 @ -1, -1, -2
    """

    wind_data = [parse_line(w) for w in wind_data.strip().splitlines()]

    hailstone_a = wind_data[0]
    hailstone_b = wind_data[1]

    ax, ay, _, axv, ayv, _ = hailstone_a
    bx, by, _, bxv, byv, _ = hailstone_b

    print((f"{ax}+{axv}t"))
    print((f"{bx}+{bxv}t"))

    a_s = ax - bx
    t_s = bxv - axv

    print(a_s, t_s)


def parse_line(line: str) -> [int]:
    return list(map(int, re.findall(r"-?\d+", line.strip())))


if __name__ == "__main__":
    run()
