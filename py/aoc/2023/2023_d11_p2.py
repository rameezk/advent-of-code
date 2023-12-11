from aoc.helper import download_input, submit_answer

from itertools import combinations


def get_cols_rows_to_be_expanded(galaxies: list[list[str]]) -> (list[int], list[int]):
    rows_to_expand = []
    for r, row in enumerate(galaxies):
        if all(ch == "." for ch in row):
            rows_to_expand.append(r)

    cols_to_expand = []
    for c, col in enumerate(zip(*galaxies)):
        if all(ch == "." for ch in col):
            cols_to_expand.append(c)

    return rows_to_expand, cols_to_expand


def build_galaxy_map(
    galaxies: list[list[str]],
) -> dict[int, tuple[int, int]]:
    i = 1
    M = {}

    for r, row in enumerate(galaxies):
        for c, col in enumerate(row):
            if col == "#":
                M[i] = (r, c)
                i += 1

    return M


def apply_cosmic_expansion(
    galaxies_map: dict[int, tuple[int, int]],
    rows_to_expand: list[int],
    cols_to_expand: list[int],
    expansion_multiplier: int,
) -> dict[int, tuple[int, int]]:
    for k, (r, c) in galaxies_map.items():
        count_left = len([x for x in cols_to_expand if x < c])
        count_top = len([x for x in rows_to_expand if x < r])
        galaxies_map[k] = (
            r + (count_top * (expansion_multiplier - 1)),
            c + (count_left * (expansion_multiplier - 1)),
        )

    return galaxies_map


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
    #         """.strip().splitlines()

    galaxies = []
    for row in image:
        galaxies.append(list(row))

    rows_to_expand, cols_to_expand = get_cols_rows_to_be_expanded(galaxies)

    galaxies_map = build_galaxy_map(galaxies)
    galaxies_map = apply_cosmic_expansion(
        galaxies_map, rows_to_expand, cols_to_expand, 1000000
    )

    galaxy_ids = list(range(1, len(galaxies_map) + 1))

    S = 0
    for comb in combinations(galaxy_ids, 2):
        s = get_shortest_path(galaxies_map[comb[0]], galaxies_map[comb[1]])
        S += s

    print(S)
    # submit_answer(2023, 11, 2, S)
