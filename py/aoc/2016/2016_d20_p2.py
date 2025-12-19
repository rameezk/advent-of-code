from aoc.helper import AOC


@AOC.puzzle(2016, 20, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """5-8
# 0-2
# 4-7""".strip().splitlines()

    ranges = []
    for line in data:
        start, end = map(int, line.split('-'))
        ranges.append((start, end))

    ranges.sort()

    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))

    max_ip = 4294967295
    allowed = 0

    if merged[0][0] > 0:
        allowed += merged[0][0]

    for i in range(len(merged) - 1):
        gap = merged[i + 1][0] - merged[i][1] - 1
        allowed += gap

    if merged[-1][1] < max_ip:
        allowed += max_ip - merged[-1][1]

    print(allowed)
    AOC.submit_answer(allowed)


if __name__ == "__main__":
    solve()
