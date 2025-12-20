from aoc.helper import AOC

@AOC.puzzle(2021, 3, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

    sample_data = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

#     data = sample_data.splitlines()

    def find_rating(numbers, prefer_most_common):
        remaining = numbers[:]
        bit_pos = 0

        while len(remaining) > 1:
            ones = sum(1 for num in remaining if num[bit_pos] == '1')
            zeros = len(remaining) - ones

            if prefer_most_common:
                keep_bit = '1' if ones >= zeros else '0'
            else:
                keep_bit = '0' if zeros <= ones else '1'

            remaining = [num for num in remaining if num[bit_pos] == keep_bit]
            bit_pos += 1

        return int(remaining[0], 2)

    oxygen = find_rating(data, True)
    co2 = find_rating(data, False)

    answer = oxygen * co2

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
