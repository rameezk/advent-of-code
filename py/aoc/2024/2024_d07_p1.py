import re
from itertools import product

from aoc.helper import AOC


@AOC.puzzle(year=2024, day=7, part=1)
def solve():
    data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""
    data = AOC.get_data()

    total = 0
    for line in data.strip().splitlines():
        numbers = list(map(int, re.findall(r"\d+", line)))
        should_equal, operands = numbers[0], numbers[1:]

        possible_operators = get_possible_operators(len(operands) - 1)

        found = False
        for operators in possible_operators:
            ans = calculate(operands[0], operands[1], operators[0])

            for i in range(2, len(operands)):
                ans = calculate(ans, operands[i], operators[i - 1])

            if ans == should_equal:
                found = True
                break

        if found:
            total += should_equal

    print(total)
    AOC.submit_answer(total)


def calculate(n1, n2, op):
    if op == "+":
        return n1 + n2
    else:
        return n1 * n2


def get_possible_operators(operator_count):
    return list(product(["*", "+"], repeat=operator_count))


if __name__ == "__main__":
    solve()
