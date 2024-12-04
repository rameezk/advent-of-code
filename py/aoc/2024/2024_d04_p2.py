from aoc.helper import AOC


def is_x(row: int, col: int, data: list[str]) -> bool:
    if 0 < row < len(data) - 1 and 0 < col < len(data[0]) - 1:

        top_left = data[row - 1][col - 1]
        bottom_right = data[row + 1][col + 1]
        top_right = data[row - 1][col + 1]
        bottom_left = data[row + 1][col - 1]

        return (
            (top_left == "M" and bottom_right == "S")
            or (top_left == "S" and bottom_right == "M")
        ) and (
            (top_right == "M" and bottom_left == "S")
            or (top_right == "S" and bottom_left == "M")
        )

    return False


@AOC.puzzle(year=2024, day=4, part=2)
def solve():
    data = AOC.get_data().strip().splitlines()
    #     data = """MMMSXXMASM
    # MSAMXMSMSA
    # AMXSXMAAMM
    # MSAMASMSMX
    # XMASAMXAMM
    # XXAMMXXAMA
    # SMSMSASXSS
    # SAXAMASAAA
    # MAMMMXMMMM
    # MXMXAXMASX""".strip().splitlines()

    count = 0
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if char == "A" and is_x(row, col, data):
                count += 1

    print(count)
    AOC.submit_answer(count)


if __name__ == "__main__":
    solve()
