from aoc.helper import download_input, submit_answer


def split_at(pattern):
    for r in range(1, len(pattern)):
        above = pattern[:r][::-1]
        below = pattern[r:]

        above = above[: len(below)]
        below = below[: len(above)]

        if above == below:
            return r

    return 0


if __name__ == "__main__":
    download_input(2023, 13)

    raw_patterns = """
#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
    """

    with open("2023_d13.txt") as f:
        raw_patterns = f.read()

    patterns = []
    for p in raw_patterns.strip().split("\n\n"):
        patterns.append(p.splitlines())

    T = 0
    for pattern in patterns:
        r = split_at(pattern)
        c = split_at(list(zip(*pattern)))
        T += (r * 100) + c

    print(T)
    submit_answer(2023, 13, 1, T)
