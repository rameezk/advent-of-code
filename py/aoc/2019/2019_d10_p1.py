from aoc.helper import AOC
from math import gcd


@AOC.puzzle(2019, 10, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

    asteroids = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '#':
                asteroids.append((x, y))

    max_visible = 0
    best_location = None

    for base in asteroids:
        directions = set()
        for target in asteroids:
            if base == target:
                continue
            dx = target[0] - base[0]
            dy = target[1] - base[1]
            g = gcd(abs(dx), abs(dy))
            direction = (dx // g, dy // g)
            directions.add(direction)

        visible = len(directions)
        if visible > max_visible:
            max_visible = visible
            best_location = base

    answer = max_visible
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
