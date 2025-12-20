from aoc.helper import AOC
from math import gcd, atan2, pi, sqrt
from collections import defaultdict


@AOC.puzzle(2019, 10, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

    asteroids = []
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char == '#':
                asteroids.append((x, y))

    max_visible = 0
    station = None

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
            station = base

    asteroids_by_angle = defaultdict(list)

    for asteroid in asteroids:
        if asteroid == station:
            continue

        dx = asteroid[0] - station[0]
        dy = asteroid[1] - station[1]

        angle = atan2(dx, -dy)
        if angle < 0:
            angle += 2 * pi

        distance = sqrt(dx*dx + dy*dy)
        asteroids_by_angle[angle].append((distance, asteroid))

    for angle in asteroids_by_angle:
        asteroids_by_angle[angle].sort()

    angles = sorted(asteroids_by_angle.keys())

    vaporized = []
    while len(vaporized) < 200:
        for angle in angles:
            if asteroids_by_angle[angle]:
                dist, asteroid = asteroids_by_angle[angle].pop(0)
                vaporized.append(asteroid)
                if len(vaporized) == 200:
                    break

    target = vaporized[199]
    answer = target[0] * 100 + target[1]
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
