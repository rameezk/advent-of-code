from aoc.helper import AOC
from aoc.util import adj


@AOC.puzzle(year=2024, day=10, part=2)
def solve():
    data = """..90..9
...1.98
...2..7
6543456
765.987
876....
987...."""
    data = AOC.get_data()
    t_map = []
    for row in data.strip().splitlines():
        t_map.append([-1 if col == "." else int(col) for col in row])

    possible_trailheads = []
    for r, row in enumerate(t_map):
        for c, height in enumerate(row):
            if height == 0:
                possible_trailheads.append((r, c))

    result = 0
    for possible_trailhead in possible_trailheads:
        rating = get_rating(t_map, [possible_trailhead])
        result += rating

    print(result)
    AOC.submit_answer(result)


def get_rating(t_map, positions, seen=None):
    if seen is None:
        seen = set()

    rating = 0

    for pos in positions:

        seen.add(pos)

        r, c = pos
        h = t_map[r][c]

        if h == 9:
            rating += 1
            continue

        for n_pos in adj(pos):
            n_r, n_c = n_pos

            if n_r < 0 or n_r >= len(t_map) or n_c < 0 or n_c >= len(t_map[0]):
                continue

            n_h = t_map[n_r][n_c]
            if n_h == h + 1:
                rating += get_rating(t_map, [n_pos], seen)

    return rating


if __name__ == "__main__":
    solve()
