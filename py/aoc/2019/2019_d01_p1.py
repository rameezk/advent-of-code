from aoc.helper import AOC


@AOC.puzzle(2019, 1, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """12
# 14
# 1969
# 100756""".splitlines()

    answer = sum(int(mass) // 3 - 2 for mass in data)
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
