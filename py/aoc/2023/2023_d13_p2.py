from aoc.helper import download_input, submit_answer


def split_at(pattern):
    for r in range(1, len(pattern)):
        above = pattern[:r][::-1]
        below = pattern[r:]

        differences = 0

        for n1, n2 in zip(above, below):
            for nn1, nn2 in zip(n1, n2):
                if nn1 != nn2:
                    differences += 1

        if differences == 1:
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
    assert T == 34795
    submit_answer(2023, 13, 2, T)
