from aoc.helper import download_input, submit_answer

import re


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
    #     """.strip().splitlines()

    T = 0
    for card in cards:
        _, L = card.split(":")
        W, H = L.split("|")
        W = set(map(int, re.findall(r"\d+", W)))
        H = set(map(int, re.findall(r"\d+", H)))
        I = W.intersection(H)

        if len(I):
            s = 1
            for i in range(1, len(I)):
                s = s * 2
            T += s

    print(T)
    submit_answer(2023, 4, 1, T)
