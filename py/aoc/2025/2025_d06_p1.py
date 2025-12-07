from aoc.helper import AOC


@AOC.puzzle(2025, 6, 1)
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

            problem_lines = []
            for row in range(len(padded_lines)):
                problem_lines.append(padded_lines[row][col:col+problem_width].strip())

            numbers = []
            operator = None
            for line in problem_lines:
                if line and line in ['*', '+']:
                    operator = line
                elif line and line.isdigit():
                    numbers.append(int(line))

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
