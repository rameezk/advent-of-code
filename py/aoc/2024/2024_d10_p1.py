from aoc.helper import AOC
from aoc.util import adj


@AOC.puzzle(year=2024, day=10, part=1)
def solve():
    data = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732"""
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
        score = get_score(t_map, [possible_trailhead])
        result += score

    print(result)
    AOC.submit_answer(result)


def get_score(t_map, positions, seen=None):
    if seen is None:
        seen = set()

    score = 0
    n_positions = []

    for pos in positions:

        if pos in seen:
            continue

        seen.add(pos)

        r, c = pos
        h = t_map[r][c]

        if h == 9:
            score += 1

        for n_pos in adj(pos):
            n_r, n_c = n_pos

            if n_r < 0 or n_r >= len(t_map) or n_c < 0 or n_c >= len(t_map[0]):
                continue

            n_h = t_map[n_r][n_c]
            if n_h == h + 1:
                n_positions.append(n_pos)

    if n_positions:
        return score + get_score(t_map, n_positions, seen)

    return score


if __name__ == "__main__":
    solve()
