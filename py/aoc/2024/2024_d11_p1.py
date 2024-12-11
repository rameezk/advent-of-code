from aoc.helper import AOC


@AOC.puzzle(year=2024, day=11, part=1)
def solve():
    data = "125 17"
    data = AOC.get_data()

    stones = [int(s) for s in data.strip().split(" ")]

    new_stones = stones
    for i in range(25):
        new_stones = blink(new_stones)

    num_stones = len(new_stones)
    print(num_stones)
    AOC.submit_answer(num_stones)


def blink(stones: list[int]) -> list[int]:
    new_stones = []

    for stone in stones:
        if stone == 0:
            new_stones.append(1)
            continue

        stone_s = str(stone)
        if len(stone_s) % 2 == 0:
            l, r = stone_s[: len(stone_s) // 2], stone_s[len(stone_s) // 2 :]
            new_stones.append(int(l))
            new_stones.append(int(r))
            continue

        new_stones.append(int(stone) * 2024)

    return new_stones


if __name__ == "__main__":
    solve()
