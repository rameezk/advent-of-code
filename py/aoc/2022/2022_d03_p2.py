from aoc.helper import AOC


@AOC.puzzle(2022, 3, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw""".strip().splitlines()

    total = 0
    for i in range(0, len(data), 3):
        elf1 = set(data[i])
        elf2 = set(data[i + 1])
        elf3 = set(data[i + 2])

        common = (elf1 & elf2 & elf3).pop()

        if common.islower():
            priority = ord(common) - ord('a') + 1
        else:
            priority = ord(common) - ord('A') + 27

        total += priority

    print(total)
    AOC.submit_answer(total)


if __name__ == "__main__":
    solve()
