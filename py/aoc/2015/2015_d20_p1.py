from aoc.helper import AOC


@AOC.puzzle(2015, 20, 1)
def solve():
    data = AOC.get_data().strip()
    target = int(data)

    max_house = target // 10
    houses = [0] * (max_house + 1)

    for elf in range(1, max_house + 1):
        for house in range(elf, max_house + 1, elf):
            houses[house] += elf * 10

    for house in range(1, max_house + 1):
        if houses[house] >= target:
            AOC.submit_answer(house)
            return


if __name__ == "__main__":
    solve()
