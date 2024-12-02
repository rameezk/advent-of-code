from itertools import pairwise

from aoc.helper import AOC


@AOC.puzzle(2024, 2, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

    #     data = """7 6 4 2 1
    # 1 2 7 8 9
    # 9 7 6 2 1
    # 1 3 2 4 5
    # 8 6 4 4 1
    # 1 3 6 7 9""".strip().splitlines()

    safe_report_count = 0
    for report in data:
        levels = map(int, report.split())

        differences = [p2 - p1 for p1, p2 in pairwise(levels)]

        if all(0 < d < 4 for d in differences):
            safe_report_count += 1
            continue

        if all(-4 < d < 0 for d in differences):
            safe_report_count += 1
            continue

    print(safe_report_count)
    AOC.submit_answer(safe_report_count)


if __name__ == "__main__":
    solve()
