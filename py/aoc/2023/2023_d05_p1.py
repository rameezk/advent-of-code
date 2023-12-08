from aoc.helper import download_input, submit_answer

import re


def get_offset_target(data, target) -> int:
    for line in data:
        n1, n2, d = map(int, re.findall(r"\d+", line))

        if n2 <= target <= n2 + d:
            far = target - n2
            offset = far + n1
            return offset

    return target


def lookup(data, T) -> {}:
    M = {}
    for t in T:
        M[t] = get_offset_target(data, t)
    return M


if __name__ == "__main__":
    download_input(2023, 5)

    with open("./2023_d05.txt") as f:
        almanac = f.read().strip().split("\n\n")

    #     almanac = """
    # seeds: 79 14 55 13
    #
    # seed-to-soil map:
    # 50 98 2
    # 52 50 48
    #
    # soil-to-fertilizer map:
    # 0 15 37
    # 37 52 2
    # 39 0 15
    #
    # fertilizer-to-water map:
    # 49 53 8
    # 0 11 42
    # 42 0 7
    # 57 7 4
    #
    # water-to-light map:
    # 88 18 7
    # 18 25 70
    #
    # light-to-temperature map:
    # 45 77 23
    # 81 45 19
    # 68 64 13
    #
    # temperature-to-humidity map:
    # 0 69 1
    # 1 0 69
    #
    # humidity-to-location map:
    # 60 56 37
    # 56 93 4
    #         """.strip().split(
    #         "\n\n"
    #     )

    seeds = list(map(int, re.findall(r"\d+", almanac[0])))
    targets = seeds

    for a in almanac[1:]:
        a_l = a.splitlines()

        T = lookup(a_l[1:], targets)
        targets = T.values()

    R = min(targets)
    print(R)
    submit_answer(2023, 5, 1, R)
