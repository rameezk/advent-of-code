from aoc.helper import AOC
from collections import defaultdict


@AOC.puzzle(2024, 22, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """1
# 2
# 3
# 2024""".splitlines()

    def next_secret(secret):
        secret = (secret ^ (secret * 64)) % 16777216
        secret = (secret ^ (secret // 32)) % 16777216
        secret = (secret ^ (secret * 2048)) % 16777216
        return secret

    all_sequences = defaultdict(int)

    for line in data:
        secret = int(line)
        prices = [secret % 10]

        for _ in range(2000):
            secret = next_secret(secret)
            prices.append(secret % 10)

        changes = [prices[i+1] - prices[i] for i in range(len(prices)-1)]

        seen_sequences = set()
        for i in range(len(changes) - 3):
            seq = tuple(changes[i:i+4])
            if seq not in seen_sequences:
                seen_sequences.add(seq)
                price = prices[i+4]
                all_sequences[seq] += price

    max_bananas = max(all_sequences.values())

    AOC.submit_answer(max_bananas)


if __name__ == "__main__":
    solve()
