from aoc.helper import AOC


@AOC.puzzle(2024, 15, 2)
def solve():
    data = AOC.get_data().strip()

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

#     data = """#######
# #...#.#
# #.....#
# #..OO@#
# #..O..#
# #.....#
# #######
#
# <vv<<^^<<^^"""

    parts = data.split('\n\n')
    grid_lines = parts[0].splitlines()
    moves = parts[1].replace('\n', '')

    expanded = []
    for line in grid_lines:
        new_line = ""
        for char in line:
            if char == '#':
                new_line += '##'
            elif char == 'O':
                new_line += '[]'
            elif char == '.':
                new_line += '..'
            elif char == '@':
                new_line += '@.'
        expanded.append(new_line)

    grid = {}
    robot_pos = None
    for r, line in enumerate(expanded):
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

    def can_move_vertical(positions, dr):
        next_positions = set()
        for r, c in positions:
            nr = r + dr
            if grid.get((nr, c)) == '#':
                return False, set()
            if grid.get((nr, c)) == '[':
                next_positions.add((nr, c))
                next_positions.add((nr, c + 1))
            elif grid.get((nr, c)) == ']':
                next_positions.add((nr, c))
                next_positions.add((nr, c - 1))

        if not next_positions:
            return True, set()

        can_move, further = can_move_vertical(next_positions, dr)
        if can_move:
            return True, next_positions | further
        return False, set()

    for move in moves:
        dr, dc = directions[move]
        nr, nc = robot_pos[0] + dr, robot_pos[1] + dc

        if grid.get((nr, nc)) == '#':
            continue

        if grid.get((nr, nc)) == '.':
            robot_pos = (nr, nc)
            continue

        if move in '<>':
            boxes_to_move = []
            check_r, check_c = nr, nc
            while grid.get((check_r, check_c)) in '[]':
                boxes_to_move.append((check_r, check_c))
                check_c = check_c + dc

            if grid.get((check_r, check_c)) == '.':
                for box_r, box_c in reversed(boxes_to_move):
                    grid[(box_r, box_c + dc)] = grid[(box_r, box_c)]
                    grid[(box_r, box_c)] = '.'
                robot_pos = (nr, nc)

        else:
            initial_box_positions = set()
            if grid.get((nr, nc)) == '[':
                initial_box_positions.add((nr, nc))
                initial_box_positions.add((nr, nc + 1))
            elif grid.get((nr, nc)) == ']':
                initial_box_positions.add((nr, nc))
                initial_box_positions.add((nr, nc - 1))

            can_move, all_boxes = can_move_vertical(initial_box_positions, dr)
            if can_move:
                all_to_move = initial_box_positions | all_boxes
                sorted_boxes = sorted(all_to_move, key=lambda p: p[0], reverse=(dr > 0))

                for box_r, box_c in sorted_boxes:
                    grid[(box_r + dr, box_c)] = grid[(box_r, box_c)]
                    grid[(box_r, box_c)] = '.'

                robot_pos = (nr, nc)

    total = 0
    for (r, c), char in grid.items():
        if char == '[':
            gps = 100 * r + c
            total += gps

    print(total)
    AOC.submit_answer(total)


if __name__ == "__main__":
    solve()
