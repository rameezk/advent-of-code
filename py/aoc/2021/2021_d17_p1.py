from aoc.helper import AOC

@AOC.puzzle(2021, 17, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """target area: x=20..30, y=-10..-5"""

    parts = data.split(": ")[1].split(", ")
    x_range = parts[0][2:].split("..")
    y_range = parts[1][2:].split("..")

    x_min, x_max = int(x_range[0]), int(x_range[1])
    y_min, y_max = int(y_range[0]), int(y_range[1])

    def simulate(vx, vy):
        x, y = 0, 0
        max_y = 0
        while True:
            x += vx
            y += vy
            max_y = max(max_y, y)

            if vx > 0:
                vx -= 1
            elif vx < 0:
                vx += 1

            vy -= 1

            if x_min <= x <= x_max and y_min <= y <= y_max:
                return True, max_y

            if x > x_max or y < y_min:
                return False, max_y

    best_max_y = 0

    for initial_vx in range(1, x_max + 1):
        for initial_vy in range(y_min, 200):
            hit, max_y = simulate(initial_vx, initial_vy)
            if hit:
                best_max_y = max(best_max_y, max_y)

    answer = best_max_y

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
