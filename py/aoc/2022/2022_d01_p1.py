from aoc.helper import AOC


@AOC.puzzle(2022, 1, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """1000
# 2000
# 3000
#
# 4000
#
# 5000
# 6000
#
# 7000
# 8000
# 9000
#
# 10000"""

    elves = data.split("\n\n")
    max_calories = 0

    for elf in elves:
        calories = sum(int(line) for line in elf.split("\n"))
        max_calories = max(max_calories, calories)

    print(max_calories)
    AOC.submit_answer(max_calories)


if __name__ == "__main__":
    solve()
