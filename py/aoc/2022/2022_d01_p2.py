from aoc.helper import AOC


@AOC.puzzle(2022, 1, 2)
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
    calories_list = []

    for elf in elves:
        calories = sum(int(line) for line in elf.split("\n"))
        calories_list.append(calories)

    calories_list.sort(reverse=True)
    top_three = sum(calories_list[:3])

    print(top_three)
    AOC.submit_answer(top_three)


if __name__ == "__main__":
    solve()
