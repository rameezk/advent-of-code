from aoc.helper import AOC


@AOC.puzzle(2022, 25, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """1=-0-2
# 12111
# 2=0=
# 21
# 2=01
# 111
# 20012
# 112
# 1=-1=
# 1-12
# 12
# 1=
# 122""".strip().splitlines()

    def snafu_to_decimal(snafu):
        snafu_map = {'2': 2, '1': 1, '0': 0, '-': -1, '=': -2}
        result = 0
        for i, digit in enumerate(reversed(snafu)):
            result += snafu_map[digit] * (5 ** i)
        return result

    def decimal_to_snafu(decimal):
        if decimal == 0:
            return '0'

        digits = []
        while decimal > 0:
            remainder = decimal % 5
            decimal //= 5

            if remainder <= 2:
                digits.append(str(remainder))
            elif remainder == 3:
                digits.append('=')
                decimal += 1
            elif remainder == 4:
                digits.append('-')
                decimal += 1

        return ''.join(reversed(digits))

    total_decimal = sum(snafu_to_decimal(line) for line in data)
    result = decimal_to_snafu(total_decimal)

    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
