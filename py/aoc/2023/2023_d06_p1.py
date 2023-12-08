from aoc.helper import download_input, submit_answer

import re

from math import prod


def calculate_distance(total_time, time_pressed) -> int:
    assert time_pressed <= total_time
    speed = time_pressed
    time_left_to_move = total_time - time_pressed
    distance = speed * time_left_to_move
    return distance


if __name__ == "__main__":
    download_input(2023, 6)

    with open("./2023_d06.txt") as f:
        document = f.read().strip().splitlines()

    #     document = """
    # Time:      7  15   30
    # Distance:  9  40  200
    #     """.strip().splitlines()

    T = list(map(int, re.findall(r"\d+", document[0])))
    D = list(map(int, re.findall(r"\d+", document[1])))

    W = []
    for i in range(len(T)):
        t = T[i]
        d = D[i]

        C = 0
        for j in range(t + 1):
            dis = calculate_distance(t, j)
            if dis > d:
                C += 1
        W.append(C)

    P = prod(W)
    print(P)

    # submit_answer(2023, 6, 1, P)
