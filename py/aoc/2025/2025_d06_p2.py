from aoc.helper import AOC


@AOC.puzzle(2025, 6, 2)
def solve():
    data = AOC.get_data()

#     data = """123 328  51 64
#  45 64  387 23
#   6 98  215 314
# *   +   *   +  """

    lines = data.strip().split("\n")
    max_width = max(len(line) for line in lines)

    padded_lines = [line.ljust(max_width) for line in lines]

    problems = []
    col = 0
    while col < max_width:
        if any(padded_lines[row][col] != ' ' for row in range(len(padded_lines))):
            problem_width = 0
            while col + problem_width < max_width:
                if all(padded_lines[row][col + problem_width] == ' ' for row in range(len(padded_lines))):
                    break
                problem_width += 1

            operator = None

            problem_chars = []
            for row in range(len(padded_lines)):
                row_chars = padded_lines[row][col:col+problem_width]
                problem_chars.append(row_chars)

            last_row = problem_chars[-1].strip()
            if last_row in ['*', '+']:
                operator = last_row

            numbers = []
            num_rows = len(problem_chars) - 1

            for c in range(problem_width - 1, -1, -1):
                digits = []
                for row in range(num_rows):
                    char = problem_chars[row][c] if c < len(problem_chars[row]) else ' '
                    if char.isdigit():
                        digits.append(char)

                if digits:
                    number = int(''.join(digits))
                    numbers.append(number)

            if numbers and operator:
                problems.append((numbers, operator))

            col += problem_width
        else:
            col += 1

    answers = []
    for numbers, operator in problems:
        if operator == '*':
            result = 1
            for num in numbers:
                result *= num
        else:
            result = sum(numbers)
        answers.append(result)

    grand_total = sum(answers)
    print(grand_total)
    AOC.submit_answer(grand_total)

if __name__ == "__main__":
    solve()
