from aoc.helper import download_input, submit_answer

import re

lookup = {
    "one": 1,
    "1": 1,
    "two": 2,
    "2": 2,
    "three": 3,
    "3": 3,
    "four": 4,
    "4": 4,
    "five": 5,
    "5": 5,
    "six": 6,
    "6": 6,
    "seven": 7,
    "7": 7,
    "eight": 8,
    "8": 8,
    "nine": 9,
    "9": 9,
}


def get_digits(s: str):
    P = []
    for look in lookup.keys():
        p1 = s.find(look)
        p2 = s.rfind(look)
        if p1 >= 0:
            P.append([p1, lookup[look]])
        if p2 >= 0:
            P.append([p2, lookup[look]])

    P = sorted(P, key=lambda x: x[0])
    return [p[1] for p in P]


if __name__ == "__main__":
    # download_input(2023, 1)

    with open("./2023_d01.txt") as f:
        data = f.read().strip().splitlines()

    # sample = """
    # 74one27
    # two1nine
    # eightwothree
    # abcone2threexyz
    # xtwone3four
    # 4nineeightseven2
    # zoneight234
    # 7pqrstsixteen
    #         """

    # data = sample.strip().splitlines()

    t = 0
    for s in data:
        d = get_digits(s)
        n = str(d[0]) + str(d[-1])
        t += int(n)

    print(t)
    # submit_answer(2023, 1, 2, t)
