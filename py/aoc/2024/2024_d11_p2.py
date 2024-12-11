from collections import Counter

from aoc.helper import AOC


@AOC.puzzle(year=2024, day=11, part=2)
def solve():
    data = "125 17"
    data = AOC.get_data()

    stones = [int(s) for s in data.strip().split(" ")]

    stone_counts = Counter(stones)

    repeat = 75
    for i in range(repeat):
        new_stone_counts = Counter()
        for stone, stone_count in stone_counts.items():
            new_stones = apply_rule(stone)
            for new_stone in new_stones:
                new_stone_counts[new_stone] += stone_count
        stone_counts = new_stone_counts

    num_stones = sum(stone_counts.values())
    print(num_stones)
    AOC.submit_answer(num_stones)


def apply_rule(stone: int) -> list[int]:
    if stone == 0:
        return [1]

    stone_s = str(stone)
    if len(stone_s) % 2 == 0:
        l, r = stone_s[: len(stone_s) // 2], stone_s[len(stone_s) // 2 :]
        return [int(l), int(r)]

    return [int(stone) * 2024]


if __name__ == "__main__":
    solve()
