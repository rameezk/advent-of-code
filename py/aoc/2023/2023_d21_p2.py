from aoc.helper import download_input, submit_answer
from aoc.util import benchmark

from functools import cache


@cache
def get_next_tiles(garden_map, tiles, tiles_visited_count):
    l_r = len(garden_map)
    l_c = len(garden_map[0])

    next = []
    visited = set()
    tiles_visited_count = 0

    for n in tiles:
        r, c = n
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = r + dr
            nc = c + dc

            if (nr, nc) in visited:
                continue

            # if nr >= len(garden_map) or nc >= len(garden_map[0]) or nr < 0 or nc < 0:
            #     print("here")
            #     nr_d, _ = divmod(nr, l_r)
            #     nc_d, _ = divmod(nc, l_c)
            #
            #     if nr_d != 0 or nc_d != 0:
            #         tiles_visited_count += 1
            #         nr = nr % l_r
            #         nc = nc % l_c

            if garden_map[nr % l_r][nc % l_c] == "#":
                continue

            visited.add((nr, nc))
            next.append((nr, nc))
            tiles_visited_count += 1

    tiles = next
    return tiles_visited_count, tuple(tiles)


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

    # with open("./2023_d21.txt") as f:
    #     garden_map = f.read().strip().splitlines()

    garden_map = tuple(garden_map)

    start = None
    for r, row in enumerate(garden_map):
        for c, char in enumerate(row):
            if char == "S":
                start = (r, c)
                break

    # steps_left = 26501365
    steps_left = 1000
    tiles = (start,)
    tiles_visited_count = 0
    for i in range(steps_left, 0, -1):
        if i % 100 == 0:
            print("steps left", i)
        tiles_visited_count, tiles = get_next_tiles(
            garden_map, tiles, tiles_visited_count
        )

    print(tiles_visited_count)
    # submit_answer(2023, 21, 2, L)


if __name__ == "__main__":
    run()
