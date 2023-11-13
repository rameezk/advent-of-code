from aoc.helper import download_input, submit_answer

import itertools


def is_nice(s: str) -> bool:
    bad_strings = ["ab", "cd", "pq", "xy"]
    for bs in bad_strings:
        if bs in s:
            return False

    vowels = ["a", "e", "i", "o", "u"]
    vc = 0
    for v in vowels:
        vc += s.count(v)
        if vc >= 3:
            break

    if vc < 3:
        return False

    for c1, c2 in itertools.pairwise(s):
        if c1 == c2:
            return True

    return False


if __name__ == "__main__":
    # download_input(2015, 5)
    with open("./2015_d05.txt") as f:
        data = f.read().strip().splitlines()

    # data = [
    #     "ugknbfddgicrmopn",
    #     "aaa",
    #     "jchzalrnumimnmhp",
    #     "haegwjzuvuyypxyu",
    #     "dvszwmarrgswjxmb",
    # ]

    t = 0
    for line in data:
        if is_nice(line):
            t += 1

    print(t)
    submit_answer(2015, 5, 1, t)
