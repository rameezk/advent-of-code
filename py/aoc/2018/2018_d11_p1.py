from aoc.helper import AOC


@AOC.puzzle(2018, 11, 1)
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

    max_power = float('-inf')
    best_coord = None

    for x in range(1, 299):
        for y in range(1, 299):
            total = 0
            for dx in range(3):
                for dy in range(3):
                    total += grid[(x + dx, y + dy)]

            if total > max_power:
                max_power = total
                best_coord = (x, y)

    result = f"{best_coord[0]},{best_coord[1]}"
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
