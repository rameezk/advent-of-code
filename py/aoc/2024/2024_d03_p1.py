from aoc.helper import AOC

import re


@AOC.puzzle(year=2024, day=3, part=1)
def solve():
    data = AOC.get_data()
    # data = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

    matches = re.findall(r"mul\((\d+),(\d+)\)", data)

    result = 0
    for d1, d2 in matches:
        result += int(d1) * int(d2)

    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
