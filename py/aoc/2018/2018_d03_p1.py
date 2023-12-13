from aoc.helper import download_input, submit_answer

import re

from collections import defaultdict

if __name__ == "__main__":
    download_input(2018, 3)

    #     claims = """
    # #1 @ 1,3: 4x4
    # #2 @ 3,1: 4x4
    # #3 @ 5,5: 2x2
    #     """.strip().splitlines()

    with open("./2018_d03.txt") as f:
        claims = f.read().strip().splitlines()

    fabric = defaultdict(lambda: 0)

    for claim in claims:
        _, l, t, w, h = map(int, re.findall(r"\d+", claim))

        for r in range(t, t + h):
            for c in range(l, l + w):
                fabric[(r, c)] += 1

    T = len([f for f in fabric.values() if f >= 2])
    print(T)
    submit_answer(2018, 3, 1, T)
