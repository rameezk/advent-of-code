from aoc.helper import download_input, submit_answer

import re

if __name__ == "__main__":
    download_input(2023, 8)

    with open("./2023_d08.txt") as f:
        data = f.read().strip().splitlines()

    #     data = """
    # RL
    #
    # AAA = (BBB, CCC)
    # BBB = (DDD, EEE)
    # CCC = (ZZZ, GGG)
    # DDD = (DDD, DDD)
    # EEE = (EEE, EEE)
    # GGG = (GGG, GGG)
    # ZZZ = (ZZZ, ZZZ)
    #     """.strip().splitlines()

    D, NR = data[0], data[2:]
    D = list(D)

    N = {}
    for n in NR:
        n1, n2, n3 = re.findall(r"[A-Z]{3}", n)
        N[n1] = (n2, n3)

    n = "AAA"
    c = 0
    l = len(D)
    while n != "ZZZ":
        d = D[c % l]
        i = 0 if d == "L" else 1
        nx = N[n][i]
        n = nx
        c += 1

    print(c)
    # submit_answer(2023, 8, 1, c)
