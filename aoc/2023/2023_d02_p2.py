from aoc.helper import download_input, submit_answer

import pathlib

import re


def parse_colour(s, c) -> int:
    f = re.findall(rf"(\d+)\s+{c}", s)
    if len(f):
        return int(f[0])
    return 0


if __name__ == "__main__":
    # download_input(2023, 2)

    with open("./2023_d02.txt") as f:
        games = f.read().strip().splitlines()

    #     games = """
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    # Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    # Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    # Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    # Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
    #         """.strip().splitlines()

    T = 0
    for g in games:
        id_part, set_part = g.split(":")
        _, id_ = id_part.split(" ")
        sets = set_part.split(";")

        set_possible = True
        R, G, B = [0, 0, 0]
        for s in sets:
            r, g, b = [parse_colour(s, c) for c in ["red", "green", "blue"]]

            R = max(R, r)
            G = max(G, g)
            B = max(B, b)

        P = R * G * B
        T += P

    print(T)
    # submit_answer(2023, 2, 2, T)
