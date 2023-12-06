from aoc.helper import download_input, submit_answer

import re


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
    #                     """.strip().split(
    #         "\n\n"
    #     )

    seeds = list(map(int, re.findall(r"\d+", almanac[0])))

    sp = []
    for i in range(0, len(seeds), 2):
        sp.append((seeds[i], seeds[i] + seeds[i + 1]))

    for m in almanac[1:]:
        a_l = m.splitlines()[1:]
        P = []
        for l in a_l:
            a, b, c = map(int, l.split())
            P.append([a, b, c])

        N = []
        while len(sp) > 0:
            ss, se = sp.pop()

            for a, b, c in P:
                os = max(ss, b)
                oe = min(se, b + c)

                if os < oe:
                    N.append((os - b + a, oe - b + a))
                    if os > ss:
                        sp.append((ss, os))
                    if se > oe:
                        sp.append((oe, se))
                    break
            else:
                N.append((ss, se))
        sp = N

    R = sorted(sp)[0][0]
    print(R)
    # submit_answer(2023, 5, 2, R)
