from aoc.helper import AOC


@AOC.puzzle(2022, 22, 1)
def solve():
    data = AOC.get_data()

#     data = """        ...#
#         .#..
#         #...
#         ....
# ...#.......#
# ........#...
# ..#....#....
# ..........#.
#         ...#....
#         .....#..
#         .#......
#         ......#.
#
# 10R5L5R10L4R5L5"""

    parts = data.split('\n\n')
    board_lines = parts[0].split('\n')
    path = parts[1].strip()

    max_width = max(len(line) for line in board_lines)
    board = []
    for line in board_lines:
        board.append(line.ljust(max_width))

    instructions = []
    i = 0
    while i < len(path):
        if path[i].isdigit():
            j = i
            while j < len(path) and path[j].isdigit():
                j += 1
            instructions.append(int(path[i:j]))
            i = j
        else:
            instructions.append(path[i])
            i += 1

    start_col = 0
    for col in range(len(board[0])):
        if board[0][col] == '.':
            start_col = col
            break

    row, col = 0, start_col
    facing = 0

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for instruction in instructions:
        if isinstance(instruction, str):
            if instruction == 'R':
                facing = (facing + 1) % 4
            else:
                facing = (facing - 1) % 4
        else:
            for _ in range(instruction):
                next_row = row + dr[facing]
                next_col = col + dc[facing]

                if (0 <= next_row < len(board) and
                    0 <= next_col < len(board[next_row]) and
                    board[next_row][next_col] != ' '):
                    if board[next_row][next_col] == '#':
                        break
                    row, col = next_row, next_col
                else:
                    wrap_row, wrap_col = row, col
                    if facing == 0:
                        for c in range(len(board[row])):
                            if board[row][c] != ' ':
                                wrap_col = c
                                break
                    elif facing == 2:
                        for c in range(len(board[row]) - 1, -1, -1):
                            if board[row][c] != ' ':
                                wrap_col = c
                                break
                    elif facing == 1:
                        for r in range(len(board)):
                            if col < len(board[r]) and board[r][col] != ' ':
                                wrap_row = r
                                break
                    else:
                        for r in range(len(board) - 1, -1, -1):
                            if col < len(board[r]) and board[r][col] != ' ':
                                wrap_row = r
                                break

                    if board[wrap_row][wrap_col] == '#':
                        break
                    row, col = wrap_row, wrap_col

    password = 1000 * (row + 1) + 4 * (col + 1) + facing
    print(f"Final position: row={row+1}, col={col+1}, facing={facing}")
    print(f"Password: {password}")
    AOC.submit_answer(password)


if __name__ == "__main__":
    solve()
