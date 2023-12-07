from aoc.helper import download_input, submit_answer

import re

import time


def calculate_distance(total_time, time_pressed) -> int:
    assert time_pressed <= total_time
    speed = time_pressed
    time_left_to_move = total_time - time_pressed
    distance = speed * time_left_to_move
    return distance


if __name__ == "__main__":
    start = time.time()

    download_input(2023, 6)

    with open("./2023_d06.txt") as f:
        document = f.read().strip().splitlines()

    #     document = """
    # Time:      7  15   30
    # Distance:  9  40  200
    #             """.strip().splitlines()

    t = int("".join(re.findall(r"\d+", document[0])))
    d = int("".join(re.findall(r"\d+", document[1])))

    C = 0

    L = None
    R = None

    for j in range(t + 1):
        dis = calculate_distance(t, j)
        if dis > d:
            L = j
            break

    for j in range(t, -1, -1):
        dis = calculate_distance(t, j)
        if dis > d:
            R = j
            break

    C = R - L + 1
    print(C)

    end = time.time()

    print((end - start) * 1000)

    # submit_answer(2023, 6, 2, C)
