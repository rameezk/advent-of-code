from aoc.helper import AOC
import math


@AOC.puzzle(2016, 23, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """cpy 2 a
# tgl a
# tgl a
# tgl a
# cpy 1 a
# dec a
# dec a""".splitlines()

    result = math.factorial(12) + 75 * 97

    print(f"Register a: {result}")
    AOC.submit_answer(result)
    return result


if __name__ == "__main__":
    solve()
