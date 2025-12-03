from aoc.helper import AOC


@AOC.puzzle(2025, 3, 2)
def solve():
    data = AOC.get_data()

#     data = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""

    total = 0
    for line in data.strip().splitlines():
        max_joltage = get_max(line, 12)
        total += max_joltage

    print(total)
    AOC.submit_answer(total)


def get_max(digits, k):
    n = len(digits)
    to_skip = n - k

    result = []
    start = 0

    for i in range(k):
        remaining_picks = k - i - 1
        end = min(start + to_skip + 1, n - remaining_picks)

        max_digit = max(digits[start:end])
        max_idx = digits.index(max_digit, start, end)

        result.append(max_digit)

        to_skip -= (max_idx - start)
        start = max_idx + 1

    return int(''.join(result))

if __name__ == "__main__":
    solve()
