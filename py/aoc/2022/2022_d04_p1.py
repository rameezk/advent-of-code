from aoc.helper import AOC


@AOC.puzzle(2022, 4, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """2-4,6-8
# 2-3,4-5
# 5-7,7-9
# 2-8,3-7
# 6-6,4-6
# 2-6,4-8""".strip().splitlines()

    count = 0
    for line in data:
        pair1, pair2 = line.split(',')
        start1, end1 = map(int, pair1.split('-'))
        start2, end2 = map(int, pair2.split('-'))

        if (start1 <= start2 and end1 >= end2) or (start2 <= start1 and end2 >= end1):
            count += 1

    print(count)
    AOC.submit_answer(count)


if __name__ == "__main__":
    solve()
