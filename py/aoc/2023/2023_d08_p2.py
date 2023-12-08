from aoc.helper import download_input, submit_answer

from aoc.util import benchmark

import re

from math import lcm


@benchmark
def run():
    download_input(2023, 8)

    with open("./2023_d08.txt") as f:
        data = f.read().strip().splitlines()

    # data = """
    # LR
    #
    # 11A = (11B, XXX)
    # 11B = (XXX, 11Z)
    # 11Z = (11B, XXX)
    # 22A = (22B, XXX)
    # 22B = (22C, 22C)
    # 22C = (22Z, 22Z)
    # 22Z = (22B, 22B)
    # XXX = (XXX, XXX)
    #         """.strip().splitlines()

    D, NR = data[0], data[2:]
    D = list(D)

    N = {}
    sn = []
    for n in NR:
        n1, n2, n3 = re.findall(r"[A-Z0-9]{3}", n)
        N[n1] = (n2, n3)
        if n1[-1] == "A":
            sn.append(n1)

    R = []
    for n in sn:
        c = 0
        l = len(D)
        while n[-1] != "Z":
            d = D[c % l]
            i = 0 if d == "L" else 1
            nx = N[n][i]
            n = nx
            c += 1
        R.append(c)

    T = lcm(*R)
    print(T)
    # submit_answer(2023, 8, 2, T)


if __name__ == "__main__":
    run()
