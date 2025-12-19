from aoc.helper import AOC


@AOC.puzzle(2016, 20, 1)
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

    if merged[0][0] > 0:
        result = 0
    else:
        result = merged[0][1] + 1

    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
