from aoc.helper import AOC


@AOC.puzzle(2025, 3, 1)
def solve():
    data = AOC.get_data()

#     data = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""

    total = 0
    for line in data.strip().splitlines():
        digits = line
        max_joltage = 0

        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                joltage = int(digits[i] + digits[j])
                max_joltage = max(max_joltage, joltage)

        total += max_joltage

    print(total)
    AOC.submit_answer(total)

if __name__ == "__main__":
    solve()
