from aoc.helper import AOC


@AOC.puzzle(2024, 22, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """1
# 10
# 100
# 2024""".splitlines()

    def next_secret(secret):
        secret = (secret ^ (secret * 64)) % 16777216
        secret = (secret ^ (secret // 32)) % 16777216
        secret = (secret ^ (secret * 2048)) % 16777216
        return secret

    total = 0
    for line in data:
        secret = int(line)
        for _ in range(2000):
            secret = next_secret(secret)
        total += secret

    AOC.submit_answer(total)


if __name__ == "__main__":
    solve()
