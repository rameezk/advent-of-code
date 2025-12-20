from aoc.helper import AOC


@AOC.puzzle(2018, 11, 2)
def solve():
    serial_number = int(AOC.get_data().strip())

    # serial_number = 18
    # serial_number = 42

    def power_level(x, y, serial):
        rack_id = x + 10
        power = rack_id * y
        power += serial
        power *= rack_id
        power = (power // 100) % 10
        power -= 5
        return power

    grid = {}
    for x in range(1, 301):
        for y in range(1, 301):
            grid[(x, y)] = power_level(x, y, serial_number)

    sat = {}
    for x in range(1, 301):
        for y in range(1, 301):
            value = grid[(x, y)]
            left = sat.get((x - 1, y), 0)
            top = sat.get((x, y - 1), 0)
            top_left = sat.get((x - 1, y - 1), 0)
            sat[(x, y)] = value + left + top - top_left

    def get_square_sum(x, y, size):
        if x + size - 1 > 300 or y + size - 1 > 300:
            return float('-inf')

        x2, y2 = x + size - 1, y + size - 1
        total = sat[(x2, y2)]

        if x > 1:
            total -= sat[(x - 1, y2)]
        if y > 1:
            total -= sat[(x2, y - 1)]
        if x > 1 and y > 1:
            total += sat[(x - 1, y - 1)]

        return total

    max_power = float('-inf')
    best_result = None

    for size in range(1, 301):
        for x in range(1, 302 - size):
            for y in range(1, 302 - size):
                power = get_square_sum(x, y, size)
                if power > max_power:
                    max_power = power
                    best_result = (x, y, size)

    result = f"{best_result[0]},{best_result[1]},{best_result[2]}"
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
