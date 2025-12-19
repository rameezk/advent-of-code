from aoc.helper import AOC

@AOC.puzzle(2017, 19, 1)
def solve():
    data = AOC.get_data().strip('\n')
    # data = """     |
    #      |  +--+
    #      A  |  C
    #  F---|----E|--+
    #      |  |  |  D
    #      +B-+  +--+
    # """

    lines = data.split('\n')
    if lines[0] == '':
        lines = lines[1:]
    if lines[-1] == '':
        lines = lines[:-1]

    grid = [list(line) for line in lines]

    max_width = max(len(line) for line in grid)
    for i in range(len(grid)):
        grid[i] += [' '] * (max_width - len(grid[i]))

    start_col = None
    for col in range(len(grid[0])):
        if grid[0][col] == '|':
            start_col = col
            break

    row, col = 0, start_col
    direction = (1, 0)
    letters = []

    while True:
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            break

        current = grid[row][col]

        if current.isalpha():
            letters.append(current)
        elif current == ' ':
            break
        elif current == '+':
            dr, dc = direction

            for new_dr, new_dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if (new_dr, new_dc) == (-dr, -dc):
                    continue
                if (new_dr, new_dc) == (dr, dc):
                    continue

                new_row = row + new_dr
                new_col = col + new_dc

                if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
                    if grid[new_row][new_col] != ' ':
                        direction = (new_dr, new_dc)
                        break

        row += direction[0]
        col += direction[1]

    answer = ''.join(letters)
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
