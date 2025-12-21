from aoc.helper import AOC


@AOC.puzzle(2022, 3, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """vJrwpWtwJgWrhcsFMMfFFhFp
# jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
# PmmdzqPrVvPwwTWBwg
# wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
# ttgJtRGJQctTZtZT
# CrZsJsPPZsGzwwsLwLmpwMDw""".strip().splitlines()

    total = 0
    for line in data:
        mid = len(line) // 2
        first_compartment = set(line[:mid])
        second_compartment = set(line[mid:])

        common = (first_compartment & second_compartment).pop()

        if common.islower():
            priority = ord(common) - ord('a') + 1
        else:
            priority = ord(common) - ord('A') + 27

        total += priority

    print(total)
    AOC.submit_answer(total)


if __name__ == "__main__":
    solve()
