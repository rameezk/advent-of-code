from aoc.helper import download_input, submit_answer

from itertools import combinations


def print_galaxies(galaxies: list[list[str]]):
    for row in galaxies:
        print("".join(row))


def apply_cosmic_expansion(galaxies: list[list[str]]) -> list[list[str]]:
    rows_to_expand = []
    for r, row in enumerate(galaxies):
        if all(ch == "." for ch in row):
            rows_to_expand.append(r)

    inserted = 0
    for r in rows_to_expand:
        galaxies.insert(r + inserted, galaxies[r + inserted])
        inserted += 1

    cols_to_expand = []
    for c, col in enumerate(zip(*galaxies)):
        if all(ch == "." for ch in col):
            cols_to_expand.append(c)

    transposed_galaxy = list(zip(*galaxies))
    inserted = 0
    for c in cols_to_expand:
        transposed_galaxy.insert(c + inserted, transposed_galaxy[c + inserted])
        inserted += 1

    galaxies = list(zip(*transposed_galaxy))
    galaxies = [list(g) for g in galaxies]
    return galaxies


def build_galaxy_map(
    galaxies: list[list[str]],
) -> (list[list[str]], dict[int, tuple[int, int]], list[int]):
    i = 1
    M = {}
    galaxy_ids = []

    for r, row in enumerate(galaxies):
        for c, col in enumerate(row):
            if col == "#":
                M[i] = (r, c)
                galaxies[r][c] = str(i)
                galaxy_ids.append(i)
                i += 1

    return galaxies, M, galaxy_ids


def get_shortest_path(start: tuple[int, int], end: tuple[int, int]) -> int:
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


if __name__ == "__main__":
    download_input(2023, 11)

    with open("./2023_d11.txt") as f:
        image = f.read().strip().splitlines()

    #     image = """
    # ...#......
    # .......#..
    # #.........
    # ..........
    # ......#...
    # .#........
    # .........#
    # ..........
    # .......#..
    # #...#.....
    #     """.strip().splitlines()

    galaxies = []
    for row in image:
        galaxies.append(list(row))

    galaxies = apply_cosmic_expansion(galaxies)
    galaxies, galaxies_map, galaxy_ids = build_galaxy_map(galaxies)

    S = 0
    for comb in combinations(galaxy_ids, 2):
        s = get_shortest_path(galaxies_map[comb[0]], galaxies_map[comb[1]])
        S += s

    print(S)
    # submit_answer(2023, 11, 1, S)
