from aoc.helper import AOC
import sys
sys.setrecursionlimit(100000)


@AOC.puzzle(2018, 17, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """x=495, y=2..7
# y=7, x=495..501
# x=501, y=3..7
# x=498, y=2..4
# x=506, y=1..2
# x=498, y=10..13
# x=504, y=10..13
# y=13, x=498..504""".strip().splitlines()

    clay = set()

    for line in data:
        parts = line.split(', ')
        if parts[0].startswith('x='):
            x_val = int(parts[0][2:])
            y_range = parts[1][2:].split('..')
            if len(y_range) == 2:
                for y in range(int(y_range[0]), int(y_range[1]) + 1):
                    clay.add((x_val, y))
            else:
                clay.add((x_val, int(y_range[0])))
        else:
            y_val = int(parts[0][2:])
            x_range = parts[1][2:].split('..')
            if len(x_range) == 2:
                for x in range(int(x_range[0]), int(x_range[1]) + 1):
                    clay.add((x, y_val))
            else:
                clay.add((int(x_range[0]), y_val))

    min_y = min(y for x, y in clay)
    max_y = max(y for x, y in clay)

    flowing = set()
    settled = set()

    def flow(x, y):
        if y > max_y:
            return False

        if (x, y) in flowing or (x, y) in settled:
            return (x, y) in settled

        flowing.add((x, y))

        below = (x, y + 1)
        if below not in clay and below not in settled:
            flow(x, y + 1)

        if below in clay or below in settled:
            left_blocked = fill_horizontal(x, y, -1)
            right_blocked = fill_horizontal(x, y, 1)

            if left_blocked and right_blocked:
                left_x = x
                while (left_x, y) not in clay:
                    settled.add((left_x, y))
                    if (left_x, y) in flowing:
                        flowing.remove((left_x, y))
                    left_x -= 1

                right_x = x
                while (right_x, y) not in clay:
                    settled.add((right_x, y))
                    if (right_x, y) in flowing:
                        flowing.remove((right_x, y))
                    right_x += 1

                return True

        return False

    def fill_horizontal(x, y, dx):
        x += dx
        while (x, y) not in clay:
            flowing.add((x, y))
            below = (x, y + 1)
            if below not in clay and below not in settled:
                flow(x, y + 1)
            if below not in clay and below not in settled:
                return False
            x += dx
        return True

    flow(500, 0)

    water_tiles = set()
    for pos in flowing | settled:
        if min_y <= pos[1] <= max_y:
            water_tiles.add(pos)

    result = len(water_tiles)
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
