from aoc.helper import download_input, submit_answer

import pathlib

if __name__ == "__main__":
    download_input(2024, 1)

    input_file = pathlib.Path(__file__).parent.resolve() / "./2024_d01.txt"

    with open(input_file) as f:
        data = f.read().strip().splitlines()

#     data = """3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3""".strip().splitlines()

    L = []
    R = []

    for line in data:
        l, r = line.split()
        L.append(int(l))
        R.append(int(r))

    S = 0
    for d in L:
        c = R.count(d)
        S += c * d

    print(S)
    submit_answer(2024, 1, 2, S)
