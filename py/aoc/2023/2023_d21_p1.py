from aoc.helper import download_input, submit_answer
from aoc.util import benchmark


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

    start = None
    for r, row in enumerate(garden_map):
        for c, char in enumerate(row):
            if char == "S":
                start = (r, c)
                break

    steps_left = 64
    tiles = [start]
    for _ in range(steps_left, 0, -1):
        next = []
        visited = set()
        for n in tiles:
            r, c = n
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = r + dr
                nc = c + dc

                if (nr, nc) in visited:
                    continue

                if nr >= len(garden_map) or nc >= len(garden_map[0]):
                    continue

                if nr < 0 or nc < 0:
                    continue

                if garden_map[nr][nc] == "#":
                    continue

                visited.add((nr, nc))
                next.append((nr, nc))

        tiles = next

    L = len(tiles)
    print(L)
    submit_answer(2023, 21, 1, L)


if __name__ == "__main__":
    run()
