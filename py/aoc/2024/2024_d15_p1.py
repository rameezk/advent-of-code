from aoc.helper import AOC


@AOC.puzzle(2024, 15, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """########
# #..O.O.#
# ##@.O..#
# #...O..#
# #.#.O..#
# #...O..#
# #......#
# ########
#
# <^^>>>vv<v>>v<<"""

#     data = """##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########
#
# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<^<v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv<>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

    parts = data.split('\n\n')
    grid_lines = parts[0].splitlines()
    moves = parts[1].replace('\n', '')

    grid = {}
    robot_pos = None
    for r, line in enumerate(grid_lines):
        for c, char in enumerate(line):
            grid[(r, c)] = char
            if char == '@':
                robot_pos = (r, c)
                grid[(r, c)] = '.'

    directions = {
        '^': (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    for move in moves:
        dr, dc = directions[move]
        nr, nc = robot_pos[0] + dr, robot_pos[1] + dc

        if grid.get((nr, nc)) == '#':
            continue

        if grid.get((nr, nc)) == '.':
            robot_pos = (nr, nc)
            continue

        if grid.get((nr, nc)) == 'O':
            boxes_to_move = []
            check_r, check_c = nr, nc
            while grid.get((check_r, check_c)) == 'O':
                boxes_to_move.append((check_r, check_c))
                check_r, check_c = check_r + dr, check_c + dc

            if grid.get((check_r, check_c)) == '.':
                for box_r, box_c in reversed(boxes_to_move):
                    grid[(box_r + dr, box_c + dc)] = 'O'
                    grid[(box_r, box_c)] = '.'
                robot_pos = (nr, nc)

    total = 0
    for (r, c), char in grid.items():
        if char == 'O':
            gps = 100 * r + c
            total += gps

    print(total)
    AOC.submit_answer(total)


if __name__ == "__main__":
    solve()
