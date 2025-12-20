from aoc.helper import AOC

@AOC.puzzle(2020, 10, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """16
# 10
# 15
# 5
# 1
# 11
# 7
# 19
# 6
# 12
# 4""".splitlines()

    adapters = [int(x) for x in data]
    adapters.sort()

    adapters = [0] + adapters + [adapters[-1] + 3]

    diff_1 = 0
    diff_3 = 0

    for i in range(1, len(adapters)):
        diff = adapters[i] - adapters[i-1]
        if diff == 1:
            diff_1 += 1
        elif diff == 3:
            diff_3 += 1

    answer = diff_1 * diff_3

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
