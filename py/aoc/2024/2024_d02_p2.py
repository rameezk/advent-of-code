import pathlib
from itertools import pairwise

from aoc.helper import download_input, submit_answer


def is_safe(levels: list[int]) -> bool:
    differences = [p2 - p1 for p1, p2 in pairwise(levels)]
    return all(0 < d < 4 for d in differences) or all(-4 < d < 0 for d in differences)


def is_safe_when_removing_a_level(levels: list[int]) -> bool:
    for i in range(len(levels)):
        s = levels.copy()
        s.pop(i)
        if is_safe(s):
            return True
    return False


if __name__ == "__main__":
    download_input(2024, 2)

    input_file = pathlib.Path(__file__).parent.resolve() / "./2024_d02.txt"

    with open(input_file) as f:
        data = f.read().strip().splitlines()

    #     data = """7 6 4 2 1
    # 1 2 7 8 9
    # 9 7 6 2 1
    # 1 3 2 4 5
    # 8 6 4 4 1
    # 1 3 6 7 9""".strip().splitlines()

    safe_report_count = 0
    for report in data:
        levels = list(map(int, report.split()))
        if is_safe(levels):
            safe_report_count += 1
        else:
            if is_safe_when_removing_a_level(levels):
                safe_report_count += 1

    print(safe_report_count)
    submit_answer(2024, 2, 2, safe_report_count)
