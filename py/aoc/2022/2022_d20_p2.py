from aoc.helper import AOC


@AOC.puzzle(2022, 20, 2)
def solve():
#     data = """1
# 2
# -3
# 3
# -2
# 0
# 4"""

    data = AOC.get_data().strip()

    DECRYPTION_KEY = 811589153
    ROUNDS = 10

    numbers = [int(x) * DECRYPTION_KEY for x in data.splitlines()]

    mixed = [(i, num) for i, num in enumerate(numbers)]

    for _ in range(ROUNDS):
        for i, num in enumerate(numbers):
            if num == 0:
                continue

            current_idx = next(idx for idx, (orig_i, _) in enumerate(mixed) if orig_i == i)

            item = mixed.pop(current_idx)

            new_idx = (current_idx + num) % len(mixed)

            mixed.insert(new_idx, item)

    values = [v for _, v in mixed]
    zero_idx = values.index(0)

    coord1 = values[(zero_idx + 1000) % len(values)]
    coord2 = values[(zero_idx + 2000) % len(values)]
    coord3 = values[(zero_idx + 3000) % len(values)]

    result = coord1 + coord2 + coord3

    print(f"1000th: {coord1}, 2000th: {coord2}, 3000th: {coord3}")
    print(f"Sum: {result}")

    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
