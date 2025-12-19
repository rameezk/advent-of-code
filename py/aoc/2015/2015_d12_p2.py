from aoc.helper import AOC
import json


def sum_numbers(obj, ignore_red=False):
    if isinstance(obj, int):
        return obj
    elif isinstance(obj, list):
        return sum(sum_numbers(item, ignore_red) for item in obj)
    elif isinstance(obj, dict):
        if ignore_red and "red" in obj.values():
            return 0
        return sum(sum_numbers(value, ignore_red) for value in obj.values())
    else:
        return 0


@AOC.puzzle(2015, 12, 2)
def solve():
    data = AOC.get_data().strip()

    parsed = json.loads(data)
    result = sum_numbers(parsed, ignore_red=True)

    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
