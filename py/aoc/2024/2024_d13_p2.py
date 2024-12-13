import re

from aoc.helper import AOC


@AOC.puzzle(year=2024, day=13, part=2)
def solve():
    data = """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279"""
    data = AOC.get_data()

    token_a_cost = 3
    token_b_cost = 1

    total_cost = 0
    for machine in data.strip().split("\n\n"):
        lines = machine.splitlines()
        A, B, P = [parse_line(line) for line in lines]
        scale = 10_000_000_000_000
        P = (scale + P[0], scale + P[1])
        a_presses, b_presses = min_button_presses(A, B, P)
        cost = (a_presses * token_a_cost) + (b_presses * token_b_cost)
        total_cost += int(cost)

    print(total_cost)
    AOC.submit_answer(total_cost)


def parse_line(line):
    return tuple(map(int, (re.findall(r"\d+", line))))


def min_button_presses(A, B, P):
    ax, ay = A
    bx, by = B
    px, py = P

    a = (px * by - py * bx) // (by * ax - bx * ay)
    b = (px * ay - py * ax) // (ay * bx - by * ax)

    if ax * a + bx * b == px and ay * a + by * b == py:
        return a, b
    else:
        return 0, 0


if __name__ == "__main__":
    solve()
