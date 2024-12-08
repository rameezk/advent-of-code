from collections import defaultdict
from itertools import permutations

from aoc.helper import AOC


@AOC.puzzle(year=2024, day=8, part=2)
def solve():
    data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............"""
    data = AOC.get_data()

    data = data.strip().splitlines()
    max_r, max_c = len(data) - 1, len(data[0]) - 1

    antenna_positions = defaultdict(list)
    for row_i, row in enumerate(data):
        for col_i, col in enumerate(row):
            if col != ".":
                antenna_positions[col].append((row_i, col_i))

    unique_antinodes = set()
    for _, positions in antenna_positions.items():
        pairs = list(permutations(positions, 2))
        for p1, p2 in pairs:
            line_points = get_line_points(p1, p2, max_r, max_c)
            unique_antinodes.update(line_points)

    unique_locations = len(unique_antinodes)
    print(unique_locations)
    AOC.submit_answer(unique_locations)


def get_line_points(p1, p2, max_r, max_c):
    points = set()

    p1_r, p1_c = p1
    p2_r, p2_c = p2

    distance_r = p2_r - p1_r
    distance_c = p2_c - p1_c

    for r in range(max_r + 1):
        c = p1_c + (distance_c / distance_r) * (r - p1_r)
        if c.is_integer() and 0 <= c <= max_c:
            points.add((r, c))

    for c in range(max_c + 1):
        r = p1_r + (distance_r / distance_c) * (c - p1_c)
        if r.is_integer() and 0 <= r <= max_r:
            points.add((r, c))

    return points


if __name__ == "__main__":
    solve()
