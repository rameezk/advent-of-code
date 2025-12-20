from aoc.helper import AOC

@AOC.puzzle(2021, 13, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0
#
# fold along y=7
# fold along x=5"""

    lines = data.strip().split('\n')

    dots = set()
    folds = []

    parsing_dots = True
    for line in lines:
        if line == '':
            parsing_dots = False
            continue

        if parsing_dots:
            x, y = map(int, line.split(','))
            dots.add((x, y))
        else:
            parts = line.split()
            axis_val = parts[2].split('=')
            axis = axis_val[0]
            val = int(axis_val[1])
            folds.append((axis, val))

    axis, fold_line = folds[0]

    new_dots = set()

    if axis == 'y':
        for x, y in dots:
            if y < fold_line:
                new_dots.add((x, y))
            else:
                new_y = fold_line - (y - fold_line)
                new_dots.add((x, new_y))
    else:
        for x, y in dots:
            if x < fold_line:
                new_dots.add((x, y))
            else:
                new_x = fold_line - (x - fold_line)
                new_dots.add((new_x, y))

    answer = len(new_dots)

    print(f"Part 1: {answer}")

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
