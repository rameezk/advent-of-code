from aoc.helper import download_input, submit_answer

import re

from collections import defaultdict

if __name__ == "__main__":
    download_input(2018, 3)

    #     claims = """
    # #1 @ 1,3: 4x4
    # #2 @ 3,1: 4x4
    # #3 @ 5,5: 2x2
    #         """.strip().splitlines()

    with open("./2018_d03.txt") as f:
        claims = f.read().strip().splitlines()

    fabric = defaultdict(lambda: [])
    all_claims = set()
    for claim in claims:
        id_, l, t, w, h = map(int, re.findall(r"\d+", claim))
        all_claims.add(id_)

        for r in range(t, t + h):
            for c in range(l, l + w):
                fabric[(r, c)].append(id_)

    bad_claims = set()
    for k, v in fabric.items():
        if len(v) > 1:
            bad_claims.update(v)

    intact_claims = all_claims.difference(bad_claims)
    assert len(intact_claims) == 1
    (R,) = intact_claims
    print(R)
    # submit_answer(2018, 3, 2, R)
