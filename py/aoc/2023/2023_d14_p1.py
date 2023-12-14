from aoc.helper import download_input, submit_answer


def move_rocks(path: list[str]) -> list[str]:
    n = len(path)

    for i in range(n - 1):
        for j in range(n - i - 1):
            c1, c2 = path[j], path[j + 1]
            if c1 == "." and c2 == "O":
                path[j], path[j + 1] = path[j + 1], path[j]

    return path


if __name__ == "__main__":
    download_input(2023, 14)

    raw_dish = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
    """.strip().splitlines()

    with open("./2023_d14.txt") as f:
        raw_dish = f.read().strip().splitlines()

    dish = []
    for row in raw_dish:
        dish.append(list(row))

    cw_dish = list(zip(*dish))

    n_cw_dish = []
    for col in cw_dish:
        n_cw_dish.append(move_rocks(list(col)))

    moved_dish = list(zip(*n_cw_dish))[::-1]

    T = 0
    for r, mv in enumerate(moved_dish, start=1):
        rocks = list(mv).count("O")
        T += rocks * r

    print(T)
    submit_answer(2023, 14, 1, T)
