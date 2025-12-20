from aoc.helper import AOC
import re


@AOC.puzzle(2018, 10, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """position=< 9,  1> velocity=< 0,  2>
# position=< 7,  0> velocity=<-1,  0>
# position=< 3, -2> velocity=<-1,  1>
# position=< 6, 10> velocity=<-2, -1>
# position=< 2, -4> velocity=< 2,  2>
# position=<-6, 10> velocity=< 2, -2>
# position=< 1,  8> velocity=< 1, -1>
# position=< 1,  7> velocity=< 1,  0>
# position=<-3, 11> velocity=< 1, -2>
# position=< 7,  6> velocity=<-1, -1>
# position=<-2,  3> velocity=< 1,  0>
# position=<-4,  3> velocity=< 2,  0>
# position=<10, -3> velocity=<-1,  1>
# position=< 5, 11> velocity=< 1, -2>
# position=< 4,  7> velocity=< 0, -1>
# position=< 8, -2> velocity=< 0,  1>
# position=<15,  0> velocity=<-2,  0>
# position=< 1,  6> velocity=< 1,  0>
# position=< 8,  9> velocity=< 0, -1>
# position=< 3,  3> velocity=<-1,  1>
# position=< 0,  5> velocity=< 0, -1>
# position=<-2,  2> velocity=< 2,  0>
# position=< 5, -2> velocity=< 1,  2>
# position=< 1,  4> velocity=< 2,  1>
# position=<-2,  7> velocity=< 2, -2>
# position=< 3,  6> velocity=<-1, -1>
# position=< 5,  0> velocity=< 1,  0>
# position=<-6,  0> velocity=< 2,  0>
# position=< 5,  9> velocity=< 1, -2>
# position=<14,  7> velocity=<-2,  0>
# position=<-3,  6> velocity=< 2, -1>""".splitlines()

    points = []
    for line in data:
        match = re.findall(r'-?\d+', line)
        px, py, vx, vy = map(int, match)
        points.append([px, py, vx, vy])

    def get_bounds(pts):
        min_x = min(p[0] for p in pts)
        max_x = max(p[0] for p in pts)
        min_y = min(p[1] for p in pts)
        max_y = max(p[1] for p in pts)
        return min_x, max_x, min_y, max_y

    def area(pts):
        min_x, max_x, min_y, max_y = get_bounds(pts)
        return (max_x - min_x) * (max_y - min_y)

    def step_forward(pts):
        for p in pts:
            p[0] += p[2]
            p[1] += p[3]

    def step_backward(pts):
        for p in pts:
            p[0] -= p[2]
            p[1] -= p[3]

    prev_area = area(points)
    while True:
        step_forward(points)
        curr_area = area(points)
        if curr_area > prev_area:
            step_backward(points)
            break
        prev_area = curr_area

    min_x, max_x, min_y, max_y = get_bounds(points)

    grid = set()
    for p in points:
        grid.add((p[0], p[1]))

    print()
    for y in range(min_y, max_y + 1):
        line = ""
        for x in range(min_x, max_x + 1):
            if (x, y) in grid:
                line += "#"
            else:
                line += "."
        print(line)
    print()


if __name__ == "__main__":
    solve()
