from aoc.helper import download_input, submit_answer
from aoc.util import benchmark
from collections import deque


@benchmark
def run():
    download_input(2023, 21)

    garden_map = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
    """.strip().splitlines()

    with open("./2023_d21.txt") as f:
        garden_map = f.read().strip().splitlines()

    sr, sc = next(
        (r, c)
        for r, row in enumerate(garden_map)
        for c, ch in enumerate(row)
        if ch == "S"
    )

    assert len(garden_map) == len(garden_map[0])

    size = len(garden_map)
    steps = 26501365

    assert sr == sc == size // 2
    assert steps % size == size // 2

    def fill(sr, sc, ss):
        ans = set()
        seen = {(sr, sc)}
        q = deque([(sr, sc, ss)])

        while q:
            r, c, s = q.popleft()

            if s % 2 == 0:
                ans.add((r, c))
            if s == 0:
                continue

            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if (
                    nr < 0
                    or nr >= len(garden_map)
                    or nc < 0
                    or nc >= len(garden_map[0])
                    or garden_map[nr][nc] == "#"
                    or (nr, nc) in seen
                ):
                    continue
                seen.add((nr, nc))
                q.append((nr, nc, s - 1))

        return len(ans)

    garden_map_width = steps // size - 1

    odd = (garden_map_width // 2 * 2 + 1) ** 2
    even = ((garden_map_width + 1) // 2 * 2) ** 2

    odd_points = fill(sr, sc, size * 2 + 1)
    even_points = fill(sr, sc, size * 2)

    corner_t = fill(size - 1, sc, size - 1)
    corner_r = fill(sr, 0, size - 1)
    corner_b = fill(0, sc, size - 1)
    corner_l = fill(sr, size - 1, size - 1)

    small_tr = fill(size - 1, 0, size // 2 - 1)
    small_tl = fill(size - 1, size - 1, size // 2 - 1)
    small_br = fill(0, 0, size // 2 - 1)
    small_bl = fill(0, size - 1, size // 2 - 1)

    large_tr = fill(size - 1, 0, size * 3 // 2 - 1)
    large_tl = fill(size - 1, size - 1, size * 3 // 2 - 1)
    large_br = fill(0, 0, size * 3 // 2 - 1)
    large_bl = fill(0, size - 1, size * 3 // 2 - 1)

    print(
        odd * odd_points
        + even * even_points
        + corner_t
        + corner_r
        + corner_b
        + corner_l
        + (garden_map_width + 1) * (small_tr + small_tl + small_br + small_bl)
        + garden_map_width * (large_tr + large_tl + large_br + large_bl)
    )


if __name__ == "__main__":
    run()
