from aoc.helper import AOC


def adjacent_matches(row, col, data):
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1)]

    matches = 0
    max_rows, max_cols = len(data), len(data[0])

    for delta_row, delta_col in directions:
        word = ""
        current_row = row
        current_col = col

        for _ in range(4):
            if not (0 <= current_row < max_rows and 0 <= current_col < max_cols):
                break

            word += data[current_row][current_col]
            current_row += delta_row
            current_col += delta_col

        if word == "XMAS":
            matches += 1

    return matches


@AOC.puzzle(year=2024, day=4, part=1)
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
            if char == "X":
                count += adjacent_matches(row, col, data)

    print(count)
    AOC.submit_answer(count)


if __name__ == "__main__":
    solve()
