from aoc.helper import AOC
import re


@AOC.puzzle(2015, 12, 1)
def solve():
    data = AOC.get_data().strip()

    numbers = re.findall(r'-?\d+', data)
    result = sum(int(num) for num in numbers)

    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
