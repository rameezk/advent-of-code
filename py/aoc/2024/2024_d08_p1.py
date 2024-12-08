from collections import defaultdict
from itertools import permutations

from aoc.helper import AOC


@AOC.puzzle(year=2024, day=8, part=1)
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
        for (p1_r, p1_c), (p2_r, p2_c) in pairs:
            distance_r = p2_r - p1_r
            distance_c = p2_c - p1_c

            antinode1_r = p1_r - distance_r
            antinode1_c = p1_c - distance_c
            if not (
                antinode1_r < 0
                or antinode1_r > max_r
                or antinode1_c < 0
                or antinode1_c > max_c
            ):
                unique_antinodes.add((antinode1_r, antinode1_c))

            antinode2_r = p2_r + distance_r
            antinode2_c = p2_c + distance_c
            if not (
                antinode2_r < 0
                or antinode2_r > max_r
                or antinode2_c < 0
                or antinode2_c > max_c
            ):
                unique_antinodes.add((antinode2_r, antinode2_c))

    unique_locations = len(unique_antinodes)
    print(unique_locations)
    AOC.submit_answer(unique_locations)


if __name__ == "__main__":
    solve()
