from aoc.helper import AOC


@AOC.puzzle(2022, 22, 2)
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

    face_size = 4 if len(board) < 50 else 50

    def get_cube_wrap(r, c, f):
        if face_size == 4:
            fr = r // 4
            fc = c // 4
            lr = r % 4
            lc = c % 4

            edges = {}
            edges[(0, 2, 0)] = (11 - lr, 15, 2)
            edges[(0, 2, 1)] = (4 + lc, 11 - lr, 2)
            edges[(0, 2, 2)] = (4 + lr, 4 + lr, 1)
            edges[(0, 2, 3)] = (lr, 11 - lc, 1)

            edges[(1, 0, 0)] = (11 - lr, 15, 2)
            edges[(1, 0, 1)] = (11 - lc, 11 - lr, 3)
            edges[(1, 0, 2)] = (11, 15 - lr, 3)
            edges[(1, 0, 3)] = (0, 11 - lc, 1)

            edges[(1, 1, 0)] = (11 - lr, 15, 2)
            edges[(1, 1, 1)] = (11 - lc, 8, 0)
            edges[(1, 1, 2)] = (11, 15 - lr, 3)
            edges[(1, 1, 3)] = (0, 8 + lc, 1)

            edges[(1, 2, 0)] = (8 + (3 - lr), 15, 2)
            edges[(1, 2, 1)] = (11 - lc, 8 + (3 - lr), 2)
            edges[(1, 2, 2)] = (11, 15 - lr, 3)
            edges[(1, 2, 3)] = (0, 8 + lc, 1)

            edges[(2, 2, 0)] = (3 - lr, 11, 2)
            edges[(2, 2, 1)] = (7, 3 - lc, 3)
            edges[(2, 2, 2)] = (7 - lr, 7 - lr, 3)
            edges[(2, 2, 3)] = (7, 11 - lc, 2)

            edges[(2, 3, 0)] = (11 - lr, 11, 2)
            edges[(2, 3, 1)] = (7 - lc, 0, 0)
            edges[(2, 3, 2)] = (7 - lr, 7 - lr, 3)
            edges[(2, 3, 3)] = (7 - lc, 11, 2)

            key = (fr, fc, f)
            if key in edges:
                return edges[key]
        else:
            face_row = r // 50
            face_col = c // 50
            local_r = r % 50
            local_c = c % 50

            if face_row == 0 and face_col == 1:
                if f == 3:
                    return 150 + local_c, 0, 0
                elif f == 2:
                    return 149 - local_r, 0, 0
            elif face_row == 0 and face_col == 2:
                if f == 0:
                    return 149 - local_r, 99, 2
                elif f == 1:
                    return 50 + local_c, 99, 2
                elif f == 3:
                    return 199, local_c, 3
            elif face_row == 1 and face_col == 1:
                if f == 0:
                    return 49, 100 + local_r, 3
                elif f == 2:
                    return 100, local_r, 1
            elif face_row == 2 and face_col == 0:
                if f == 3:
                    return 50 + local_c, 50, 0
                elif f == 2:
                    return 49 - local_r, 50, 0
            elif face_row == 2 and face_col == 1:
                if f == 0:
                    return 49 - local_r, 149, 2
                elif f == 1:
                    return 150 + local_c, 49, 2
            elif face_row == 3 and face_col == 0:
                if f == 0:
                    return 149, 50 + local_r, 3
                elif f == 1:
                    return 0, 100 + local_c, 1
                elif f == 2:
                    return 0, 50 + local_r, 1

        return None, None, None

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
                next_facing = facing

                if (0 <= next_row < len(board) and
                    0 <= next_col < len(board[next_row]) and
                    board[next_row][next_col] != ' '):
                    if board[next_row][next_col] == '#':
                        break
                    row, col, facing = next_row, next_col, next_facing
                else:
                    wrap_row, wrap_col, wrap_facing = get_cube_wrap(row, col, facing)
                    if wrap_row is not None and board[wrap_row][wrap_col] == '#':
                        break
                    if wrap_row is not None:
                        row, col, facing = wrap_row, wrap_col, wrap_facing

    password = 1000 * (row + 1) + 4 * (col + 1) + facing
    print(f"Final position: row={row+1}, col={col+1}, facing={facing}")
    print(f"Password: {password}")
    AOC.submit_answer(password)


if __name__ == "__main__":
    solve()
