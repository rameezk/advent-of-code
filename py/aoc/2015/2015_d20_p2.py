from aoc.helper import AOC


@AOC.puzzle(2015, 20, 2)
def solve():
    data = AOC.get_data().strip()
    target = int(data)

    max_house = target // 11
    houses = [0] * (max_house + 1)

    for elf in range(1, max_house + 1):
        visits = 0
        for house in range(elf, max_house + 1, elf):
            houses[house] += elf * 11
            visits += 1
            if visits >= 50:
                break

    for house in range(1, max_house + 1):
        if houses[house] >= target:
            AOC.submit_answer(house)
            return


if __name__ == "__main__":
    solve()
