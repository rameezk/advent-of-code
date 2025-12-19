from aoc.helper import AOC


@AOC.puzzle(2015, 25, 1)
def solve():
    data = AOC.get_data().strip()

    import re
    match = re.search(r'row (\d+), column (\d+)', data)
    target_row = int(match.group(1))
    target_col = int(match.group(2))

    def get_code_index(row, col):
        diagonal = row + col - 1
        codes_before_diagonal = (diagonal - 1) * diagonal // 2
        position_in_diagonal = col
        return codes_before_diagonal + position_in_diagonal

    target_index = get_code_index(target_row, target_col)

    code = 20151125
    for _ in range(target_index - 1):
        code = (code * 252533) % 33554393

    result = code
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
