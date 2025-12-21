from aoc.helper import AOC


@AOC.puzzle(2024, 14, 1)
def solve():
    data = AOC.get_data()

#     data = """p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3"""

    width = 101
    height = 103

    robots = []
    for line in data.strip().splitlines():
        parts = line.split()
        pos = parts[0].split("=")[1].split(",")
        vel = parts[1].split("=")[1].split(",")
        px, py = int(pos[0]), int(pos[1])
        vx, vy = int(vel[0]), int(vel[1])
        robots.append((px, py, vx, vy))

    seconds = 100
    final_positions = []

    for px, py, vx, vy in robots:
        final_x = (px + vx * seconds) % width
        final_y = (py + vy * seconds) % height
        final_positions.append((final_x, final_y))

    mid_x = width // 2
    mid_y = height // 2

    quadrants = [0, 0, 0, 0]

    for x, y in final_positions:
        if x == mid_x or y == mid_y:
            continue

        if x < mid_x and y < mid_y:
            quadrants[0] += 1
        elif x > mid_x and y < mid_y:
            quadrants[1] += 1
        elif x < mid_x and y > mid_y:
            quadrants[2] += 1
        else:
            quadrants[3] += 1

    safety_factor = quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3]

    print(f"Quadrants: {quadrants}")
    print(f"Safety factor: {safety_factor}")
    AOC.submit_answer(safety_factor)


if __name__ == "__main__":
    solve()
