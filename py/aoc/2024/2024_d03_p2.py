from aoc.helper import AOC

import re


def get_left_most_operation(position_operations, index) -> bool:
    on_the_left = (x for x in position_operations if x[0] <= index)
    return max(on_the_left)[1]


def get_positions_of_operation(op_regex, data) -> list[int]:
    return [i.start() for i in re.finditer(op_regex, data)]


@AOC.puzzle(year=2024, day=3, part=2)
def solve():
    data = AOC.get_data()
    # data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

    mul_matches = re.findall(r"mul\((\d+),(\d+)\)", data)

    positions_of_mul_ops = get_positions_of_operation(r"mul\((\d+),(\d+)\)", data)
    positions_of_do_ops = get_positions_of_operation(r"do\(\)", data)
    positions_of_dont_ops = get_positions_of_operation(r"don't\(\)", data)

    positions_of_do_ops.insert(0, 0)

    positions_of_do_ops = [(e, True) for e in positions_of_do_ops]
    positions_of_dont_ops = [(e, False) for e in positions_of_dont_ops]

    position_operations = sorted(positions_of_do_ops + positions_of_dont_ops)

    result = 0
    for position, (d1, d2) in zip(positions_of_mul_ops, mul_matches):
        if get_left_most_operation(position_operations, position):
            result += int(d1) * int(d2)

    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
