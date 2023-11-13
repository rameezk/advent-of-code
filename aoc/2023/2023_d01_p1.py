from aoc.helper import download_input, submit_answer

import pathlib

import re

if __name__ == "__main__":
    # download_input(2023, 1)

    input_file = pathlib.Path(__file__).parent.resolve() / "./2023_d01.txt"

    with open(input_file) as f:
        data = f.read().strip().splitlines()

    #     sample = """
    # 1abc2
    # pqr3stu8vwx
    # a1b2c3d4e5f
    # treb7uchet
    #     """

    t = 0
    for s in data:
        d = re.findall(r"\d", s)
        n = d[0] + d[-1]
        t += int(n)

    print(t)
    # submit_answer(2023, 1, 1, t)
