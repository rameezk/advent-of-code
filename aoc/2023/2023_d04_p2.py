from aoc.helper import download_input, submit_answer

import re

from collections import defaultdict


def play(S, M, C):
    new_cards = []

    for id_, w, h in S:
        I = w.intersection(h)
        if len(I):
            R = list(range(int(id_) + 1, int(id_) + len(I) + 1))
            for r in R:
                c = M[str(r)]
                C[str(r)] += 1
                new_cards.append([r, c[0], c[1]])

    if not len(new_cards):
        return C
    else:
        return play(new_cards, M, C)


if __name__ == "__main__":
    download_input(2023, 4)

    with open("./2023_d04.txt") as f:
        cards = f.read().strip().splitlines()

    #     cards = """
    # Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    # Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    # Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    # Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    # Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    # Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
    #         """.strip().splitlines()

    S = []
    M = {}
    C = defaultdict(lambda: 0)
    for card in cards:
        N, L = card.split(":")
        N = re.findall(r"\d+", N)[0]
        W, H = L.split("|")
        W = set(map(int, re.findall(r"\d+", W)))
        H = set(map(int, re.findall(r"\d+", H)))

        S.append([N, W, H])
        M[N] = [W, H]
        C[N] += 1

    C = play(S, M, C)
    T = sum(C.values())
    print(T)
    assert T == 5921508
    # submit_answer(2023, 4, 2, T)
