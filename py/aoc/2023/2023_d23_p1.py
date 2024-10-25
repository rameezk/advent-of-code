from aoc.helper import download_input, submit_answer
from aoc.util import benchmark


@benchmark
def run():
    download_input(2023, 23)

    hiking_trail_map = """
#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
    """.strip().splitlines()

    with open("./2023_d23.txt") as f:
        hiking_trail_map = f.read().strip().splitlines()

    start = (
        0,
        [i for i, c in enumerate(hiking_trail_map[0]) if c == "."][0],
    )
    target = (
        len(hiking_trail_map) - 1,
        [i for i, c in enumerate(hiking_trail_map[-1]) if c == "."][0],
    )

    ps = [[start, 0, {start}]]
    tm = []
    while True:
        if not ps:
            break
        np = []
        for cp, s, visited in ps:
            visited = visited.copy()

            if cp == target:
                tm.append(s)
                continue

            r, c = cp

            w = hiking_trail_map[r][c]

            if w == "#":
                raise RuntimeError("Something went wrong")

            if w == ".":
                np.extend(
                    move(
                        hiking_trail_map,
                        visited,
                        s,
                        [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)],
                    )
                )
            elif w == "^":
                np.extend(move(hiking_trail_map, visited, s, [(r - 1, c)]))
            elif w == "v":
                np.extend(move(hiking_trail_map, visited, s, [(r + 1, c)]))
            elif w == ">":
                np.extend(move(hiking_trail_map, visited, s, [(r, c + 1)]))
            elif w == "<":
                np.extend(move(hiking_trail_map, visited, s, [(r, c - 1)]))
            else:
                raise RuntimeError("Unrecognized direction")

            # if len(np) == 0:
            #     raise RuntimeError("empty")

        ps = np
        # print([p[1] for p in ps])
        # _ = input("c?")

    M = max(tm)
    submit_answer(2023, 23, 1, M)


def move(hiking_trail_map, visited, s, moves):
    np = []
    for nr, nc in moves:
        if (
            (nr, nc) in visited
            or nr < 0
            or nr >= len(hiking_trail_map)
            or nc < 0
            or nc >= len(hiking_trail_map[0])
        ):
            continue

        if hiking_trail_map[nr][nc] == "#":
            continue

        ns = s + 1
        visited.add((nr, nc))
        np.append([(nr, nc), ns, visited])
    return np


if __name__ == "__main__":
    run()
