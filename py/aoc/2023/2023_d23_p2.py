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
            elif w in ".^v><":
                np.extend(
                    move_as_far_as_possible(
                        hiking_trail_map,
                        visited,
                        r,
                        c,
                        s,
                    )
                )
            else:
                raise RuntimeError("Unrecognized direction")

            # if len(np) == 0:
            #     raise RuntimeError("empty")

        ps = np
        print([p[1] for p in ps])
        # _ = input("c?")

    print(tm)
    M = max(tm)
    print(M)
    # submit_answer(2023, 23, 1, M)


def move_as_far_as_possible(hiking_trail_map, visited, r, c, s):
    np = []

    # down
    by = 0
    for i in range(r + 1, len(hiking_trail_map)):
        if (i, c) in visited or hiking_trail_map[i][c] == "#":
            break
        by += 1
        visited.add((i, c))

    if by != 0:
        np.append([(r + by, c), s + by, visited])

    # up
    by = 0
    for i in range(r - 1, -1, -1):
        if (i, c) in visited or hiking_trail_map[i][c] == "#":
            break
        by += 1
        visited.add((i, c))

    if by != 0:
        np.append([(r - by, c), s + by, visited])

    # right
    by = 0
    for i in range(c + 1, len(hiking_trail_map[0])):
        if (r, i) in visited or hiking_trail_map[r][i] == "#":
            break
        by += 1
        visited.add((r, i))

    if by != 0:
        np.append([(r, c + by), s + by, visited])

    # left
    by = 0
    for i in range(c - 1, -1, -1):
        if (r, i) in visited or hiking_trail_map[r][i] == "#":
            break
        by += 1
        visited.add((r, i))

    if by != 0:
        np.append([(r, c - by), s + by, visited])

    # for nr, nc in moves:
    #     if (
    #         (nr, nc) in visited
    #         or nr < 0
    #         or nr >= len(hiking_trail_map)
    #         or nc < 0
    #         or nc >= len(hiking_trail_map[0])
    #     ):
    #         continue
    #
    #     if hiking_trail_map[nr][nc] == "#":
    #         continue
    #
    #     ns = s + 1
    #     visited.add((nr, nc))
    #     np.append([(nr, nc), ns, visited])

    return np


if __name__ == "__main__":
    run()
