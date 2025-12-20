from aoc.helper import AOC

@AOC.puzzle(2021, 3, 1)
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

    num_bits = len(data[0])
    num_numbers = len(data)

    gamma_bits = []
    epsilon_bits = []

    for bit_pos in range(num_bits):
        ones = sum(1 for num in data if num[bit_pos] == '1')
        zeros = num_numbers - ones

        if ones > zeros:
            gamma_bits.append('1')
            epsilon_bits.append('0')
        else:
            gamma_bits.append('0')
            epsilon_bits.append('1')

    gamma = int(''.join(gamma_bits), 2)
    epsilon = int(''.join(epsilon_bits), 2)

    answer = gamma * epsilon

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
